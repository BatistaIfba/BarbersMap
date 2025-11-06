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
            historico_cliente(cpf)
        elif opc == 5:
            menu_sac()
        elif opc == 6:
            print("Até logo!")
        else:
            print("Opção inválida!")



#Adicionar melhorias de controle de senha e email!
def editar_informacoes(cpf):
    print(f"\n\n{BARBEIROS}\n\n")
    nome = input("Informe seu novo nome: ")
    email = input("Informe seu novo email: ")
    senha = input("informe sua nova senha: ")
    CLIENTES[cpf]["nome"] = nome
    CLIENTES[cpf]["email"] = email
    CLIENTES[cpf]["senha"] = senha
    for chave in BARBEIROS:
        for I in range(len(BARBEIROS[chave]["agendamentos"])):
            if BARBEIROS[chave]["agendamentos"][I]["cpf"] == cpf:
                BARBEIROS[chave]["agendamentos"][I]["cliente"] = nome
        for i in range(len(BARBEIROS[chave]["historico"])):
            if BARBEIROS[chave]["historico"][i]["cpf"] == cpf:
                BARBEIROS[chave]["historico"][i]["cliente"] = nome
    print("Informações alteradas com sucesso!")
    print(f"\n\n{BARBEIROS}\n\n")
    time.sleep(10)
    #salvar_cliente()

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
        print("2 - Concluir agendamento")
        print("3 - Voltar")
        opc = int(input("Digite uma opção: "))
        while opc>3 or opc<1:
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
                            #salvar_cliente()
                            #salvar_barbeiro()
                            time.sleep(2)
                            break
                else:
                    print("Serviço não encontrado!")
        elif opc == 2:
            servico = input("Informe o nome do serviço que deseja confirmar a realização: ")
            for i in range(len(CLIENTES[cpf]["agendamentos"])):
                if servico.lower().strip() == CLIENTES[cpf]["agendamentos"][i]["servico"].lower().strip():
                    for I in range(len(BARBEIROS[CLIENTES[cpf]["agendamentos"][i]["cpf"]]["agendamentos"])):
                        if cpf == BARBEIROS[CLIENTES[cpf]["agendamentos"][i]["cpf"]]["agendamentos"][I]["cpf"]:
                            CLIENTES[cpf]["historico"].append(CLIENTES[cpf]["agendamentos"][i])
                            BARBEIROS[CLIENTES[cpf]["agendamentos"][i]["cpf"]]["historico"].append(BARBEIROS[CLIENTES[cpf]["agendamentos"][i]["cpf"]]["agendamentos"][I])
                            del BARBEIROS[CLIENTES[cpf]["agendamentos"][i]["cpf"]]["agendamentos"][I]
                            del CLIENTES[cpf]["agendamentos"][i]
                            nota = float(input("De uma nota para o serviço [0 a 5]: "))
                            while nota>5 or nota<0:
                                print("A nota tem que ser entre 0 e 5!")
                                nota = float(input("De uma nota para o serviço [0 a 5]: "))
                            for P in range(len(BARBEIROS[CLIENTES[cpf]["historico"][i]["cpf"]]["servicos"])):
                                if BARBEIROS[CLIENTES[cpf]["historico"][i]["cpf"]]["servicos"][i]["nome"] == CLIENTES[cpf]["historico"][len(CLIENTES[cpf]["historico"])-1]["servico"]:
                                    BARBEIROS[CLIENTES[cpf]["historico"][i]["cpf"]]["servicos"][i]["avaliacao"].append(nota)
                            print("Agendamento concluido! Muito obrigado!")
                            #salvar_cliente()
                            #salvar_barbeiro()
                            time.sleep(2)
                            break
                    else:
                        print("Serviço não encontrado!")

def historico_cliente(cpf):
    os.system('cls') 
    print("=============================")
    print("|        Barber´sMap        |")
    print("|         Histórico         |")
    print("=============================")
    for i in range(len(CLIENTES[cpf]["historico"])):
        print(f"Serviço concluido N{i+1}°:")
        print(f"Serviço: {CLIENTES[cpf]["historico"][i]["servico"]}")
        print(f"Barbeiro: {CLIENTES[cpf]["historico"][i]["barbeiro"]}")
        print(f"Valor: R${CLIENTES[cpf]["historico"][i]["valor"]}  -  Data: {CLIENTES[cpf]["historico"][i]["data"]}\n")
    if len(CLIENTES[cpf]["historico"]) == 0:
        print("Histórico vazio!\n")
    print("1 - Voltar")
    opc = int(input("Digite uma opção: "))
    while opc != 1:
        print("Opção inválida!")
        opc = int(input("Digite uma opção: "))