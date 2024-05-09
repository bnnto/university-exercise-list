# Utilize 1 para cliente comum, 2 para cliente especial e 3 para funcionário.
C = int(input("Digite seu código: "))
vT = float(input("Digite o valor total: "))
if C == 2:
    print(F"O valor total da compra com desconto é: R$ {vT - (vT * 0.1):.2f}")
elif C == 3:
    print(F"O valor total da compra com desconto é: R$ {vT - (vT * 0.05):.2f}")
else:
    print(F"O valor total da compra é R$ {vT}")