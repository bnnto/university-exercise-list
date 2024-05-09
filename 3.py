A, B, C = map(float, input("Digite os lados do triângulo: ").split())
T = B ** 2 + C ** 2
if A ** 2 == T:
    print("Sim, é um triângulo retângulo.")
else:
    print("Não é um triângulo retângulo.")
