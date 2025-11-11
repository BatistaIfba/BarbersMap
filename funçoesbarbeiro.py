from banco import carregar_barbeiro, salvar_barbeiro

CPF_BARBEIRO = "00000000000"
barbeiros = carregar_barbeiro()

def info_profissional():
    barbeiros = carregar_barbeiro()
    barbeiro = barbeiros.get(CPF_BARBEIRO)

    if not barbeiro:
        print("Barbeiro não encontrado!")
        return

    print("\n--- INFORMAÇÕES PROFISSIONAIS ---")
    print(f"Nome: {barbeiro.get('nome', 'Não informado')}")
    print(f"Email: {barbeiro.get('email', 'Não informado')}")
    print(f"Endereço: {barbeiro.get('endereco', 'Não informado')}")
    print(f"Sobre: {barbeiro.get('sobre', 'Sem descrição')}")
    print(f"Serviços cadastrados: {len(barbeiro.get('servicos', []))}")
    print(f"Agendamentos ativos: {len(barbeiro.get('agendamentos', []))}")
    print(f"Serviços realizados: {len(barbeiro.get('historico', []))}")


def gerenciar_servicos():
    barbeiros = carregar_barbeiro()
    barbeiro = barbeiros.get(CPF_BARBEIRO)

    if not barbeiro:
        print("Barbeiro não encontrado!")
        return

    servicos = barbeiro.get("servicos", [])
    if not servicos:
        print("\nNenhum serviço cadastrado ainda.")
    else:
        print("\n--- SERVIÇOS CADASTRADOS ---")
        for i, s in enumerate(servicos, start=1):
            print(f"{i}. {s['nome']} - R${s['valor']:.2f} | Tempo: {s['tempo']} min")

    opc = input("\nDeseja adicionar um novo serviço [s/n]? ").lower()
    if opc == "s":
        nome = input("Nome do serviço: ")
        valor = float(input("Valor (R$): "))
        tempo = int(input("Tempo estimado (min): "))

        novo_servico = {"nome": nome, "valor": valor, "tempo": tempo}
        barbeiro.setdefault("servicos", []).append(novo_servico)
        salvar_barbeiro()
        print(f"Serviço '{nome}' adicionado com sucesso!")


def listar_agendamentos():
    barbeiros = carregar_barbeiro()
    barbeiro = barbeiros.get(CPF_BARBEIRO)

    if not barbeiro:
        print("Barbeiro não encontrado!")
        return

    agendamentos = barbeiro.get("agendamentos", [])
    if not agendamentos:
        print("\nNenhum agendamento ativo.")
    else:
        print("\n--- AGENDAMENTOS ---")
        for a in agendamentos:
            print(f"Cliente: {a['cliente']} | CPF: {a['cpf']} | Serviço: {a['servico']} | Data: {a['data']}")


def visualizar_historico():
    barbeiros = carregar_barbeiro()
    barbeiro = barbeiros.get(CPF_BARBEIRO)

    if not barbeiro:
        print("Barbeiro não encontrado!")
        return

    historico = barbeiro.get("historico", [])
    if not historico:
        print("\nNenhum serviço realizado ainda.")
    else:
        print("\n--- HISTÓRICO DE SERVIÇOS ---")
        for h in historico:
            print(f"Cliente: {h['cliente']} | Serviço: {h['servico']} | Valor: R${h['valor']:.2f} | Data: {h['data']}")
