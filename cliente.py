from menu import menu_cliente, menu_sac, menu_info_cliente
from banco import CLIENTES, BARBEIROS, salvar_cliente  
import os
import time

def fluxo_cliente(cpf):
    opc = 0
    while opc != 6:
        opc = menu_cliente()
        if opc == 1:
            print("Trabalho em andamento")
        elif opc == 2:
            menu_info_cliente(cpf)
        elif opc == 3:
            agendamentos_cliente(cpf)
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

def agendamentos_cliente(cpf):
    os.system('cls') 
    print("=============================")
    print("|        Barber´sMap        |")
    print("|        Agendamentos       |")
    print("=============================")
    for i in range(len(CLIENTES[cpf]["agendamentos"])):
        print(f"{i+1}° Agendamento:")
        print(f"Serviço: {CLIENTES[cpf]["agendamentos"][i]["servico"]}")
        print(f"Barbeiro: {CLIENTES[cpf]["agendamentos"][i]["barbeiro"]}")
        print(f"Valor: R${CLIENTES[cpf]["agendamentos"][i]["valor"]}  -  Data: {CLIENTES[cpf]["agendamentos"][i]["data"]}\n")
    if len(CLIENTES[cpf]["agendamentos"]) == 0:
        print("NENHUM AGENDAMENTO MARCADO!")
        print("1 - Voltar")
        opc = int(input("Digite uma opção: "))
        while opc != 1:
            print("Opção inválida!")
            opc = int(input("Digite uma opção: "))
    else:
        print("1 - Cancelar agendamento")
        print("2 - Voltar")
        opc = int(input("Digite uma opção: "))
        while opc>2 or opc<1:
            print("Opção inválida!")
            opc = int(input("Digite uma opção: "))
        if opc == 1:
            servico = input("Informe o nome do serviço que deseja cancelar o agendamento: ")
            for i in range(len(CLIENTES[cpf]["agendamentos"])):
                if servico.lower().strip() == CLIENTES[cpf]["agendamentos"][i]["servico"].lower().strip():
                    for I in range(len(BARBEIROS[CLIENTES[cpf]["agendamentos"][i]["cpf"]]["agendamentos"])):
                        if cpf == BARBEIROS[CLIENTES[cpf]["agendamentos"][i]["cpf"]]["agendamentos"][I]["cpf"]:
                            del BARBEIROS[CLIENTES[cpf]["agendamentos"][i]["cpf"]]["agendamentos"][I]
                            del CLIENTES[cpf]["agendamentos"][i]
                    print("Agendamento cancelado!")
                    time.sleep(2)
                    break

        

        