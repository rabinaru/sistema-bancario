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
                print(f"Deposito de R${movi:.2f}")
                extrat += f"\n.D +{movi}"

        elif op == "S":
            if qtd_saque > 0:
                movi = float(input())
                if movi <= 500 and movi <= saldo:
                    print(f"Saldo anterior:{saldo:.2f}")
                    saldo -= movi
                    print(f"Saldo atualizado:{saldo:.2f}")
                    qtd_saque -= 1
                    print(f"Restam {qtd_saque} saques")
                    extrat += f"\n.S -{movi:.2f}"
                else:
                    if movi > saldo:
                        print("Saldo insuficiente")
                        print(f"Saldo atual: R${saldo:.2f}")
                    if movi > 500:
                        print("Limite por saque de: R$500,00")
            else:
                print("Limite de quantidade de saque atingido")

        elif op == "E":
            if len(extrat)>0:
                print(extrat)
                print(f"Saldo: R${saldo:.2f}")
            else:
                print("Não foram realizadas movimentações")
        else:
            print("Operacao inválida")
        
        print(intro)
        op = input()
