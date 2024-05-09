itemsE = int(input("Digite quantos items tem no estoque: "))
itemsF = int(input("Digite o número de items a serem fornecidos: "))
if itemsF > itemsE:
    print("Não tem itens suficientes no estoque para atender seu pedido.")
else:
    print(f"Estoque atualizado: {itemsE - itemsF}")