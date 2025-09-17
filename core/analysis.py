from core.utils import clear_screen
from core.ai import run_ai_runbook_generator
import pandas as pd
import glob
import os

def run_analysis():
    """
    Função principal para executar a análise a partir do menu.
    Coleta os arquivos da pasta 'data' e solicita a seleção ao usuário.
    """
    clear_screen()
    data_dir = "data"
    
    if not os.path.exists(data_dir):
        print(f"Erro: O diretório '{data_dir}' não foi encontrado.")
        input("Pressione Enter para retornar...")
        return

    # Lista todos os arquivos .csv disponíveis na pasta 'data'
    available_files = [f for f in os.listdir(data_dir) if f.endswith('.csv')]
    
    if not available_files:
        print(f"Erro: Nenhum arquivo CSV foi encontrado no diretório '{data_dir}'.")
        input("Pressione Enter para retornar...")
        return
    
    while True:
        print("\nAnálise de logs x indicadores (IoC)")
        print("---------------------------------------")
        print(f"Arquivos CSV disponíveis no diretório '{data_dir}':")
        for f in available_files:
            print(f" - {f}")

        print("\nInsira o nome dos arquivos a serem analisados (separados por espaço):")
        print("O primeiro arquivo deve ser o de indicadores (e.g., indicadores.csv).")
        print("O(s) demais arquivo(s) será(ão) tratado(s) como log(s) de detecção.")
        
        user_input = input("\n> ")
        file_names = user_input.split()
        
        if len(file_names) < 2:
            print("Entrada inválida. Você precisa fornecer pelo menos um arquivo de indicadores e um arquivo de log.")
            input("Pressione Enter para tentar novamente...")
            continue
            
        indicator_file = os.path.join(data_dir, file_names[0])
        log_files = [os.path.join(data_dir, f) for f in file_names[1:]]
        
        threats_found = analyze_logs(indicator_file, log_files)
        
        # Se nenhuma ameaça for encontrada, informa o usuário e espera um comando
        if not threats_found:
            print("Nenhuma ameaça correlacionada encontrada nos logs.")
            input("\nPressione Enter para retornar ao menu principal...")
        else:
            # Se ameaças forem encontradas, exibe o menu pós-análise
            post_analysis_menu()
        
        return

def analyze_logs(indicator_file, log_files):
    """
    Analisa logs de detecção e e-mail e correlaciona com indicadores de ameaças.
    Retorna uma lista de ameaças encontradas.
    """
    clear_screen()
    print(f"[*] Analisando logs com base em '{indicator_file}'...")
    try:
        indicators_df = pd.read_csv(indicator_file, low_memory=False)
        if 'indicator' not in indicators_df.columns:
            print(f"[!] Erro: A coluna 'indicator' não foi encontrada em '{indicator_file}'.")
            return []

        # Cria um mapa para busca rápida de 'malware_families' por indicador
        indicator_map = pd.Series(
            indicators_df.malware_families.values,
            index=indicators_df.indicator
        ).to_dict()
        
        indicator_set = set(indicators_df['indicator'])
        print(f"[*] {len(indicator_set)} indicadores únicos carregados.")
        
    except FileNotFoundError:
        print(f"[!] Erro: Arquivo de indicadores '{indicator_file}' não encontrado.")
        return []
    except Exception as e:
        print(f"[!] Erro ao ler o arquivo de indicadores: {e}")
        return []

    found_threats = set()

    print("\n--- Iniciando Correlação ---")
    for log_file in log_files:
        log_name = os.path.basename(log_file)
        print(f"\n\n  [*] Processando arquivo de log: '{log_name}'...")
        try:
            log_df = pd.read_csv(log_file, low_memory=False)
            
            # Identifica dinamicamente colunas que possam conter IoCs (hashes)
            potential_ioc_columns = [
                col for col in log_df.columns 
                if 'sha256' in col.lower() or 'sha1' in col.lower() or 'md5' in col.lower() or 'hash' in col.lower()
            ]
            # Adiciona colunas comuns extras que podem não seguir o padrão
            potential_ioc_columns.extend(['indicator', 'Sample sha256', 'parent_process_hash', 'process_hash'])
            potential_ioc_columns = list(set(col for col in potential_ioc_columns if col in log_df.columns))

            if not potential_ioc_columns:
                print(f"  [-] Nenhuma coluna de hash potencial encontrada em '{log_name}'.")
                continue

            found_in_file = False
            for index, row in log_df.iterrows():
                for col in potential_ioc_columns:
                    value = row[col]
                    if pd.notna(value) and value in indicator_set:
                        threat_name = indicator_map.get(value, "Nome Desconhecido")
                        
                        # --- EXIBIÇÃO DETALHADA ---
                        print(f"  [+] AMEAÇA ENCONTRADA!")
                        print(f"    - Nome da Ameaça: {threat_name}")
                        print(f"    - Indicador.....: {value}")
                        print(f"    - Arquivo de Log: {log_name}")
                        print(f"    - Coluna........: {col}")
                        # --------------------------------------------------
                        
                        found_threats.add(threat_name)
                        found_in_file = True
            
            if not found_in_file:
                print(f"  [-] Nenhuma ameaça correlacionada em '{log_name}'.")


        except Exception as e:
            error_message = f"[!] Erro ao processar '{log_name}': {e}"
            print(error_message)
    
    print("--------------------------\n")

    # Verificação de runbooks existentes
    available_runbooks = [os.path.basename(f)[:-3] for f in glob.glob('runbooks/*.py') if os.path.basename(f) != '__init__.py']
    
    analyzed_threats = []
    for threat in found_threats:
        # Verifica se o nome da ameaça ou um termo relacionado existe nos runbooks
        is_available = any(threat.lower() in rb.lower() for rb in available_runbooks)
        analyzed_threats.append({"name": threat, "available": is_available})

    # Exibição do resumo
    print("\n--- Resumo da Análise ---")
    print("Arquivos de log analisados:")
    for file in log_files:
        print(f" - {file}")

    green_color = "\033[92m"
    red_color = "\033[91m"
    reset_color = "\033[0m"

    # Caso o runbook esteja disponível, exibe em verde; caso contrário, em vermelho
    print("\nAmeaças identificadas e status do Runbook:")
    for threat in analyzed_threats:
        status = "disponível" if threat["available"] else "indisponível"
        color = green_color if threat["available"] else red_color
        print(f"{threat['name']} ({color}{status}{reset_color})")
        
    print("-------------------------\n")
    
    return analyzed_threats

def post_analysis_menu():
    """
    Exibe o menu de pós-análise.
    """
    while True:
        print("\n--- Análise Finalizada ---")
        print("Opções:")
        print("1. Gerar runbook com IA")
        print("0. Voltar ao menu principal")
        print("---------------------------")
        
        choice = input("Digite sua escolha: ")
        
        if choice == '0':
            return
        elif choice == '1':
            run_ai_runbook_generator()
        else:
            print("Escolha inválida. Tente novamente.")
            input("Pressione Enter para continuar...")