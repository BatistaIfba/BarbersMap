from cadastroElogin import cadastrar_usuario, fluxo_cadastrar, fluxo_login

#Banco de dados em memória
BARBEIROS = {}
CLIENTES = {}

def menu():
    print("=============================")
    print("|        Barber´sMap        |")
    print("|   Serviços de barbeiros   |")
    print("=============================")
    print("1 - Buscar serviços disponiveis")
    print("2 - Login")
    print("3 - Cadastrar-se")
    print("4 - Atendimento ao consumidor")
    print("5 - Sair")
    opc = int(input("Digite uma opção: "))
    return opc

def main():
    cadastrar_usuario("batista", "batista@gmail.com", "09291376558", "senhalonga", "n")

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
