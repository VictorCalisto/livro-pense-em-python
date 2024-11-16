#!/usr/bin/env python3

# tutorial_operadores_gerais.py

# ===== Operadores Aritméticos =====
print("===== Operadores Aritméticos =====")

# 1. Operador de Soma (+)
a = 10
b = 5
resultado_soma = a + b
print(f"{a} + {b} = {resultado_soma}")  # Saída: 10 + 5 = 15

# 2. Operador de Subtração (-)
a = 10
b = 5
resultado_subtracao = a - b
print(f"{a} - {b} = {resultado_subtracao}")  # Saída: 10 - 5 = 5

# 3. Operador de Multiplicação (*)
a = 10
b = 5
resultado_multiplicacao = a * b
print(f"{a} * {b} = {resultado_multiplicacao}")  # Saída: 10 * 5 = 50

# 4. Operador de Divisão (/)
a = 10
b = 5
resultado_divisao = a / b
print(f"{a} / {b} = {resultado_divisao}")  # Saída: 10 / 5 = 2.0

# 5. Operador de Divisão Inteira (//)
a = 10
b = 3
resultado_divisao_inteira = a // b
print(f"{a} // {b} = {resultado_divisao_inteira}")  # Saída: 10 // 3 = 3

# 6. Operador de Resto da Divisão (%)
a = 10
b = 3
resultado_resto = a % b
print(f"{a} % {b} = {resultado_resto}")  # Saída: 10 % 3 = 1

# 7. Operador de Exponenciação (**)
a = 2
b = 3
resultado_exponenciacao = a ** b
print(f"{a} ** {b} = {resultado_exponenciacao}")  # Saída: 2 ** 3 = 8


# ===== Operadores de Atribuição =====
print("\n===== Operadores de Atribuição =====")

# 1. Atribuição simples (=)
a = 10
b = 5
c = a + b
print(f"Atribuição simples: c = {c}")  # Saída: c = 15

# 2. Atribuição com adição (+=)
a = 10
a += 5  # Equivalente a: a = a + 5
print(f"Atribuição com adição (+=): a = {a}")  # Saída: a = 15

# 3. Atribuição com subtração (-=)
a = 10
a -= 5  # Equivalente a: a = a - 5
print(f"Atribuição com subtração (-=): a = {a}")  # Saída: a = 5

# 4. Atribuição com multiplicação (*=)
a = 10
a *= 5  # Equivalente a: a = a * 5
print(f"Atribuição com multiplicação (*=): a = {a}")  # Saída: a = 50

# 5. Atribuição com divisão (/=)
a = 10
a /= 5  # Equivalente a: a = a / 5
print(f"Atribuição com divisão (/=): a = {a}")  # Saída: a = 2.0

# 6. Atribuição com divisão inteira (//=)
a = 10
a //= 3  # Equivalente a: a = a // 3
print(f"Atribuição com divisão inteira (//=): a = {a}")  # Saída: a = 3

# 7. Atribuição com resto da divisão (%=)
a = 10
a %= 3  # Equivalente a: a = a % 3
print(f"Atribuição com resto da divisão (%=): a = {a}")  # Saída: a = 1

# 8. Atribuição com exponenciação (**=)
a = 2
a **= 3  # Equivalente a: a = a ** 3
print(f"Atribuição com exponenciação (**=): a = {a}")  # Saída: a = 8

# ===== Operadores de Associação =====
print("\n===== Operadores de Associação =====")

# 1. Operador 'in'
lista = [1, 2, 3, 4, 5]
if 3 in lista:
    print("3 está na lista.")  # Saída: 3 está na lista.

# 2. Operador 'not in'
if 6 not in lista:
    print("6 não está na lista.")  # Saída: 6 não está na lista.


# Fim do Tutorial
print("\n===== Fim do Tutorial =====")
