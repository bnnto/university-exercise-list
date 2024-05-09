cF = float(input("Digite o valor do custo de fábrica do carro: "))
pD = 28 / 100
I = 45 / 100
cC = cF + (pD * cF) + (I * cF)
print(f"O custo ao consumidor é de R$ {cC:.2f}")