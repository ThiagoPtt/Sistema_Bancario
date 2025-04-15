menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 1000;
limite = 500;
extrato = ""
numero_de_saques = 0;
limite_de_saques = 3;

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Digite o valor do depósito:"))
        if valor > 0:
            saldo = saldo + valor
            extrato = extrato + f"Depósito: R$ {valor:.2f}\n"
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
        
    elif opcao == "s":
        valor = float(input("Digite o valor do saque:"))
        if numero_de_saques < limite_de_saques:
            if valor > 0 and valor <= saldo and valor <= limite:
                saldo = saldo - valor
                extrato = extrato + f"Saque: R$ {valor:.2f}\n"
                print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
                numero_de_saques = numero_de_saques + 1
            else:
                print("Valor inválido para saque!")
        else:
            print("Número máximo de saques atingido!")
            
    elif opcao == "e":
        print("=== Extrato ===")
        print(extrato)
        print(f"Saldo: R$ {saldo:.2f}")
        print("================")

    elif opcao == "q":
        break

    else:
        print("Valor inválido para depósito!")