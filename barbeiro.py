from menu import menu_barbeiro, menu_sac

def fluxo_barbeiro():
    opc = 0
    while opc != 7:
        opc = menu_barbeiro()
        if opc == 1:
            print("Trabalho em andamento")
        elif opc == 2:
            print("Trabalho em andamento")
        elif opc == 3:
            print("Trabalho em andamento")
        elif opc == 4:
            print("Trabalho em andamento")
        elif opc == 5:
            print("Trabalho em andamento")
        elif opc == 6:
            menu_sac()
        elif opc == 7:
            print("Até logo!")
        else:
            print("opção inválida!")
