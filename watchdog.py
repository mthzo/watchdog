import os
import importlib
import sys

def clear_screen():
    """Limpa a tela do terminal."""
    os.system('cls' if os.name == 'nt' else 'clear')

def load_runbooks():
    """Carrega os scripts de runbook do diretório 'runbooks'."""
    runbooks = {}
    runbooks_dir = 'runbooks'
    
    if not os.path.exists(runbooks_dir):
        print(f"Erro: O diretório '{runbooks_dir}' não foi encontrado.")
        return runbooks
        
    # Lista arquivos .py no diretório 'runbooks', exceto watchdog.py e __init__.py
    script_files = [f for f in os.listdir(runbooks_dir) if f.endswith('.py') and f not in ['watchdog.py', '__init__.py']]
    
    for filename in script_files:
        module_name = filename[:-3]
        runbooks[module_name] = f"{runbooks_dir}.{module_name}"
    
    return runbooks

def main_menu():
    """Exibe o menu principal e aguarda a seleção do usuário."""
    while True:
        clear_screen()
        print(" _    _       _       _    ______            ")
        print("| |  | |     | |     | |   |  _  \           ")
        print("| |  | | __ _| |_ ___| |__ | | | |___   __ _ ")
        print("| |/\| |/ _` | __/ __| '_ \| | | / _ \ / _` |")
        print("\  /\  / (_| | || (__| | | | |/ / (_) | (_| |")
        print(" \/  \/ \__,_|\__\___|_| |_|___/ \___/ \__, |")
        print("                                        __/ |")
        print("                                       |___/ ")
        print("---------------------------------")
        print("1. Executar runbook")
        print("2. Sair")
        print("---------------------------------")
        
        choice = input("Digite sua escolha: ")
        
        if choice == '1':
            runbook_menu()
        elif choice == '2':
            print("Saindo do programa.")
            sys.exit()
        else:
            print("Escolha inválida. Tente novamente.")
            input("Pressione Enter para continuar...")

def runbook_menu():
    """Exibe o menu de runbooks e executa o selecionado."""
    runbooks = load_runbooks()
    
    while True:
        clear_screen()
        print("Runbooks Disponíveis")
        print("---------------------------------")
        
        sorted_runbooks = sorted(runbooks.keys())
        
        for i, name in enumerate(sorted_runbooks, 1):
            print(f"{i}. {name}")
        
        print("---------------------------------")
        print("0. Retornar ao menu principal")
        print("---------------------------------")
        
        try:
            choice = int(input("Digite o número do runbook que deseja executar: "))
            
            if choice == 0:
                break
            
            if 1 <= choice <= len(sorted_runbooks):
                selected_runbook_name = sorted_runbooks[choice - 1]
                
                module = importlib.import_module(runbooks[selected_runbook_name])
                clear_screen()
                
                if hasattr(module, 'run'):
                    should_return_to_main = module.run()
                    if should_return_to_main:
                        break
                    else:
                        continue
                else:
                    print(f"Erro: O runbook '{selected_runbook_name}' não possui a função 'run'.")
                    input("Pressione Enter para continuar...")
            else:
                print("Escolha inválida. Tente novamente.")
                input("Pressione Enter para continuar...")
        
        except (ValueError, IndexError):
            print("Entrada inválida. Digite um número da lista.")
            input("Pressione Enter para continuar...")

if __name__ == "__main__":
    main_menu()