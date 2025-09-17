from core.utils import generate_report, clear_screen
import importlib
import glob
import sys
import os

def runbook_menu():
    """Exibe o menu de runbooks disponíveis e permite execução ou consulta."""
    runbooks_dir = "runbooks"
    all_runbooks = [os.path.basename(f)[:-3] for f in glob.glob(os.path.join(runbooks_dir, '*.py')) if os.path.basename(f) != '__init__.py']
    
    while True:
        clear_screen()
        print("\n--- Menu de Runbooks ---")
        if not all_runbooks:
            print("Nenhum runbook disponível.")
            input("Pressione Enter para voltar ao menu principal...")
            return

        print("Runbooks Disponíveis:")
        for i, rb in enumerate(all_runbooks):
            print(f" {i+1}. {rb}")
        
        print("\nOpções:")
        print("1. Executar um runbook (por número)")
        print("2. Consultar um runbook (por nome)")
        print("\n0. Voltar ao menu principal")
        print("---------------------------")
        
        try:
            choice = int(input("Escolha uma opção: "))
            
            if choice == 0:
                return
            elif choice == 1:
                runbook_num = int(input("\nDigite o número do runbook para executar: "))
                if 1 <= runbook_num <= len(all_runbooks):
                    runbook_name = all_runbooks[runbook_num - 1]
                    clear_screen()
                    module = importlib.import_module(f"{runbooks_dir}.{runbook_name}")
                    if hasattr(module, 'run'):
                        module.run()
                    else:
                        print(f"Erro: A função 'run' não foi encontrada no runbook '{runbook_name}'.")
                    return
                else:
                    print("Número inválido. Tente novamente.")
                    input("Pressione Enter para continuar...")
            elif choice == 2:
                consult_runbook(all_runbooks)
            else:
                print("Escolha inválida. Tente novamente.")
                input("Pressione Enter para continuar...")
        except ValueError:
            print("Entrada inválida. Digite um número.")
            input("Pressione Enter para continuar...")

def consult_runbook(all_runbooks):
    """Lida com a busca e execução de um runbook específico."""
    while True:
        clear_screen()
        print("\n--- Consultar Runbook ---")
        print("Digite o nome do runbook que deseja consultar ou '0' para voltar.")
        search_query = input("Buscar > ").lower()

        if search_query == '0':
            return
            
        filtered_runbooks = [rb for rb in all_runbooks if search_query in rb.lower()]
        
        if not filtered_runbooks:
            print(f"\nNenhum runbook encontrado para o termo '{search_query}'.")
            input("Pressione Enter para tentar novamente...")
            continue
            
        # Exibe apenas o primeiro resultado encontrado
        runbook_name = filtered_runbooks[0]
        
        print(f"\nRunbook encontrado: {runbook_name}")
        print("Opções:")
        print("1. Executar este runbook")
        print("0. Voltar para o menu anterior")
        print("---------------------------")
        
        try:
            choice = int(input("Escolha uma opção: "))
            if choice == 0:
                continue
            elif choice == 1:
                runbooks_dir = "runbooks"
                clear_screen()
                module = importlib.import_module(f"{runbooks_dir}.{runbook_name}")
                if hasattr(module, 'run'):
                    module.run()
                else:
                    print(f"Erro: A função 'run' não foi encontrada no runbook '{runbook_name}'.")
                return
            else:
                print("Escolha inválida. Tente novamente.")
                input("Pressione Enter para continuar...")
        except ValueError:
            print("Entrada inválida. Digite um número.")
            input("Pressione Enter para continuar...")

def end_menu(report_content, threat_name, runbook_name_full):
    """Exibe o menu final após a execução do runbook."""
    while True:
        print("\n---------------------------------")
        print("Execução do Runbook Concluída")
        print("1. Gerar relatório (PDF)")
        print("2. Retornar ao menu principal")
        print("\n0. Sair do programa")
        print("---------------------------------")
        
        choice = input("Digite sua escolha: ")
        
        if choice == '0':
            print("Saindo do programa.")
            sys.exit()
        elif choice == '1':
            generate_report(report_content, threat_name, runbook_name_full)
        elif choice == '2':
            input("Execução finalizada. Pressione Enter para continuar...")
            return
        else:
            print("Escolha inválida. Tente novamente.")
            input("Pressione Enter para continuar...")