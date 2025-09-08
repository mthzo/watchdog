from core.menu import end_menu

def run():
    print("Iniciando Runbook: Resposta a Phishing e Análise de Anexo Malicioso")
    print("------------------------------------------------------------------")
    report_content = []
    
    # Passo 1
    print("\n[PASSO 1/7] - Análise de Alerta (14% concluído)")
    print("Ameaça identificada: E-mail de phishing com anexo potencialmente malicioso.")
    report_content.append({"status": "success", "message": "Passo 1: Alerta de e-mail de phishing analisado. Risco confirmado."})
    input("Pressione Enter para iniciar a investigação...")

    # Passo 2
    print("\n[PASSO 2/7] - Verificação de Conteúdo (28% concluído)")
    print("Instrução: Verifique os detalhes do e-mail, como remetente, assunto e o hash do anexo.")
    response = input("O anexo corresponde a um hash conhecido de malware? (S/N): ").upper()
    while response not in ('S', 'N'):
        response = input("Resposta inválida. Por favor, digite S ou N: ").upper()
    if response == 'S':
        print("Instrução: Siga o protocolo para risco elevado. O hash do anexo foi confirmado como malicioso.")
        report_content.append({"status": "success", "message": "Passo 2: Anexo confirmado como malicioso (hash correspondente a malware conhecido)."})
    else:
        print("Instrução: Anexo não encontrado na base de indicadores. Prossiga com cautela.")
        report_content.append({"status": "failure", "message": "Passo 2: Anexo não corresponde a um hash conhecido. Risco de malware 'dia zero' ou ofuscado."})

    # Passo 3
    print("\n[PASSO 3/7] - Avaliação de Impacto (42% concluído)")
    print("Instrução: Determine se o usuário abriu o e-mail ou executou o anexo.")
    response = input("O usuário abriu o e-mail e/ou executou o anexo? (S/N): ").upper()
    while response not in ('S', 'N'):
        response = input("Resposta inválida. Por favor, digite S ou N: ").upper()
    if response == 'S':
        print("Risco de comprometimento do endpoint. Ação de contenção recomendada.")
        report_content.append({"status": "success", "message": "Passo 3: Ação do usuário comprometeu o endpoint. Iniciando contenção."})
    else:
        print("Risco mitigado. Ação de contenção não necessária neste momento.")
        report_content.append({"status": "success", "message": "Passo 3: Anexo não executado. Risco contido."})

    # Passo 4
    print("\n[PASSO 4/7] - Contenção (56% concluído)")
    print("Instrução: Isolar a máquina do usuário da rede. Confirme se a ação foi bem-sucedida.")
    response = input("A máquina do usuário foi isolada da rede? (S/N): ").upper()
    while response not in ('S', 'N'):
        response = input("Resposta inválida. Por favor, digite S ou N: ").upper()
    if response == 'S':
        print("Confirmação: A máquina está isolada. Previnindo movimentação lateral do atacante.")
        report_content.append({"status": "success", "message": "Passo 4: Contenção realizada. Máquina isolada com sucesso."})
    else:
        print("Alerta: Falha na contenção. Notifique a equipe de segurança de rede para isolamento manual.")
        report_content.append({"status": "failure", "message": "Passo 4: Falha na contenção. Necessário isolamento manual pela equipe de rede."})

    # Passo 5
    print("\n[PASSO 5/7] - Erradicação (70% concluído)")
    print("Instrução: Remova o e-mail e o anexo malicioso da caixa de entrada do usuário e do servidor.")
    response = input("O e-mail e o anexo malicioso foram removidos? (S/N): ").upper()
    while response not in ('S', 'N'):
        response = input("Resposta inválida. Por favor, digite S ou N: ").upper()
    if response == 'S':
        print("Confirmação: E-mail e anexo removidos. Execute uma varredura completa.")
        report_content.append({"status": "success", "message": "Passo 5: Erradicação concluída. E-mail e anexo removidos."})
    else:
        print("Alerta: Falha na erradicação. Tentar remover o e-mail manualmente.")
        report_content.append({"status": "failure", "message": "Passo 5: Falha na erradicação. Necessário remoção manual do e-mail."})

    # Passo 6
    print("\n[PASSO 6/7] - Recuperação (85% concluído)")
    print("Instrução: Restaure a máquina do usuário para um estado seguro. Reinstale o sistema ou softwares, se necessário.")
    response = input("A recuperação foi bem-sucedida e a máquina está de volta à rede? (S/N): ").upper()
    while response not in ('S', 'N'):
        response = input("Resposta inválida. Por favor, digite S ou N: ").upper()
    if response == 'S':
        print("Confirmação: Máquina recuperada e reinserida na rede.")
        report_content.append({"status": "success", "message": "Passo 6: Recuperação concluída. Máquina reintegrada à rede."})
    else:
        print("Alerta: Falha na recuperação. A máquina permanece isolada para investigação adicional.")
        report_content.append({"status": "failure", "message": "Passo 6: Falha na recuperação. Máquina permanece isolada."})

    # Passo 7
    print("\n[PASSO 7/7] - Lições Aprendidas e Pós-Incidente (100% concluído)")
    print("Instrução: Reúna informações para o relatório final. Crie novos alertas e assinaturas para prevenir futuros incidentes.")
    report_content.append({"status": "success", "message": "Passo 7: Pós-incidente. Lições aprendidas documentadas. Prevenção aprimorada."})
    
    return end_menu(report_content, "phishing", "Resposta a Phishing e Análise de Anexo Malicioso")