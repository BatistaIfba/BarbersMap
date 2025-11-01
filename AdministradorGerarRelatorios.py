from banco import  BARBEIROS

def gerar_relatorio_faturamento_total():
    faturamento = 0
    agendamentos_concluidos = 0
    
    for agendamento in AGENDAMENTOS:
        if agendamento['status'] == 'Concluido':
            faturamento += agendamento['valor']
            agendamentos_concluidos += 1

    return {
        "faturamento_total": faturamento,
        "total_servicos_concluidos": agendamentos_concluidos
    }

def gerar_relatorio_desempenho_barbeiro(nome_barbeiro):
    faturamento = 0
    agendamentos_concluidos = 0
    barbeiro_encontrado = False
    nome_barbeiro = nome_barbeiro.strip().lower()
    
    for agendamento in AGENDAMENTOS:
        if agendamento['barbeiro'].strip().lower() == nome_barbeiro:
           barbeiro_encontrado = True
           if agendamento['status'] == 'Concluido':
               faturamento += agendamento['valor']
               agendamentos_concluidos += 1
    
    if not barbeiro_encontrado:
        return('O barbeiro não existe.')
    
    if agendamentos_concluidos == 0:
        return('O barbeiro não possui agendamentos')
    

    return {  
        "nome_barbeiro": nome_barbeiro, 
        "faturamento_total": faturamento,
        "total_servicos_concluidos": agendamentos_concluidos
    }



    

         


               
               
               