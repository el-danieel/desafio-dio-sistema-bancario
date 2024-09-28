import datetime

def criar_usuario(usuarios):
    cpf = int(input("CPF do usuário (apenas números): "))

    for usuario in usuarios:
        if(usuario['cpf'] == cpf):
            print("Usuário já existente.")
            return
    
    nome = str(input("Nome do usuário: "))
    dt_nascimento = str(input("Data de nascimento do usuário (dd/mm/aaaa): "))
    logradouro = str(input("Logradouro do usuário: "))
    num_logradouro = int(input("Número do logradouro: "))
    bairro = str(input("Bairro do logradouro: "))
    cidade = str(input("Cidade do logradouro: "))
    uf = str(input("Unidade federativa do logradouro: "))
    usuarios.append({
        'cpf': cpf,
        'nome': nome,
        'dt_nascimento': dt_nascimento,
        'logradouro': logradouro,
        'num_logradouro': num_logradouro,
        'bairro': bairro,
        'cidade': cidade,
        'uf': uf
        })
    print('Usuário criado')
    return usuarios

def criar_conta(agencia, numero_conta, usuarios):
    cpf = int(input("CPF do usuário (apenas números): "))
    usuario = buscar_usuario_por_cpf(cpf, usuarios)
    if usuario:
        return {
            'agencia': agencia,
            'numero_conta': numero_conta,
            'usuario': usuario
        }

def deposito(saldo, valor, extrato, LIMITE_TRANSACOES, /):
    
    if(contar_transacoes_hoje(extrato) >= LIMITE_TRANSACOES):
        print(f"Não é possível fazer mais que {LIMITE_TRANSACOES} transações ao dia")
    elif(valor > 0):
        saldo += valor
        extrato = gravar_extrato(extrato, 'Depósito', valor, datetime.datetime.now())
    else:
        print("Não é possível depositar valores negativos")
    
    return saldo, extrato

def saque(*, saldo, valor, extrato, LIMITE_TRANSACOES, limite_saque):
    
    if(valor > saldo):
        print("Você não tem saldo o suficiente para a operação")

    elif(contar_transacoes_hoje(extrato) >= LIMITE_TRANSACOES):
        print(f"Não é possível fazer mais que {LIMITE_TRANSACOES} transações ao dia")

    elif(valor <= 0):
        print("Não é possível sacar valores negativos ou igual a 0")

    elif(valor <= limite_saque):
        saldo -= valor
        extrato = gravar_extrato(extrato, 'Saque', valor, datetime.datetime.now())

    else:
        print(f"O limite do saque é de {limite_saque} reais")

    return saldo, extrato

def gravar_extrato(extrato, tipo_operacao, valor, data_hora):
    id_transacao = len(extrato)
    extrato[id_transacao] = {
        'tipo_operacao': tipo_operacao,
        'valor': valor,
        'data_hora': data_hora 
    }
    return extrato

def ver_extrato(extrato, /, *, saldo):
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

def listar_contas(contas):
    for conta in contas:
        print(f"Agência: {conta['agencia']}")
        print(f"Número da conta: {conta['numero_conta']}")
        print(f"Titular: {conta['usuario']['nome']}\n")

def buscar_usuario_por_cpf(cpf, usuarios):
    # Buscar o usuário na lista de usuários pelo CPF
    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            return usuario
    return None

def menu():
    menu = """
    [nu] Novo usuário
    [nc] Nova conta
    [lc] Listar contas
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair

    => """
    return input(menu)

def main():
    saldo = 0
    limite_saque = 500
    extrato = {}
    usuarios = []
    contas = []
    LIMITE_TRANSACOES = 10
    AGENCIA = '0001'

    while True:
        opcao = menu()
        if opcao == 'nu':
            usuarios = criar_usuario(usuarios)
        
        elif opcao == 'nc':
            nummero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, nummero_conta, usuarios)
            if conta:
                contas.append(conta)
                print('Conta criada.')

        elif opcao == 'lc':
            listar_contas(contas)

        elif opcao == 'd':
            valor = float(input("Quanto deseja depositar: "))
            saldo, extrato = deposito(saldo, valor, extrato, LIMITE_TRANSACOES)

        elif opcao == 's':
            valor = float(input("Quanto deseja sacar: "))
            saldo, extrato = saque(saldo = saldo, valor = valor, extrato = extrato, LIMITE_TRANSACOES = LIMITE_TRANSACOES, limite_saque = limite_saque)
            
        elif opcao == 'e':
            ver_extrato(extrato, saldo = saldo)
        
        elif opcao == 'q':
            break

        else:
            print("Operação inválida! Por favor, selecionar a opção desejada")
    
main()