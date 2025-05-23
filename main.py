import textwrap

def menu():
    menu = """
    =============== MENU ===============
    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Criar Usuário
    [5] Criar Conta
    [6] Listar Contas
    [0] Sair
    =>"""
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("Valor inválido para depósito.")
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif excedeu_limite:
        print("Operação falhou! Você excedeu o limite de saque.")
    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print(f"Saque de R$ {valor:.2f} realizado com sucesso!")

    else:
        print("Valor inválido para saque.")

    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO =================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("=========================================")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)


    if usuario:
        print("Usuário já cadastrado com esse CPF.")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (DD/MM/AAAA): ")
    endereco = input("Informe o endereço (logradouro, número - bairro - cidade/UF): ")

    usuarios.append({"nome": nome, "cpf": cpf, "data_nascimento": data_nascimento, "endereco": endereco})
    print(f"Usuário {nome} cadastrado com sucesso!")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None    

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print(f"Conta {numero_conta} criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    else:
        print("Usuário não encontrado. Conta não criada.")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
        Agência: \t{conta['agencia']}
        Conta: \t\t{conta['numero_conta']}
        Titular: \t{conta['usuario']['nome']}
        """
        print("-" * 100)
        print(textwrap.dedent(linha))

def main():
    
  LIMITE_SAQUES = 3
  AGENCIA = "0001"

  saldo= 0
  limite = 500
  extrato = ""
  numero_saques = 0
  usuarios = []
  contas = []

 
  while True:
    opcao = menu()

    if opcao == "1":
        valor = float(input("Informe o valor a ser depositado: "))

        saldo, extrato = depositar(saldo, valor, extrato)

    elif opcao == "2":
        valor = float(input("Informe o valor a ser sacado: "))

        saldo, extrato = sacar(
            saldo= saldo,
            valor= valor,
            extrato= extrato,
            limite= limite,
            numero_saques= numero_saques,
            limite_saques= LIMITE_SAQUES,
        )
    elif opcao == "3":
        exibir_extrato (saldo, extrato= extrato)

    elif opcao == "4":
        criar_usuario(usuarios)

    elif opcao == "5":
        numero_conta = len(contas) + 1
        conta = criar_conta(AGENCIA, numero_conta, usuarios)

        if conta:
            contas.append(conta)

    elif opcao == "6":
        listar_contas(contas)
    
    elif opcao == "0":
        print("Sistema encerrado.")
        break

    else:
        print("Opção inválida! Tente novamente uma das operações do menu.")

main()