from dotenv import load_dotenv
from core.utils import clear_screen
import google.generativeai as genai
import os

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

def run_ai_runbook_generator():
    """Realiza a chamada para o Google Gemini e faz o tratamento do conteúdo do runbook gerado."""
    clear_screen()
    print("\n--- Gerar Runbook com IA ---")
    threat_name = input("Digite o nome da ameaça para a qual deseja gerar o runbook: ")
    
    # --- Chamada para a IA ---
    print("\nSolicitando ao Google Gemini para gerar o runbook...")
    runbook_code = generate_runbook_content(threat_name)
    
    if runbook_code:
        print("\nCódigo do runbook gerado. Verifique no console e confirme se deseja salvar:")
        print("--- INÍCIO DO CÓDIGO ---")
        print(runbook_code)
        print("--- FIM DO CÓDIGO ---")

        blue_color = "\033[94m"
        yellow_bold = "\033[1;93m"
        reset_color = "\033[0m"

        print(f"\n{blue_color}Certifique-se de revisar o código gerado antes de utilizá-lo em um ambiente de produção.{reset_color}")
        print(f"{blue_color}Verifique especialmente as validações de entrada e a lógica de cada passo.{reset_color}")
        print(f"{blue_color}Além disso, confirme se o runbook atende às suas políticas internas de segurança e conformidade.{reset_color}")
        print(f"\n{yellow_bold}O Gemini pode gerar código com erros ou imprecisões. Por isso, revisão humana é essencial.{reset_color}")
        
        save_option = input("\nDeseja salvar este runbook em um arquivo (S/N)? ").upper()
        if save_option == 'S':
            save_runbook_to_file(threat_name, runbook_code.replace('```python', '').replace('```', '').strip())
    
    input("\nPressione Enter para continuar...")

def generate_runbook_content(threat_name):
    """
    Gera o conteúdo de um runbook para uma ameaça específica utilizando o Google Gemini.
    """
    # Tenta obter a chave de API da variável de ambiente
    API_KEY = os.getenv("GEMINI_API_KEY")
    if not API_KEY:
        print("Erro: A chave de API 'GEMINI_API_KEY' não está configurada nas variáveis de ambiente.")
        return None
        
    genai.configure(api_key=API_KEY)
    
    model = genai.GenerativeModel('gemini-1.5-flash')
    
    prompt = f"""
    Crie um runbook de segurança cibernética em Python para a ameaça '{threat_name}'.
    Considere subpassos detalhados e perguntas de verificação para um analista seguir.
    O runbook deve ter validações de falsos positivos e negativos.
    O runbook deve ser um script Python completo, nomeado como '{threat_name.replace(" ", "_").lower()}.py'.
    Siga as seguintes regras e formato exato:
    1. O script deve importar a função 'end_menu' de 'core.menu'.
    2. A lógica principal deve estar em uma função chamada 'run()'.
    3. A função 'run()' deve ter uma lista vazia chamada 'report_content' para armazenar os passos.
    4. Cada passo do runbook deve ter a seguinte estrutura:
        - Uma linha de progresso: print(f"\\n[PASSO X/Y] - Nome do Passo (Z% concluído)")
        - Uma instrução para o analista: print("Instrução: ...")
        - A porcentagem deve ser calculada com base no número total de passos.
    5. O runbook deve ter uma validação de entrada de 'S' ou 'N' para cada pergunta e adicionar um dicionário com o status ('success' ou 'failure') e uma mensagem ao 'report_content'.
    6. Exemplo de validação de S/N:
        response = input("O host foi isolado? (S/N): ").upper()
        while response not in ('S', 'N'):
            response = input("Resposta inválida. Por favor, digite S ou N: ").upper()
        if response == 'S':
            report_content.append({{"status": "success", "message": "Passo X: Host isolado com sucesso."}})
        else:
            report_content.append({{"status": "failure", "message": "Passo X: Falha ao isolar o host."}})
    7. No final da função 'run()', retorne a chamada para 'end_menu' com os parâmetros corretos. A chamada deve ser:
        return end_menu(report_content, '{threat_name.replace(" ", "_").lower()}', Nome completo da ameaça)
    8. Quando houver um falso positivo, o runbook deve retornar a função 'end_menu' do módulo 'core.menu'.
    9. O runbook deve ser gerado em português do Brasil e não deve conter a notação de código ````python```` no início e no fim.

    Gere somente o código Python completo.
    """
    
    try:
        response = model.generate_content(prompt)
        # Remove a formatação extra do Gemini
        runbook_content = response.text.strip('`').strip('python\n')
        
        # Corrige caracteres especiais
        runbook_content = runbook_content.replace('Ã§', 'ç').replace('Ã£', 'ã').replace('Ãµ', 'õ')
        
        return runbook_content
    except Exception as e:
        print(f"Erro ao gerar o conteúdo com a IA: {e}")
        return None

def save_runbook_to_file(threat_name, content):
    """
    Salva o conteúdo do runbook em um arquivo na pasta 'runbooks'.
    """
    runbooks_dir = "runbooks"
    if not os.path.exists(runbooks_dir):
        os.makedirs(runbooks_dir)
    
    sanitized_threat_name = threat_name.replace(" ", "_").replace("-", "_").lower()
    filename = os.path.join(runbooks_dir, f"{sanitized_threat_name}.py")
    
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"\nSucesso: O runbook '{filename}' foi gerado e salvo na pasta 'runbooks'.")
    except Exception as e:
        print(f"Erro ao salvar o arquivo: {e}")