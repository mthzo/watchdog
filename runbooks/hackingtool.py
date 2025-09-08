from core.menu import end_menu

def run():
    print("Iniciando Runbook: Uso de Ferramentas de Hacking em Endpoint")
    print("------------------------------------------------------------")
    report_content = []

    # Passo 1
    print("\n[PASSO 1/6] - Análise de Alerta (16% concluído)")
    print("Alerta identificado: Uso de ferramenta de hacking em um endpoint.")
    report_content.append({"status": "success", "message": "Passo 1: Alerta de uso de ferramenta de hacking em endpoint recebido."})
    input("Pressione Enter para iniciar a investigação...")

    # Passo 2
    print("\n[PASSO 2/6] - Investigação e Validação (32% concluído)")
    print("Instrução: Analise o processo, o usuário e o contexto para determinar a legitimidade da ação.")
    response = input("A atividade do usuário foi validada e autorizada pela equipe de TI? (S/N): ").upper()
    while response not in ('S', 'N'):
        response = input("Resposta inválida. Por favor, digite S ou N: ").upper()
    if response == 'S':
        print("Confirmação: Atividade autorizada. Documente como um falso-positivo.")
        report_content.append({"status": "success", "message": "Passo 2: Atividade do usuário foi autorizada. Alerta classificado como falso-positivo."})
        return end_menu(report_content, "hackingtool", "Uso de Ferramentas de Hacking em Endpoint")
    else:
        print("Atividade não autorizada. Confirme o incidente. Prossiga para a contenção.")
        report_content.append({"status": "failure", "message": "Passo 2: Atividade não autorizada. Protocolo de resposta a incidentes acionado."})

    # Passo 3
    print("\n[PASSO 3/6] - Contenção (50% concluído)")
    print("Instrução: Isole o host da rede para evitar a movimentação lateral do atacante.")
    response = input("O host foi isolado da rede? (S/N): ").upper()
    while response not in ('S', 'N'):
        response = input("Resposta inválida. Por favor, digite S ou N: ").upper()
    if response == 'S':
        print("Confirmação: Host isolado. Inicie a varredura e análise forense.")
        report_content.append({"status": "success", "message": "Passo 3: Contenção realizada. Host isolado com sucesso."})
    else:
        print("Alerta: Falha no isolamento. Notifique a equipe de segurança de rede para ação manual.")
        report_content.append({"status": "failure", "message": "Passo 3: Falha na contenção. Necessário isolamento manual."})

    # Passo 4
    print("\n[PASSO 4/6] - Erradicação (66% concluído)")
    print("Instrução: Remova a ferramenta de hacking e quaisquer artefatos maliciosos do sistema.")
    response = input("A ferramenta e artefatos maliciosos foram removidos do sistema? (S/N): ").upper()
    while response not in ('S', 'N'):
        response = input("Resposta inválida. Por favor, digite S ou N: ").upper()
    if response == 'S':
        print("Confirmação: Artefatos removidos. Execute uma varredura completa.")
        report_content.append({"status": "success", "message": "Passo 4: Erradicação concluída. Artefatos de hacking removidos."})
    else:
        print("Alerta: Falha na erradicação. Prossiga para a recuperação, que pode incluir a formatação da máquina.")
        report_content.append({"status": "failure", "message": "Passo 4: Falha na erradicação. Ação de recuperação mais drástica é necessária."})

    # Passo 5
    print("\n[PASSO 5/6] - Análise Forense (84% concluído)")
    print("Instrução: Analise logs, processos e memória para identificar o vetor de ataque inicial.")
    response = input("O vetor de ataque inicial foi identificado com sucesso? (S/N): ").upper()
    while response not in ('S', 'N'):
        response = input("Resposta inválida. Por favor, digite S ou N: ").upper()
    if response == 'S':
        print("Confirmação: Vetor de ataque identificado. Feche a vulnerabilidade para prevenir novos incidentes.")
        report_content.append({"status": "success", "message": "Passo 5: Vetor de ataque inicial identificado e vulnerabilidade corrigida."})
    else:
        print("Vetor de ataque não identificado. Reforce o monitoramento no endpoint e em outros sistemas.")
        report_content.append({"status": "failure", "message": "Passo 5: Vetor de ataque não identificado. Monitoramento e segurança reforçados."})

    # Passo 6
    print("\n[PASSO 6/6] - Recuperação e Pós-Incidente (100% concluído)")
    print("Instrução: Restaure a máquina do usuário. Documente o incidente e agende uma reunião para lições aprendidas.")
    print("Confirmação: O protocolo de recuperação foi concluído e as ações de pós-incidente foram iniciadas.")
    report_content.append({"status": "success", "message": "Passo 6: Recuperação completa. Análise de lições aprendidas em andamento."})

    return end_menu(report_content, "hackingtool", "Uso de Ferramentas de Hacking em Endpoint")