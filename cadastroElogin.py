from banco import CLIENTES, BARBEIROS, ADMINISTRADORES
from menu import menu_cliente, menu_barbeiro
from cliente import fluxo_cliente
from barbeiro import fluxo_barbeiro
from administador import fluxo_administrador


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

    print("Cadastro realizado com sucesso!")
    if tipo_usuario == "cliente":
        CLIENTES[cpf] = {"nome": nome.strip(), "senha": senha, "email": email, "tipo_usuario": tipo_usuario}
        return fluxo_cliente()
    else: 
        BARBEIROS[cpf] = {"nome": nome.strip(), "senha": senha, "email": email, "tipo_usuario": tipo_usuario}
        return fluxo_barbeiro()

def login(cpf, email, senha):
    email = email.lower()    
    if cpf in CLIENTES:
        usuario = CLIENTES[cpf]
    elif cpf in BARBEIROS:
        usuario = BARBEIROS[cpf]
    elif cpf in ADMINISTRADORES[cpf]:
        usuario = ADMINISTRADORES[cpf]

    else:
        print("Falha no login! Seu email, senha ou cpf podem estar incorretos, verifique suas informações e tente novamente!")
        return False
    
    if usuario and usuario["senha"] == senha and usuario["email"] == email:
        print("Login realizado com sucesso!")
        if usuario["tipo_usuario"] == "cliente":
            return fluxo_cliente()
        elif usuario["tipo_usuario"] == "barbeiro":
            return fluxo_barbeiro()
        elif usuario["tipo_usuario"] == "administrador":
            return fluxo_administrador()
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