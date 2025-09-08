from core.utils import generate_report
import sys

def end_menu(report_content, threat_name, runbook_name_full):
    """Exibe o menu de finalização e retorna a escolha do usuário."""
    while True:
        print("\n---------------------------------")
        print("Execução do Runbook Concluída")
        print("1. Gerar relatório (PDF)")
        print("2. Retornar ao menu principal")
        print("3. Sair do programa")
        print("---------------------------------")
        
        choice = input("Digite sua escolha: ")
        
        if choice == '1':
            generate_report(report_content, threat_name, runbook_name_full)
        elif choice == '2':
            print("Retornando ao menu principal...")
            return True
        elif choice == '3':
            print("Saindo do programa.")
            sys.exit()
        else:
            print("Escolha inválida. Tente novamente.")
            input("Pressione Enter para continuar...")