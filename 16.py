NV = {}
lT = []
value = 0
for i in range(5):
    name = input("Digite o nome do produto: ")
    value = float(input(f"Digite o valor do {name}: "))
    NV[name] = value
    lT.append(value)
    vT = sum(lT)
    m = vT / 5

print(f"O preço médio dos produtos foi R$ {m:.2f}")

if value > 20:
    print("Os seguintes produtos tem preços superiores a 20 reais:")
    [print(f"{name}, custa R$ {value}") for name, value in NV.items() if value > 20]
if value < 10:
    print("Os seguintes produtos tem preços inferiores a 10 reais:")
    [print(f"{name}, custa R$ {value}") for name, value in NV.items() if value < 10]
if value < m:
    print("Os seguintes produtos tem preços inferiores à média:")
    [print(f"{name}, custa R$ {value}") for name, value in NV.items() if value < m]
