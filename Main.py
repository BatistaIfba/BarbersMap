from cadastroElogin import fluxo_cadastrar, fluxo_login
from menu import menu, menu_sac
import os


def main():
    os.system('cls') 
    opc = 0
    while opc != 5:
        opc = menu()
        if opc == 1:
            print("Trabalho em andamento!")
            break
        elif opc == 2:
            fluxo_login()
        elif opc == 3:
            fluxo_cadastrar()
        elif opc == 4: 
            menu_sac()
        elif opc == 5:
            print("Adeus!")
        else:
            print("Opção inválida!")

main()

