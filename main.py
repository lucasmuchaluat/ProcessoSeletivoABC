import sender
from datetime import datetime

# contem informações cadastrais dos clientes
clientes = [
    {
        "nome": "Lucas Muchaluat",
        "saldo": 100,
        "email": "lucasmuchaluat@gmail.com"
    },
    {
        "nome": "Luiz Vitor Germanos",
        "saldo": 100,
        "email": "luvi@germanos.ws"
    },
]

# contem informações dos debitos diarios
compromissos = [
    {
        "devedor": "Lucas Muchaluat",
        "debito diário": 500
    },
    {
        "devedor": "Luiz Vitor Germanos",
        "debito diário": 500
    },
]

# armazena historico de movimentações
historico = []

# rotina check 30 minutos


def checkSaldo():
    for compromisso in compromissos:
        for cliente in clientes:
            if compromisso["devedor"] == cliente["nome"]:
                if compromisso["debito diário"] > cliente["saldo"]:
                    sender.sendEmail(cliente["nome"], cliente["email"])

# simula movimentacao na conta corrente


def simulaMovimentacao(nomeCliente, valorCompra):
    for cliente in clientes:
        if cliente["nome"] == nomeCliente:
            cliente["saldo"] -= valorCompra
            now = datetime.now()
            dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
            tempDict = {"cliente": nomeCliente,
                        "variacao": valorCompra, "data": dt_string}
            historico.append(tempDict)


simulaMovimentacao("Lucas Muchaluat", 50)
checkSaldo()
print(clientes)
print(historico)
