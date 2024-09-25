import datetime

def criar_usuario():
    return

def deposito(saldo, valor):
    saldo += valor
    return saldo

def saque(saldo, valor):
    saldo -= valor
    return saldo

def gravar_extrato(extrato, tipo_operacao, valor, data_hora):
    id_transacao = len(extrato)
    extrato[id_transacao] = {
        'tipo_operacao': tipo_operacao,
        'valor': valor,
        'data_hora': data_hora 
    }
    return extrato

def ver_extrato(extrato, saldo):
    if not extrato:
        print("Não foram realizadas movimentações")
    else:
        for transacao in extrato.values():
            data_hora = transacao['data_hora'].strftime('%H:%M:%S do dia %d/%m/%Y')
            print(f"{transacao['tipo_operacao']} de {transacao['valor']:.2f} às {data_hora}")
    print(f"Saldo: R$ {saldo:.2f}")

def contar_transacoes_hoje(extrato):
    hoje = datetime.datetime.now().date()
    total = 0
    for transacao in extrato.values():
        if transacao['data_hora'].date() == hoje: total += 1
    return total

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = {}
LIMITE_TRANSACOES = 10

while True:
    opcao = input(menu)

    # =======================DEPÓSITO=================================
    if opcao == 'd':
        valor = float(input("Quanto deseja depositar: "))
        if(contar_transacoes_hoje(extrato) >= LIMITE_TRANSACOES):
            print(f"Não é possível fazer mais que {LIMITE_TRANSACOES} transações ao dia")
        elif(valor > 0):
            saldo = deposito(saldo, valor)
            extrato = gravar_extrato(extrato, 'Depósito', valor, datetime.datetime.now())
        else:
            print("Não é possível depositar valores negativos")

    # =======================SAQUE=================================
    elif opcao == 's':
        valor = float(input("Quanto deseja sacar: "))

        if(valor > saldo):
            print("Você não tem saldo o suficiente para a operação")

        elif(contar_transacoes_hoje(extrato) >= LIMITE_TRANSACOES):
            print(f"Não é possível fazer mais que {LIMITE_TRANSACOES} transações ao dia")

        elif(valor <= 0):
            print("Não é possível sacar valores negativos ou igual a 0")

        elif(valor <= 500.00):
            saldo = saque(saldo, valor)
            extrato = gravar_extrato(extrato, 'Saque', valor, datetime.datetime.now())

        else:
            print("O limite do saque é de 500 reais")

    # =======================EXTRATO=================================
    elif opcao == 'e':
        ver_extrato(extrato, saldo)
    
    # =======================SAIR=================================
    elif opcao == 'q':
        break

    else:
        print("Operação inválida! Por favor, selecionar a opção desejada")
    