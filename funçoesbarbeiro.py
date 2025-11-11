from banco import carregar_barbeiro

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
        return

    print("\n--- SERVIÇOS CADASTRADOS ---")
    for i, s in enumerate(servicos, start=1):
        print(f"{i}. {s['nome']} - R${s['valor']:.2f} | Tempo: {s['tempo']} min")


def listar_agendamentos():
    barbeiros = carregar_barbeiro()
    barbeiro = barbeiros.get(CPF_BARBEIRO)

    if not barbeiro:
        print("Barbeiro não encontrado!")
        return

    agendamentos = barbeiro.get("agendamentos", [])
    if not agendamentos:
        print("\nNenhum agendamento ativo.")
        return
    print("\n--- AGENDAMENTOS ---")
    cpf = CPF_BARBEIRO
    for agendamento in barbeiros[cpf]["agendamentos"]:
        print(f"Cliente: {agendamento['cliente']} || CPF: {agendamento['cpf']} |Serviço: {agendamento['servico']} | Data: {agendamento['data']}")


def visualizar_historico():
    barbeiros = carregar_barbeiro()
    barbeiro = barbeiros.get(CPF_BARBEIRO)

    if not barbeiro:
        print("Barbeiro não encontrado!")
        return

    historico = barbeiro.get("historico", [])
    if not historico:
        print("\nNenhum serviço realizado ainda.")
        return

    print("\n--- HISTÓRICO DE SERVIÇOS ---")
    for h in historico:
        print(f"Cliente: {h['cliente']} | Serviço: {h['servico']} | "
              f"Valor: R${h['valor']:.2f} | Data: {h['data']}")