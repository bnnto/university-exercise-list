H = int(input("Digite quantas horas: "))
M = int(input("Digite quantos minutos: "))
S = int(input("Digite quantos segundos: "))
sH = H * 3600
sM = M * 60
T = sH + sM + S
print("O valor total em segundos é de", T)