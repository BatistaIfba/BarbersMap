#Banco de dados em memória
import json

BARBEIROS = {}
with open("bancoJson/BARBEIROS.json", "r") as f:
    BARBEIROS = json.load(f)

CLIENTES = {}
with open("bancoJson/CLIENTES.json", "r") as f:
    CLIENTES = json.load(f)

ADMINISTRADORES = {}
with open("bancoJson/ADMINISTRADORES.json", "r") as f:
    ADMINISTRADORES = json.load(f)

def salvar_cliente():
    with open("bancoJson/CLIENTES.json", "w") as f:
        json.dump(CLIENTES, f, indent=4)

def salvar_barbeiro():
    with open("bancoJson/BARBEIROS.json", "w") as f:
        json.dump(BARBEIROS, f, indent=4)    

def salvar_admin():
    with open("bancoJson/ADMINISTRADORES.json", "w") as f:
        json.dump(ADMINISTRADORES, f, indent=4)
