#!/usr/bin/env python3

# tutorial_for.py

# Tutorial de como usar o loop 'for' em Python

print("Tutorial de como usar o 'for' em Python")

# 1. Como usar o 'for' com uma lista de valores
print("\n1. Usando 'for' com uma lista:")
lista = [1, 2, 3, 4, 5]
for numero in lista:
    print(numero)

# 2. Usando 'for' com a função range()
print("\n2. Usando 'for' com a função range():")
# range(start, stop, step)
# Inicia no 0, vai até 5 (sem incluir o 5), e incrementa de 1
for i in range(5):
    print(i)

# 3. Usando 'for' com intervalo customizado
print("\n3. Usando 'for' com um intervalo personalizado (start, stop, step):")
# Aqui, começamos de 3 e vamos até 20, saltando de 5 em 5
for i in range(3, 20, 5):
    print(i)

# 4. Usando 'for' em uma string
print("\n4. Usando 'for' para iterar sobre uma string:")
frase = "Python"
for letra in frase:
    print(letra)

# 5. Iterando sobre um dicionário (dict)
print("\n5. Usando 'for' em um dicionário:")
dicionario = {'nome': 'João', 'idade': 30, 'cidade': 'São Paulo'}
for chave, valor in dicionario.items():
    print(f"{chave}: {valor}")

# 6. Usando 'for' com listas aninhadas
print("\n6. Usando 'for' com listas aninhadas:")
listas = [[1, 2], [3, 4], [5, 6]]
for lista in listas:
    for item in lista:
        print(item)

print("\nFim do tutorial!")
