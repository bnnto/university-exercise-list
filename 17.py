NV = {}
c50 = 0
lT = []
for i in range(5):
    name = input("Digite o seu nome: ")
    value = float(input(f"{name}, digite quanto você pagou por sua compra: "))
    NV[name] = value
    lT.append(value)
    vT = sum(lT)
    if value < 50:
        c50 += 1

print(f"O valor total pago pelos clientes foi R$ {vT:.2f}")
print(f"O valor da compra média efetuada foi R$ {vT / 5:.2f}")
if value > 20:
    print("Os seguintes clientes efetuaram compras superiores a 20 reais:")
    [print("", name) for name, value in NV.items() if value > 20]
else:
    print("Ninguem efetuou compras superiores a 20 reais.")
print(f"{c50} cliente(s) efetuaram compras inferiores a 50 reais.")