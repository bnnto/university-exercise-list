X, Y, Z = map(float, input().split())
lM = max(X, Y, Z)
lMEN = min(X, Y, Z)
lMEI = (X + Y + Z) - (lM + lMEN)
if lM >= (lMEI + lMEN):
    print("Não forma triângulo")
    exit()
if X == Y == Z:
    print("Triângulo equilátero")
    exit()
if X != Y != Z:
    print("Triângulo escaleno")
if X == Y or X == Z or Y == Z:
    print("Triângulo isosceles")
