pV = float(input("Digite o preço à vista: "))
t1 = str(input("Você quer parcelar? [Sim ou nao]: "))
if t1 == 'Nao' or t1 == 'nao':
    print(f"O valor que você deve pagar é de R$ {pV:.2f}")
    exit()
if t1 == 'Sim' or t1 == 'sim':
    t2 = int(input("Você quer parcelar em quantas vezes? [3 ou 5]: "))
    if t2 == 3:
        ac1 = (pV * 0.1) + pV
        men1 = ac1 / 3
        print(f"O valor total ficou R$ {ac1:.2f} e o valor da prestação mensal é R$ {men1:.2f}")
    elif t2 == 5:
        ac2 = (pV * 0.2) + pV
        men2 = ac2 / 5
        print(f"O valor total ficou R$ {ac2:.2f} e o valor da prestação mensal é R$ {men2:.2f}")