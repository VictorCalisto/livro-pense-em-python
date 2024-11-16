#!/usr/bin/env python3


# tutorial_operadores_logicos.py

# Operadores de Comparação
print("===== Operadores de Comparação =====")

# 1. Operador '=='
a = 5
b = 5
if a == b:
    print(f"{a} é igual a {b}")  # Saída: 5 é igual a 5

# 2. Operador '!='
a = 5
b = 10
if a != b:
    print(f"{a} é diferente de {b}")  # Saída: 5 é diferente de 10

# 3. Operador '<'
a = 3
b = 5
if a < b:
    print(f"{a} é menor que {b}")  # Saída: 3 é menor que 5

# 4. Operador '>'
a = 7
b = 5
if a > b:
    print(f"{a} é maior que {b}")  # Saída: 7 é maior que 5

# 5. Operador '<='
a = 3
b = 5
if a <= b:
    print(f"{a} é menor ou igual a {b}")  # Saída: 3 é menor ou igual a 5

# 6. Operador '>='
a = 7
b = 5
if a >= b:
    print(f"{a} é maior ou igual a {b}")  # Saída: 7 é maior ou igual a 5


# Operadores Lógicos
print("\n===== Operadores Lógicos =====")

# 1. Operador 'and'
a = 5
b = 10
if a > 0 and b > 5:
    print("Ambas as condições são verdadeiras.")  # Saída: Ambas as condições são verdadeiras.

# 2. Operador 'or'
a = 5
b = 3
if a > 0 or b > 5:
    print("Pelo menos uma das condições é verdadeira.")  # Saída: Pelo menos uma das condições é verdadeira.

# 3. Operador 'not'
a = 5
if not a < 0:
    print("a não é menor que 0.")  # Saída: a não é menor que 0.

# 4. Operador '^' (XOR)
a = 5
b = 10
# XOR: Uma condição verdadeira e a outra falsa
if (a > 0) ^ (b < 5):
    print("Uma das condições é verdadeira, mas não ambas.")  # Saída: Uma das condições é verdadeira, mas não ambas.

# 5. Operador 'in'
lista = [1, 2, 3, 4, 5]
if 3 in lista:
    print("3 está na lista.")  # Saída: 3 está na lista.

# 6. Operador 'not in'
if 6 not in lista:
    print("6 não está na lista.")  # Saída: 6 não está na lista.

# Operadores de Identidade 
print("\n===== Operadores de Identidade =====")

# 1. Operador 'is'
a = [1, 2, 3]
b = a
if a is b:
    print("a e b referenciam o mesmo objeto.")  # Saída: a e b referenciam o mesmo objeto.

# 2. Operador 'is not'
a = [1, 2, 3]
b = [1, 2, 3]
if a is not b:
    print("a e b não referenciam o mesmo objeto.")  # Saída: a e b não referenciam o mesmo objeto.

