# [S] - sacar
# [D] - depsitar
# [E] - visualizar extrato
# [F] - finalizar

intro = """
Digite a operação desejada:
# [D] - depositar
# [S] - sacar
# [E] - visualizar extrato
# [F] - finalizar
"""
print(intro)
op = input()
saldo = 0.0
movi = 0.0
qtd_saque = 3
limite = 500
extrat = ""

if op == "F":
    print("Sessão finalizada")
else:
    while True:
        if op == "F":
            print("Sessão finalizada")
            break

        elif op == "D":
            movi = float(input())
            if movi <= 0.0:
                print("Favor depositar quantia positiva")
            else:
                saldo += movi
                print(f"Deposito de R${movi}")
                extrat += f"\n.D +{movi}"

        elif op == "S":
            if qtd_saque > 0:
                movi = float(input())
                if movi <= 500 and movi <= saldo:
                    print(f"Saldo anterior:{saldo}")
                    saldo -= movi
                    print(f"Saldo atualizado:{saldo}")
                    qtd_saque -= 1
                    print(f"Restam {qtd_saque} saques")
                    extrat += f"\n.S -{movi}"
                else:
                    if movi > saldo:
                        print("Saldo insuficiente")
                    if movi > 500:
                        print("Limite por saque de: R$500,00")
            else:
                print("Limite de quantidade de saque atingido")

        elif op == "E":
            print(extrat)
            print(f"Saldo: {saldo}")
        else:
            print("Operacao inválida")
        
        print(intro)
        op = input()
