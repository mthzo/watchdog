from core.menu import end_menu

def run():
    report_content = []
    total_steps = 7

    # Passo 1: Isolamento do Host
    print(f"\n[PASSO 1/{total_steps}] - Isolamento do Host (0% concluído)")
    print("Instrução: Isole o host infectado da rede para evitar propagação.")
    response = input("O host foi isolado? (S/N): ").upper()
    while response not in ('S', 'N'):
        response = input("Resposta inválida. Por favor, digite S ou N: ").upper()
    if response == 'S':
        report_content.append({"status": "success", "message": "Passo 1: Host isolado com sucesso."})
    else:
        report_content.append({"status": "failure", "message": "Passo 1: Falha ao isolar o host."})

    # Passo 2: Análise de Logs
    print(f"\n[PASSO 2/{total_steps}] - Análise de Logs (14% concluído)")
    print("Instrução: Analise os logs do sistema para identificar a atividade maliciosa do Xworm.")
    response = input("Logs analisados e atividade maliciosa identificada? (S/N): ").upper()
    while response not in ('S', 'N'):
        response = input("Resposta inválida. Por favor, digite S ou N: ").upper()
    if response == 'S':
        report_content.append({"status": "success", "message": "Passo 2: Logs analisados e atividade maliciosa identificada."})
    else:
        report_content.append({"status": "failure", "message": "Passo 2: Falha na análise de logs."})


    # Passo 3: Remoção de arquivos maliciosos
    print(f"\n[PASSO 3/{total_steps}] - Remoção de Arquivos Maliciosos (29% concluído)")
    print("Instrução: Remova todos os arquivos e pastas relacionados ao Xworm.")
    response = input("Arquivos maliciosos removidos? (S/N): ").upper()
    while response not in ('S', 'N'):
        response = input("Resposta inválida. Por favor, digite S ou N: ").upper()
    if response == 'S':
        report_content.append({"status": "success", "message": "Passo 3: Arquivos maliciosos removidos com sucesso."})
    else:
        report_content.append({"status": "failure", "message": "Passo 3: Falha na remoção de arquivos maliciosos."})

    # Passo 4: Verificação de processos maliciosos
    print(f"\n[PASSO 4/{total_steps}] - Verificação de Processos Maliciosos (43% concluído)")
    print("Instrução: Verifique se há processos relacionados ao Xworm em execução.")
    response = input("Processos maliciosos encontrados e finalizados? (S/N): ").upper()
    while response not in ('S', 'N'):
        response = input("Resposta inválida. Por favor, digite S ou N: ").upper()
    if response == 'S':
        report_content.append({"status": "success", "message": "Passo 4: Processos maliciosos finalizados com sucesso."})
    else:
        report_content.append({"status": "failure", "message": "Passo 4: Falha na finalização de processos maliciosos."})

    # Passo 5: Restauração de Sistema (se necessário)
    print(f"\n[PASSO 5/{total_steps}] - Restauração de Sistema (57% concluído)")
    print("Instrução: Se necessário, restaure o sistema a um ponto anterior à infecção.")
    response = input("Sistema restaurado? (S/N): ").upper()
    while response not in ('S', 'N'):
        response = input("Resposta inválida. Por favor, digite S ou N: ").upper()
    if response == 'S':
        report_content.append({"status": "success", "message": "Passo 5: Sistema restaurado com sucesso."})
    else:
        report_content.append({"status": "failure", "message": "Passo 5: Falha na restauração do sistema."})

    # Passo 6: Verificação de vulnerabilidades
    print(f"\n[PASSO 6/{total_steps}] - Verificação de Vulnerabilidades (71% concluído)")
    print("Instrução: Verifique se há vulnerabilidades que permitiram a infecção pelo Xworm.")
    response = input("Vulnerabilidades identificadas e corrigidas? (S/N): ").upper()
    while response not in ('S', 'N'):
        response = input("Resposta inválida. Por favor, digite S ou N: ").upper()
    if response == 'S':
        report_content.append({"status": "success", "message": "Passo 6: Vulnerabilidades corrigidas com sucesso."})
    else:
        report_content.append({"status": "failure", "message": "Passo 6: Falha na identificação/correção de vulnerabilidades."})

    # Passo 7: Monitoramento
    print(f"\n[PASSO 7/{total_steps}] - Monitoramento (86% concluído)")
    print("Instrução: Monitore o sistema para garantir que a ameaça foi completamente eliminada.")
    response = input("Monitoramento concluído e sistema limpo? (S/N): ").upper()
    while response not in ('S', 'N'):
        response = input("Resposta inválida. Por favor, digite S ou N: ").upper()
    if response == 'S':
        report_content.append({"status": "success", "message": "Passo 7: Monitoramento concluído e sistema limpo."})
    else:
        report_content.append({"status": "failure", "message": "Passo 7: Falha no monitoramento."})

    # Validação de Falso Positivo (Exemplo)
    response = input("\nSuspeita de falso positivo? (S/N): ").upper()
    while response not in ('S', 'N'):
        response = input("Resposta inválida. Por favor, digite S ou N: ").upper()
    if response == 'S':
        return end_menu(report_content, 'xworm', 'XWorm - Ameaça de Vírus')


    return end_menu(report_content, 'xworm', 'XWorm - Ameaça de Vírus')