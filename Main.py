from cadastroElogin import cadastrar_usuario, fluxo_cadastrar, fluxo_login
from banco import BARBEIROS, CLIENTES 
from menu import menu

def main():
    opc = 0

    while opc != 5:
        opc = menu()

        if opc == 1:
            print("Trabalho em andamento!")
        elif opc == 2:
            fluxo_login()
        elif opc == 3:
            fluxo_cadastrar()
        elif opc == 4: 
            print("Trabalho em andamento!")
        elif opc == 5:
            print("Adeus!")
        else:
            print("Opção inválida!")

main()
