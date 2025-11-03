from banco import BARBEIROS, ADMINISTRADORES, CLIENTES

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
        listar_usuarios()
        return True 

  
   else:
      print('O cpf informado não está cadastrado')
      return False

def fluxo_gerenciar_usuarios():
    print("====Gerenciar usuários====")
    print("1 - Listar todos os usuários")
    print("2 - deletar usuário")
    print("3 - cadastrar usuario ")



  