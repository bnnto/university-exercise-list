c1 = int(input("Digite o código da peça 1: "))
n1 = int(input("Digite número de peças 1: "))
v1 = float(input("Digite o valor da peça 1: "))
c2 = int(input("Digite o código da peça 2: "))
n2 = int(input("Digite número de peças 2: "))
v2 = float(input("Digite o valor da peça 2: "))
IPI = int(input("Digite o valor do IPI: "))
vt = ((n1 * v1) + (n2 * v2))
vT = (vt * (IPI / 100)) + vt
print(f"Valor total: R$ {vT:.2f}")


