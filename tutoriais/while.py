#!/usr/bin/env python3

# tutorial_while.py

# Tutorial de como usar o loop 'while' em Python

print("Tutorial de como usar o 'while' em Python")

# 1. Usando 'while' com uma condição simples
print("\n1. Usando 'while' com uma condição simples:")
contador = 0
while contador < 5:
    print(contador)
    contador += 1  # Incrementa o contador a cada iteração

# 2. Usando 'while' com 'break' para sair do loop
print("\n2. Usando 'while' com 'break' para sair do loop:")
contador = 0
while True:  # O loop será infinito
    print(contador)
    contador += 1
    if contador >= 5:  # Quando contador atingir 5, o loop será interrompido
        break

# 3. Usando 'while' com 'continue' para pular iterações
print("\n3. Usando 'while' com 'continue' para pular uma iteração:")
contador = 0
while contador < 5:
    contador += 1
    if contador == 3:
        continue  # Pula a iteração quando contador for igual a 3
    print(contador)

# 4. Usando 'while' para realizar contagem regressiva
print("\n4. Usando 'while' para realizar uma contagem regressiva:")
contador = 10
while contador > 0:
    print(contador)
    contador -= 1  # Decrementa o contador a cada iteração
print("Fim da contagem regressiva!")

# 5. 'while' com listas (verificando um item até encontrar)
print("\n5. 'while' com listas (verificando um item até encontrar):")
numeros = [1, 3, 5, 7, 9]
indice = 0
while indice < len(numeros):
    if numeros[indice] == 5:  # Verifica se encontrou o número 5
        print("Encontrou o número 5!")
        break
    indice += 1

# 6. Usando 'while' com um dicionário
print("\n6. Usando 'while' com um dicionário:")

# Definindo um dicionário
pessoa = {'nome': 'João', 'idade': 30, 'cidade': 'São Paulo'}

# Vamos usar um 'while' para iterar sobre as chaves do dicionário
chaves = list(pessoa.keys())  # Convertemos as chaves em uma lista
indice = 0  # Índice para percorrer as chaves

while indice < len(chaves):
    chave = chaves[indice]
    valor = pessoa[chave]
    print(f"{chave}: {valor}")
    indice += 1

# 7. Exemplo de loop 'while' infinito (cuidado!)
print("\n7. Exemplo de loop 'while' infinito (não execute sem necessidade!):")
# while True:
#     print("Este loop nunca vai parar! Use com cuidado!")

print("\nFim do tutorial!")
