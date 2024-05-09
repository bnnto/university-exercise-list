pA, pB, pC = map(float, input("Digite o preço de cada ovo [A, B, C]: ").split())
tO = str(input("Qual ovo você deseja [A, B ou C]? "))
if tO == 'A':
    U = int(input("Quantas unidades você deseja? "))
    if U > 50:
        print("Não pode ser integralmente atendido, 50 unidades vão ser fornecidas.")
        vT = 50 * pA
        vD = vT * 0.1971
    else:
        vT = U * pA
        vD = vT * 0.1971
if tO == 'B':
    U = int(input("Quantas unidades você deseja? "))
    if U > 30:
        print("Não pode ser integralmente atendido, 30 unidades vão ser fornecidas.")
        vT = 30 * pB
        vD = vT * 0.1971
    else:
        vT = U * pA
        vD = vT * 0.1971
if tO == 'C':
    U = int(input("Quantas unidades você deseja? "))
    if U > 20:
        print("Não pode ser integralmente atendido, 20 unidades vão ser fornecidas.")
        vT = 20 * pC
        vD = vT * 0.1971
    else:
        vT = U * pA
        vD = vT * 0.1971
print(f"O total à ser pago é de R$ {vT:.2f} e o equivalente em doláres é de USD {vD:.2f}")