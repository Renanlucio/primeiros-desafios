menu = """

[1] DEPOSITAR
[2] SACAR
[3] EXTRATO
[4] SAIR
=> """

Saldo = 0
limite = 500
Extrato = ""
numero_saques = 0
limite_saques = 3

while True:
    opcao = input(menu)
    3
    if opcao == "1":
        print("deposito")
        valor =float(input("qual valor deseja depositar?"))
        if valor > 0:
            Saldo += valor
            Extrato += f"Deposito: R$ {valor: .2f}\n"
            print("insira as notas no local indicado.")
        else:
            print("operação invalida!")


    elif opcao == "2":
        print("Saque")
        valor = int(input("qual valor deseja sacar?"))
        
        excedeu_saldo = valor > Saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= limite_saques

        if excedeu_saldo:
            print("Operação falho! você não tem saldo o suficiente")
        elif excedeu_limite:
            print("Operação falhou! limite de saque excedido!")
        elif excedeu_saques:
            print("Operação falhou! Número de saques excedido")
        elif valor > 0:
            Saldo -= valor
            Extrato += f"saque: R${valor: .2f}\n"
            numero_saques =+ 1
            print("Aguarde a contagem das notas e retire no local indicado!")
        else:
            print("Operação falhou! valor informado invalido.")
    
    elif opcao == "3":
        print("\n========extrato========")
        print("Não foram realizadas movimentações." if not Extrato else Extrato)
        print(f"\n Saldo: R$ {Saldo: .2f}")
        print("=========================")
    
    elif opcao == "4":
        break

    else:
        print("operação invalida!")