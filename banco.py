#Banco de dados em memória
BARBEIROS = {
    "00000000000": {
        "nome": "barbeiroteste",
        "senha": "senhateste",
        "email": "barbeiro@gmail.com",
        "tipo_usuario": "barbeiro",
        "endereco": "Rua Arlindo, Bairro Dali, Número 29",
        "sobre": "Eu tenho talento!, se nao gostar do corte eu vou te devolver o seu dinheiro!",
        "servicos": [
            {"nome": "Corte Social", "valor": 45, "tempo": 40},
            {"nome": "Barba Simples", "valor": 20, "tempo": 20},
            {"nome": "Corte na Tesoura", "valor": 55, "tempo": 50},
        ],
        "agendamentos" : [
            {"cliente": "Lucas", "servico": "Corte Social", "valor": 45, "data": "13/11"},
            {"cliente": "Batista", "servico": "Barba Simples", "valor": 20, "data": "14/11"},
        ],
        "historico": [
            {"cliente": "Alejandro", "servico": "Corte Social", "valor": 45, "data": "01/11"},
            {"cliente": "Ravana", "servico": "Corte na Tesoura", "valor": 55, "data": "02/11"},
        ],
    },
}

CLIENTES = {
    "11111111111": {
        "nome": "clienteteste",
        "senha": "senhateste",
        "email": "cliente@gmail.com",
        "tipo_usuario": "cliente",
        "agendamentos": [
            {"barbeiro": "BarbeiroTeste", "servico": "Corte Social", "valor": 45, "data": "08/11"},
        ],
        "historico": [
            {"barbeiro": "BarbeiroTeste", "servico": "Corte Social", "valor": 45, "data": "01/11"},
        ],
    },
}

ADMINISTRADORES = {
    "12345678910": {
        "nome": "admin",
        "email": "admin@gmail.com",
        "senha": "12345678",
        "tipo_usuario": "administrador"
    },
}