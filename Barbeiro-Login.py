import re

# "Banco de dados" dos barbeiros
BARBEIROS = {}

class Barbeiro:
    def __init__(self, nome, email, plano):
        self.nome = nome

        # Valida email: local@dominio.ext
        if not re.match(r"^[^@]+@[^@]+\.[^@]+$", email.strip()):
            raise ValueError("Email inválido. Use formato local@dominio.ext")

        email_normalizado = email.strip().lower()

        # Verifica se já está cadastrado (usando email normalizado)
        if email_normalizado in BARBEIROS:
            print(f"Aviso: Email '{email_normalizado}' já estava cadastrado! (será reutilizado)")
        else:
            BARBEIROS[email_normalizado] = {"nome": nome, "plano": plano}

        self.email = email_normalizado

        self.lista_planos = ["basic", "premium", "pro"]
        if plano in self.lista_planos:
            self.plano = plano
            BARBEIROS[self.email]["plano"] = plano
        else:
            raise ValueError("Plano inválido")

    def mudar_plano(self, novo_plano):
        if novo_plano in self.lista_planos:
            self.plano = novo_plano
            BARBEIROS[self.email]["plano"] = novo_plano
            print(f"Plano do barbeiro {self.nome} alterado para {novo_plano}.")
        else:
            print("Plano inválido")


# "Banco de dados" de serviços
SERVICOS = {}

class Servico:
    def __init__(self, nome_corte, tempo, valor):
        self.nome_corte = nome_corte
        self.tempo = tempo
        self.valor = valor

        SERVICOS[self.nome_corte] = {
            "tempo": self.tempo,
            "valor": self.valor
        }

    def __repr__(self):
        return f"<Servico: {self.nome_corte}, {self.tempo}, {self.valor}>"


# -------------------
# INTERAÇÃO NO TERMINAL
# -------------------
if __name__ == "__main__":
    print("=== Cadastro de Barbeiro ===")
    nome_barbeiro = input("Digite seu nome: ")
    email_barbeiro = input("Digite seu email: ")
    plano_barbeiro = input("Escolha seu plano (basic, premium, pro): ")

    try:
        barbeiro = Barbeiro(nome_barbeiro, email_barbeiro, plano_barbeiro)
        print("\nBarbeiro cadastrado com sucesso!")
        print("Nome:", barbeiro.nome)
        print("Email:", barbeiro.email)
        print("Plano:", barbeiro.plano)
    except ValueError as e:
        print("Erro:", e)


    print("\n=== Cadastro de Serviços ===")
    while True:
        nome_corte = input("Nome do corte (ou ENTER para encerrar): ")
        if nome_corte.strip() == "":
            break
        tempo = input("Tempo do corte: ")
        valor = input("Valor do corte R$: ")
        servico = Servico(nome_corte, tempo, valor)
        print(f"Serviço '{nome_corte}' cadastrado com sucesso!\n")

    # Mostra resultados finais
    print("\n--- Barbeiros cadastrados ---")
    for email, dados in BARBEIROS.items():
        print(f"{dados['nome']} - {email} - Plano: {dados['plano']}")

    print("\n--- Serviços cadastrados ---")
    for nome, dados in SERVICOS.items():
        print(f"{nome}: tempo {dados['tempo']} - valor {dados['valor']}")
