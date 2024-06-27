menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0.
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:


    opcao = input(menu)

    if opcao == "d":
        deposito= float(input("O quanto você quer depositar? "))
        if (deposito >= 0):
            saldo += deposito;
            extrato += f"Depósito: R${deposito:.2f}\n"
            print("Depósito concluído")
        else:
            print("Valor inválido para depósito")
        

    elif opcao == "s":
        if(numero_saques<LIMITE_SAQUES):
            saque = float(input("O quanto você quer sacar? "))
            if(saque>=0):
                if (saque<=limite):
                    if (saldo-saque>=0):
                        saldo -= saque
                        numero_saques = numero_saques+1
                        extrato += f"Saque: R${saque:.2f}\n"
                        print("Saque concluído")
                    else:
                        print("Saldo insuficiente")
                else:
                    print("Valor superior ao limite de R$500,00")
            else:
                print("Valores negativos são inválidos para saque")
        else:
            print("Número de saques excedeu o limite de 3 saques diários")

    elif opcao == "e":
        print("Extrato:")
        print(extrato)
        print(f"Saldo atual da conta: R${saldo:.2f}")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada")