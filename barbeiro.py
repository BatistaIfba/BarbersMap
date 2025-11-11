from menu import menu_barbeiro, menu_sac
from funçoesbarbeiro import info_profissional, gerenciar_servicos, listar_agendamentos, visualizar_historico
def fluxo_barbeiro(cpf):
    opc = 0
    while opc != 7:
        opc = menu_barbeiro()
        if opc == 1:
            info_profissional()
        elif opc == 2:
            gerenciar_servicos()
        elif opc == 3:
            listar_agendamentos()
        elif opc == 4:
            visualizar_historico()
        elif opc == 5:
            print("Trabalho em andamento")
        elif opc == 6:
            menu_sac()
        elif opc == 7:
            print("Até logo!")
        else:
            print("opção inválida!")
