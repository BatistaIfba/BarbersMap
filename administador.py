from menu import Menu_administrador
from AdministradorGerarRelatorios import fluxo_GerarRelatórios
from AdministradorGerenciarUsuarios import fluxo_gerenciar_usuarios

def fluxo_administrador():
    opc = 0

    while opc != 4:
        opc = Menu_administrador()

        if opc == 1:
            return fluxo_GerarRelatórios()
        elif opc == 2:
            return fluxo_gerenciar_usuarios()
        elif opc == 3:
            print("Trabalho em andamento")
        elif opc == 4:
            print("Até logo!")
        else:
            print("opção inválida!")