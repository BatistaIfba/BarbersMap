from menu import menu_cliente, menu_sac, menu_info_cliente
from banco import CLIENTES, salvar_cliente  

def fluxo_cliente(cpf):
    opc = 0
    while opc != 6:
        opc = menu_cliente()
        if opc == 1:
            print("Trabalho em andamento")
        elif opc == 2:
            menu_info_cliente(cpf)
        elif opc == 3:
            print("Trabalho em andamento")
        elif opc == 4:
            print("Trabalho em andamento")
        elif opc == 5:
            menu_sac()
        elif opc == 6:
            print("Até logo!")
        else:
            print("Opção inválida!")



#Adicionar melhorias de controle de senha e email!
def editar_informacoes(cpf):
    nome = input("Informe seu novo nome: ")
    email = input("Informe seu novo email: ")
    senha = input("informe sua nova senha: ")
    CLIENTES[cpf]["nome"] = nome
    CLIENTES[cpf]["email"] = email
    CLIENTES[cpf]["senha"] = senha
    print("Informações alteradas com sucesso!")
    salvar_cliente()
