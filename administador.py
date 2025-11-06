from menu import Menu_administrador
from banco import BARBEIROS, ADMINISTRADORES, CLIENTES, salvar_barbeiro, salvar_cliente, salvar_admin
import os
import time

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

def deletar_usuario(cpf):
    if cpf in CLIENTES:
        confirmacao = input(f"Tem certeza que deseja deletar o cliente com CPF {cpf}? (s/n): ").strip().lower()
        if confirmacao == 's':
            del CLIENTES[cpf]
            print(f"\n Cliente com CPF {cpf} excluído com sucesso.")
        else:
            print("\n Exclusão cancelada.")
    elif cpf in BARBEIROS:
        confirmacao = input(f"Tem certeza que deseja deletar o barbeiro com CPF {cpf}? (s/n): ").strip().lower()
        if confirmacao == 's':
            del BARBEIROS[cpf]
            print(f"\n Barbeiro com CPF {cpf} excluído com sucesso.")
        else:
            print("\n Exclusão cancelada.")
    elif cpf in ADMINISTRADORES:
        if len(ADMINISTRADORES) == 1:
            print("\n Não é possível deletar o único administrador do sistema.")
            return

def fluxo_gerenciar_usuarios(cpf):
    os.system('cls')
    print("=============================")
    print("      gerenciar usuários     ")
    print("=============================")

    listar_usuarios()
    opc = 0
    cpf = input('\nInforme o cpf do usuario que deseja gerenciar: ').strip()
    
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
        time.sleep(2)
        return fluxo_administrador(cpf)
    
    print("\n1 - editar usuário")
    print("2 - excluir usuário")
    print("3 - Voltar")

    try:
        opc = int(input("Escolha uma opção: "))

        if opc == 1:
            print('Em desenvolvimento')
        elif opc == 2:
           deletar_usuario(cpf)
           listar_usuarios()
           time.sleep(3)
           return fluxo_administrador(cpf)
        elif opc == 3:
           return fluxo_administrador(cpf)
        else:
            print('Opção inválida')
    except ValueError:
        print("Por favor, digite um número válido")
        