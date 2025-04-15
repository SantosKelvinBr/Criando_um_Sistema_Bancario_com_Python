menu = """

-------Sistema Bancario v1.0--------

        [1] Depositar
        [2] Sacar
        [3] Extrato
        [0] Sair

--------Versão 1.0 de teste--------        

=>"""

saldo= 0
limite = 500
extrato = ""
numero_saques = 0
limite_saques = 3   

while True:
    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Informe o valor a ser depositado: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso!") 
        else:
            print("Valor inválido! Tente novamente.")

    elif opcao == "2":
        valor = float(input("Informe o valor a ser sacado: "))

        if valor > 0:
            if valor <= saldo and valor <= limite and numero_saques < limite_saques:
                saldo -= valor
                extrato += f"Saque: R$ {valor:.2f}\n"
                numero_saques += 1
                print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
            elif valor > saldo:
                print("Saldo insuficiente!")
            elif valor > limite:
                print("O valor do saque excede o limite permitido!")
            elif numero_saques >= limite_saques:
                print("Número máximo de saques diários atingido!")
        else:
            print("Valor inválido! Tente novamente.")

    elif opcao == "3":
        print("\n------- Extrato -------")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo atual: R$ {saldo:.2f}")
        print("-----------------------")

    elif opcao == "0":
        print("Sistema encerrado.")
        break

    else:
        print("Opção inválida! Tente novamente uma das operações do menu.")
       