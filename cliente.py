from menu import menu_cliente, menu_sac


def fluxo_cliente():
    opc = 0

    while opc != 6:
        opc = menu_cliente()

        if opc == 1:
            print("Trabalho em andamento")
        elif opc == 2:
            print("Trabalho em andamento")
        elif opc == 3:
            print("Trabalho em andamento")
        elif opc == 4:
            print("Trabalho em andamento")
        elif opc == 5:
            menu_sac()
        elif opc == 6:
            print("Até logo!")
        else:
            print("opção inválida!")