from banco import CLIENTES, BARBEIROS


def cadastrar_usuario(nome, email, cpf, senha, tipo_usuario):
    email = email.lower()
    if cpf in CLIENTES or cpf in BARBEIROS: 
        print("Usuário já cadastrado!")
        return False
    if len(senha) < 8:
        print("Senha muito curta! Use pelo menos 8 caracteres!")
        return False
    if not len(cpf) == 11:
        print("Número de cpf inválido!")
        return False

    if tipo_usuario == "cliente":
        CLIENTES[cpf] = {"nome": nome.strip(), "senha": senha, "email": email}
    else: 
        BARBEIROS[cpf] = {"nome": nome.strip(), "senha": senha, "email": email}
    print("Cadastro realizado com sucesso!")
    return True

def login(cpf, email, senha):
    email = email.lower()    
    if cpf in CLIENTES:
        usuario = CLIENTES[cpf]
    elif cpf in BARBEIROS:
        usuario = BARBEIROS[cpf]
    else:
        print("Falha no login! Seu email, senha ou cpf podem estar incorretos, verifique suas informações e tente novamente!")
        return False
    
    if usuario and usuario["senha"] == senha and usuario["email"] == email:
        print("Login realizado com sucesso!")
        return True
    else: 
        print("Falha no login! Seu email, senha ou cpf podem estar incorretos, verifique suas informações e tente novamente!")
        return False

def fluxo_cadastrar():
    print("=============================")
    print("       Crie sua conta!       ")
    print("=============================")
    nome = input("Nome: ").strip()
    email = input("Email: ").strip()
    cpf = input("CPF: ").strip()
    senha = input("Senha: ").strip()
    tipo_usuario = input("Deseja ofertar serviços na plataforma? [S/N] ").strip().lower()
    if tipo_usuario == "s":
        tipo_usuario = "barbeiro"
    else:
        tipo_usuario = "cliente"
    cadastrar_usuario(nome, email, cpf, senha, tipo_usuario)
    
def fluxo_login():
    print("=============================")
    print("            Login            ")
    print("=============================")
    cpf = input("CPF: ").strip()
    email = input("Email: ").strip()
    senha = input("Senha: ").strip()
    login(cpf, email, senha)