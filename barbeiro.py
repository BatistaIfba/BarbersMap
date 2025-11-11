from menu import menu_barbeiro, menu_sac
from banco import BARBEIROS, salvar_barbeiro
import os

def fluxo_barbeiro(cpf):
    opc = 0
    while opc != 7:
        opc = menu_barbeiro()
        if opc == 1:
            info_profissional(cpf)
        elif opc == 2:
            gerenciar_servicos(cpf)
        elif opc == 3:
            listar_agendamentos(cpf)
        elif opc == 4:
            visualizar_historico(cpf)
        elif opc == 5:
            print("Trabalho em andamento")
        elif opc == 6:
            menu_sac()
        elif opc == 7:
            print("Até logo!")
        else:
            print("opção inválida!")


def info_profissional(cpf):
    os.system('cls') 
    print("=============================")
    print("|        Barber´sMap        |")
    print("| Informações Profissionais |")
    print("=============================")
    print(f"Nome: {BARBEIROS[cpf]["nome"]}")
    print(f"Email: {BARBEIROS[cpf]["email"]}")
    print(f"Endereço: {BARBEIROS[cpf]["endereco"]}")
    print(f"Sobre: {BARBEIROS[cpf]["sobre"]}")
    print("\n1 - Editar informações")
    print("2 - Voltar")
    opc = int(input("Digite uma opção: "))
    while opc != 2 :
        if opc == 1:
            nome = input("Informe seu novo nome: ")
            email = input("Informe seu novo email: ")
            endereco = input("Informe seu novo endereço: ")
            sobre = input("Informe seu novo texto pessoal: ")
            BARBEIROS[cpf]["nome"] = nome
            BARBEIROS[cpf]["email"] = email
            BARBEIROS[cpf]["endereco"] = endereco
            BARBEIROS[cpf]["sobre"] = sobre
            salvar_barbeiro()
            break
        else:
            print("OPÇÂO INVALIDA!")
            opc = int(input("Digite uma opção: "))



def gerenciar_servicos(cpf):
    os.system("cls")
    print("=============================")
    print("|        Barber´sMap        |")
    print("|     Painel de Serviços    |")
    print("=============================")
    servicos = BARBEIROS[cpf]["servicos"]
    if len(servicos)==0 :
        print("\nNenhum serviço cadastrado ainda.")
    else:
        for i, s in enumerate(servicos, start=1):
            print(f"{i}. {s['nome']} - R${s['valor']:.2f} | Tempo: {s['tempo']} min")

    print("\n1 - Adiconar serviço")
    print("2 - Editar serviço")
    print("3 - Apagar serviço")
    print("4 - Voltar")
    opc = int(input("Digite uma opção: "))
    while opc != 4: 
        if opc == 1:
            nome = input("Nome do serviço: ")
            valor = float(input("Valor (R$): "))
            tempo = int(input("Tempo estimado (min): "))
            novo_servico = {"nome": nome, "valor": valor, "tempo": tempo}
            BARBEIROS[cpf]["servicos"].append(novo_servico)
            salvar_barbeiro()
            print(f"Serviço '{nome}' adicionado com sucesso!")
            break
        elif opc == 2:
            print("Trabalho em andamento")
            #CRIAR CASO DE USO EDITAR INFORMAÇAO DE SERVIÇOS
            break
        elif opc == 3:
            print("Trabalho em andamento!!!")
            #CRIAR CASO DE USO APAGAR SERVIÇO
        else:
            print("OPÇÂO INVÁLIDA!")
            opc = int(input("Digite uma opção: "))

def listar_agendamentos(cpf):
    os.system("cls")
    print("=============================")
    print("|        Barber´sMap        |")
    print("|        Agendamentos       |")
    print("=============================")
    agendamentos = BARBEIROS[cpf]["agendamentos"]
    if len(agendamentos)==0:
        print("\nNenhum agendamento ativo.")
    else:
        for a in agendamentos:
            print(f"Cliente: {a['cliente']} | CPF: {a['cpf']} | Serviço: {a['servico']} | Data: {a['data']}")
    print("\n1 - Cancelar agendamento")
    print("2 - Voltar")
    opc = int(input("Digite uma opção: "))
    while opc != 2:
        if opc == 1:
            print("TRABALHO EM ANDAMENTO...")
            #CRIAR CASO DE USO CANCELAR AGENDAMENTO!!!!
            break
        else:
            print("OPÇÂO INVÁLIDA!")
            opc = int(input("Digite uma opção: "))


def visualizar_historico(cpf):
    os.system("cls")
    print("=============================")
    print("|        Barber´sMap        |")
    print("|         Histórico         |")
    print("=============================")
    historico = BARBEIROS[cpf]["historico"]
    if len(historico)==0:
        print("\nNenhum serviço realizado ainda.")
    else:
        for h in historico:
            cont = 1
            print(f"{cont}° - Cliente: {h['cliente']} | Serviço: {h['servico']} | Valor: R${h['valor']:.2f} | Data: {h['data']}")
            cont += 1
    print("\n1 - Voltar")
    opc = int(input("Digite uma opção: "))
    while opc != 1:
        print("OPÇÂO INVÁLIDA!")
        opc = int(input("Digite uma opção: "))