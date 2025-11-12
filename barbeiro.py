from menu import menu_barbeiro, menu_sac
from banco import BARBEIROS, CLIENTES, salvar_barbeiro, salvar_cliente
import os
import time

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
            central_receita(cpf)
        elif opc == 6:
            menu_sac()
        elif opc == 7:
            print("Até logo!")
            time.sleep(2)
            os.system("cls")
        else:
            print("opção inválida!")

def info_profissional(cpf):
    os.system('cls') 
    medias = 0
    for i in range(len(BARBEIROS[cpf]["servicos"])):
        medias += sum(BARBEIROS[cpf]["servicos"][i]["avaliacao"])/len(BARBEIROS[cpf]["servicos"][i]["avaliacao"])
    media = medias/len(BARBEIROS[cpf]["servicos"])
    print("=============================")
    print("|        Barber´sMap        |")
    print("| Informações Profissionais |")
    print("=============================")
    print(f"Nome: {BARBEIROS[cpf]["nome"]}")
    print(f"Email: {BARBEIROS[cpf]["email"]}")
    print(f"Endereço: {BARBEIROS[cpf]["endereco"]}")
    print(f"Sobre: {BARBEIROS[cpf]["sobre"]}")
    print(f"Avaliação média: {media:.2f}")
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
            if len(s["avaliacao"]) == 0:
                media = 0
            else: 
                media = sum(s["avaliacao"])/len(s["avaliacao"])
            print(f"{i}. {s['nome']} - R${s['valor']:.2f} | Tempo: {s['tempo']} min | Avaliação média: {media:.2f}")
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
            novo_servico = {"nome": nome, "valor": valor, "tempo": tempo, "avaliacao": []}
            BARBEIROS[cpf]["servicos"].append(novo_servico)
            salvar_barbeiro()
            print(f"Serviço '{nome}' adicionado com sucesso!")
            break
        elif opc == 2:
            nome_servico = input("Digite o nome do serviço que deseja editar: ").lower()
            for i in range(len(BARBEIROS[cpf]["servicos"])):
                if nome_servico == BARBEIROS[cpf]["servicos"][i]["nome"].lower():
                    nome = input("Informe o novo nome do serviço: ")
                    valor = float(input("Informe o novo valor do serviço: R$"))
                    tempo = int(input("Informe o novo prazo de tempo serviço: "))
                    BARBEIROS[cpf]["servicos"][i]["nome"] = nome
                    BARBEIROS[cpf]["servicos"][i]["valor"] = valor
                    BARBEIROS[cpf]["servicos"][i]["tempo"] = tempo
                    cont = True
                    print("Serviço alterado!")
                    salvar_barbeiro()
                    break
            if cont != True:
                print("Serviço não encontrado no banco de dados!. Tente novamente.")
            break
        elif opc == 3:
            nome = input("Digite o nome do serviço que deseja parar de ofertar: ").lower()
            for i in range(len(BARBEIROS[cpf]["servicos"])):
                if nome == BARBEIROS[cpf]["servicos"][i]["nome"].lower():
                    del BARBEIROS[cpf]["servicos"][i]
                    salvar_barbeiro()
                    print("Serviço deletado!")
                    time.sleep(2.5)
                    cont = True
                    break
            if cont != True:
                print("Serviço não encontrado no banco de dados! Tente novamente.")
            break
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
            nome = input("Informe o nome do cliente que deseja cancelar o agendamento: ").lower()
            for i in range(len(BARBEIROS[cpf]["agendamentos"])):
                if nome == BARBEIROS[cpf]["agendamentos"][i]["cliente"].lower():
                    for I in range(len(CLIENTES[BARBEIROS[cpf]["agendamentos"][i]["cpf"]]["agendamentos"])):
                        if cpf == CLIENTES[BARBEIROS[cpf]["agendamentos"][i]["cpf"]]["agendamentos"][i]["cpf"]:
                            del CLIENTES[BARBEIROS[cpf]["agendamentos"][i]["cpf"]]["agendamentos"][i]
                            del BARBEIROS[cpf]["agendamentos"][i]
                            print("Agendamento cancelado!")
                            salvar_barbeiro()
                            salvar_cliente()
                            time.sleep(3)
                            break
                    break
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

def central_receita(cpf):
    os.system("cls")
    print("=============================")
    print("|        Barber´sMap        |")
    print("|     Central de Receita    |")
    print("=============================")
    print(f"Total de agendamentos concluidos: {len(BARBEIROS[cpf]["historico"])}")
    print(f"Total de agendamentos pendentes: {len(BARBEIROS[cpf]["agendamentos"])}")
    soma = 0
    for i in range(len(BARBEIROS[cpf]["historico"])):
        if len(BARBEIROS[cpf]["historico"]) == 0:
            break
        soma += BARBEIROS[cpf]["historico"][i]["valor"]
    print(f"Receita total: R${soma}")
    print(f"Valor médio por serviço: R${soma/len(BARBEIROS[cpf]["historico"])}")
    print("\n1 - Voltar")
    opc = int(input("Digite uma opção: "))
    while opc != 1:
        print("OPÇÂO INVÁLIDA!")
        opc = int(input("Digite uma opção: "))    