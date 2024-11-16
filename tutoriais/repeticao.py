#!/usr/bin/env python3


frutas = ["maçã", "banana", "laranja"]
for fruta in frutas:
    print(fruta)


pessoa = {'nome': 'João', 'idade': 30, 'cidade': 'São Paulo'}
for chave, valor in pessoa.items():
    print(f"{chave}: {valor}")


tupla = (1, 2, 3, 4)
for item in tupla:
    print(item)


numeros = [1, 2, 3, 4, 5]
quadrados = [x**2 for x in numeros]
print(quadrados)  # [1, 4, 9, 16, 25]
pares = [x for x in numeros if x % 2 == 0]
print(pares)  # [2, 4]


for i in range(5):
    if i == 2:
        continue  # Pula o número 2
    elif i == 4:
        break  # Interrompe o loop no número 4
    print(f"Break e Continue: {i}")
# Break e Continue: 0
# Break e Continue: 1
# Break e Continue: 3

numeros = [10, 20, 30, 40]
iterador = iter(numeros)

print(next(iterador))  # 10
print(next(iterador))  # 20
print(next(iterador))  # 30
print(next(iterador))  # 40
print(next(iterador))  # Erro