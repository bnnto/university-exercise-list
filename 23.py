N = int(input("Digite sua nota: "))
if N < 3:
    print("Seu conceito é E")
elif 3 <= N <= 5:
    print("Seu conceito é D")
elif N == 6 or N == 7:
    print("Seu conceito é C")
elif N == 8 or N == 9:
    print("Seu conceito é B")
elif N > 10:
    print("Sua nota foi inserida incorretamente.")
else:
    print("Seu conceito é A")
