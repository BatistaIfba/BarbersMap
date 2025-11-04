from banco import BARBEIROS, ADMINISTRADORES, CLIENTES, salvar_barbeiro, salvar_cliente, salvar_admin
from administador import Menu_administrador

def listar_usuarios():
   print("\n=== Lista de Usuários ===")

   print("\nAdministradores:")
   for cpf, admin_data in ADMINISTRADORES.items():
      print(f"cpf: {cpf} | nome: {admin_data['nome']} | email: {admin_data['email']} | senha: {admin_data['senha']}")
     
   print("\nBarbeiros:")
   for cpf, barbeiros_data in BARBEIROS.items():
      print(f"cpf: {cpf} | nome: {barbeiros_data['nome']} | email: {barbeiros_data['email']} | senha: {barbeiros_data['senha']}")

   print("\nclientes:")
   for cpf, clientes_data in CLIENTES.items():
      print(f"cpf: {cpf} | nome: {clientes_data['nome']} | email: {clientes_data['email']} | senha: {clientes_data['senha']}")


def deletar_usuarios():
   listar_usuarios()
   usuario = input("informe o cpf do usuario que deseja deletar:")
   if  usuario in ADMINISTRADORES:
      del ADMINISTRADORES[usuario]
      print(f"Usuário Barbeiro com CPF {usuario} deletado com sucesso!")
      return True
   elif usuario in BARBEIROS:
        del BARBEIROS[usuario]
        print(f"Usuário Barbeiro com CPF {usuario} deletado com sucesso!")
        return True
   elif usuario in CLIENTES:
        del CLIENTES[usuario]
        print(f"Usuário Cliente com CPF {usuario} deletado com sucesso!")
        salvar_barbeiro()
        salvar_cliente()
        listar_usuarios()
        return True

  
   else:
      print('O cpf informado não está cadastrado')
      return False

def cadastrar_usuario_administrador(nome, email, cpf, senha, tipo_usuario):
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
        CLIENTES[cpf] = {"nome": nome.strip(), "senha": senha, "email": email, "tipo_usuario": tipo_usuario}
        print("Cadastro realizado com sucesso!")
        salvar_cliente()
    elif tipo_usuario == "barbeiro": 
        BARBEIROS[cpf] = {"nome": nome.strip(), "senha": senha, "email": email, "tipo_usuario": tipo_usuario, "endereco": input("Informe o endereço do seu local de trabalho: ") , "sobre": input("Escreva um breve resumo sobre você: ")}
        print("Cadastro realizado com sucesso!")
        salvar_barbeiro()
    elif tipo_usuario == "administrador":
        ADMINISTRADORES[cpf] = {"nome": nome.strip(), "senha": senha, "email": email, "tipo_usuario": tipo_usuario} 
        print("Cadastro realizado com sucesso!")
        salvar_admin()
         
    
def fluxo_cadastrar_administrador():
    print("=============================")
    print("       Cadastre um usuário   ")
    print("=============================")
    nome = input("Nome: ").strip()
    email = input("Email: ").strip()
    cpf = input("CPF: ").strip()
    senha = input("Senha: ").strip()
    tipo_usuario = input("informe o tipo do usuário(cliente, barbeiro, administrador):").strip().lower()
    
    if tipo_usuario in ["cliente", "barbeiro", "administrador"]:
        cadastrar_usuario_administrador(nome, email, cpf, senha, tipo_usuario)
    else:
        print("Tipo de usuário inválido! Use 'cliente', 'barbeiro' ou 'administrador'")
        return
    
def menu_gerenciar_usuarios():
    print("====Gerenciar usuários====")
    print("1 - Listar todos os usuários")
    print("2 - deletar usuário")
    print("3 - cadastrar usuario ")
    print("4 - voltar")


    try:
        entrada = input("digite um opção: ").strip() 
        opc = int(entrada)
        return opc
    except ValueError:
        print("Opção inválida! Digite um número.")
        return 0


def fluxo_gerenciar_usuarios():
    opc = 0

    while opc != 4:  
        opc = menu_gerenciar_usuarios()

        if opc == 1:
            listar_usuarios()
        elif opc == 2:
            deletar_usuarios()
        elif opc == 3:
            fluxo_cadastrar_administrador()
        elif opc == 4:
            print("Voltando ao menu anterior...")
            return  
        else:
            print("opção inválida!")




