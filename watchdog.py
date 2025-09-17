from core.utils import clear_screen
from core.menu import runbook_menu
from core.ai import run_ai_runbook_generator
from core.analysis import run_analysis
import sys

def main():
    """Exibe o menu principal e aguarda a seleção do usuário."""
    while True:
        clear_screen()
        print(r" _    _       _       _    ______            ")
        print(r"| |  | |     | |     | |   |  _  \           ")
        print(r"| |  | | __ _| |_ ___| |__ | | | |___   __ _ ")
        print(r"| |/\| |/ _` | __/ __| '_ \| | | / _ \ / _` |")
        print(r"\  /\  / (_| | || (__| | | | |/ / (_) | (_| |")
        print(r" \/  \/ \__,_|\__\___|_| |_|___/ \___/ \__, |")
        print(r"                                        __/ |")
        print(r"                                       |___/ ")
        print("---------------------------------")
        print("1. Executar runbook")
        print("2. Gerar runbook com IA")
        print("3. Análise de logs x indicadores (IoC)")
        print("\n0. Sair")
        print("---------------------------------")
        
        choice = input("Digite sua escolha: ")
        
        if choice == '0':
            print("Saindo do programa.")
            sys.exit()
        elif choice == '1':
            runbook_menu()
        elif choice == '2':
            run_ai_runbook_generator()
        elif choice == '3':
            run_analysis()
        else:
            print("Escolha inválida. Tente novamente.")
            input("Pressione Enter para continuar...")

if __name__ == "__main__":
    main()