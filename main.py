def deposito(saldo, valor):
    saldo += valor
    return saldo

def saque(saldo, valor):
    saldo -= valor
    return saldo

def extrato(operacoes, saldo):
    print("Não foram realizadas movimentações" if not operacoes else operacoes)
    print(f"Saldo: R$ {saldo:.2f}")

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
operacoes = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == 'd':
        valor = float(input("Quanto deseja depositar: "))
        if(valor > 0):
            saldo = deposito(saldo, valor)
            operacoes += f"Depósito de R${valor:.2f}\n"
        else:
            print("Não é possível depositar valores negativos")

    elif opcao == 's':
        valor = float(input("Quanto deseja sacar: "))

        if(valor > saldo):
            print("Você não tem saldo o suficiente para a operação")

        elif(numero_saques >= LIMITE_SAQUES):
            print(f"Não é possível fazer mais que {LIMITE_SAQUES} saques ao dia")

        elif(valor <= 0):
            print("Não é possível sacar valores negativos ou igual a 0")

        elif(valor <= 500.00):
            saldo = saque(saldo, valor)
            operacoes += f"Saque de R${valor:.2f}\n"
            numero_saques += 1

        else:
            print("O limite do saque é de 500 reais")
        
    elif opcao == 'e':
        extrato(operacoes, saldo)

    elif opcao == 'q':
        break

    else:
        print("Operação inválida! Por favor, selecionar a opção desejada")
    