import math
O = int(input("Digite a operação [1 ou 2]: "))
r = int(input("Digite o raio da circunferência: "))
A = math.pi * (r ** 2)
P = 2 * math.pi * r
if O == 1:
    print(f"Área da circunferência: {A:.2f}")
elif O == 2:
    print(f"Perímetro da circunferência: {P:.2f}")
else:
    print("O indicador de operação foi mal fornecido.")
