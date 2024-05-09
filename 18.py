mt = {}
m10 = 0
for i in range(5):
    mu = input("Digite o nome do município: ")
    temp = int(input(f"Digite a temperatura média em {mu}: "))
    mt[mu] = temp
    if temp < 10:
        m10 += 1

print(f"{m10} município(s) têm temperatura média inferior a 10ºC.")
if temp > 30:
    print("Os seguintes municípios têm temperatura média superior a 30ºC:")
    [print("", mu) for mu, temp in mt.items() if temp > 30]
else:
    print("Nenhum município tem temperatura média superior a 30ºC.")