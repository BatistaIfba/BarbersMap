from menu import Menu_administrador
from banco import BARBEIROS, ADMINISTRADORES, CLIENTES, salvar_barbeiro, salvar_cliente, salvar_admin

def fluxo_administrador(cpf):
    opc = 0

    while opc != 4:
        opc = Menu_administrador()

        if opc == 1:
            print("Trabalho em andamento")
        elif opc == 2:
            return fluxo_gerenciar_usuarios(cpf)
        elif opc == 3:
            print("Trabalho em andamento")
        elif opc == 4:
            print("Até logo!")
        else:
            print("opção inválida!")

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

def fluxo_gerenciar_usuarios(cpf):
    print("====Gerenciar usuários====")

    listar_usuarios()
    opc = 0
    cpf = input('Informe o cpf do usuario que deseja gerenciar: ').strip()
    
    if cpf in CLIENTES:
        print("\nDados do usuário Cliente:")
        print(f"Nome: {CLIENTES[cpf]['nome']}")
        print(f"Email: {CLIENTES[cpf]['email']}")
        print(f"Senha: {CLIENTES[cpf]['senha']}")
        print(f"histórico: {CLIENTES[cpf]['historico']}")
    elif cpf in BARBEIROS:
        print("\nDados do usuário Barbeiro:")
        print(f"Nome: {BARBEIROS[cpf]['nome']}")
        print(f"Email: {BARBEIROS[cpf]['email']}")
        print(f"Senha: {BARBEIROS[cpf]['senha']}")
        print(f"histórico {BARBEIROS[cpf]['historico']}")
    elif cpf in ADMINISTRADORES:
        print("\nDados do usuário Administrador:")
        print(f"Nome: {ADMINISTRADORES[cpf]['nome']}")
        print(f"Email: {ADMINISTRADORES[cpf]['email']}")
        print(f"Senha: {ADMINISTRADORES[cpf]['senha']}")
    else:
        print("CPF não encontrado")
        return fluxo_administrador(cpf)
    
    print("\n1 - editar usuário")
    print("2 - excluir usuário")
    print("3 - Voltar")

    try:
        opc = int(input("Escolha uma opção: "))

        if opc == 1:
            print('Em desenvolvimento')
        elif opc == 2:
            print('Em desenvolvimento')
        elif opc == 3:
            return
        else:
            print('Opção inválida')
    except ValueError:
        print("Por favor, digite um número válido")
        