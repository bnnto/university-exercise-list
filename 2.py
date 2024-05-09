n1, n2, n3 = map(float, input("Digite suas três notas: ").split())
m = (n1 + n2 + n3) / 3
if m >= 9:
    print("Seu conceito é A")
elif 9 < m <= 7.5:
    print("Seu conceito é B")
elif 7.5 < m <= 6.0:
    print("Seu conceito é C")
else:
    print("Seu conceito é D")
print(f"Média: {m:.2f}")