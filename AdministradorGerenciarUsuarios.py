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
   usuario = input("informe o cpf do usuario que deseja deletar:")
   for cpf in ADMINISTRADORES.items():
      if  usuario == administradores[cpf]:
         del ADMINISTRADORES[cpf]
         print('Usuario deletado com sucesso!')
         return True
      else:
         print('O cpf informado não está cadastrado')
         return False
