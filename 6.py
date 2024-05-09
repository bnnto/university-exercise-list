a, b, c = map(float, input("Digite os três valores: ").split())
mA = (a + b + c) / 3
mH = 3 / ((1 / a) + (1 / b) + (1 / c))
print(f"A média aritmética ficou: {mA:.2f} e a harmônica ficou: {mH:.2f}")