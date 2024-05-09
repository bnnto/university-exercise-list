r1, r2, r3 = map(float, input("Digite os valores dos três resistores: ").split())
rr = (1 / r1) + (1 / r2) + (1 / r3)
rE = 1 / rr
print(f"A resistência equivalente é {rE:.2f}")
