#!/usr/bin/env python3


# tutorial_if.py

# Tutorial de Estruturas de Seleção em Python

print("Tutorial de Estruturas de Seleção em Python")

# 1. Estrutura de seleção simples (if)
print("\n1. Estrutura de Seleção Simples (if):")

# Exemplo simples de if
numero = 10
if numero > 0:
    print(f"{numero} é positivo.")

# 2. Estrutura if-else (complementando a condição)
print("\n2. Estrutura if-else (complementando a condição):")

# Exemplo de if-else
numero = -5
if numero >= 0:
    print(f"{numero} é positivo ou zero.")
else:
    print(f"{numero} é negativo.")

# 3. Estrutura if-elif-else (várias condições)
print("\n3. Estrutura if-elif-else (várias condições):")

# Exemplo de if-elif-else
idade = 18
if idade < 13:
    print("Você é uma criança.")
elif idade < 18:
    print("Você é um adolescente.")
else:
    print("Você é um adulto.")

# 4. Operador Ternário (condicional inline)
print("\n4. Operador Ternário (condicional inline):")

# Exemplo de operador ternário (O python nao tem ternario)
numero = 10
resultado = "Positivo" if numero > 0 else "Não positivo"
print(f"O número é: {resultado}")

# 5. Estrutura match-case (como o switch-case)
print("\n5. Estrutura match-case (semelhante ao switch-case):")

# Exemplo de match-case (disponível a partir do Python 3.10)
mes = 2
match mes:
    case 1:
        print("Janeiro")
    case 2:
        print("Fevereiro")
    case 3:
        print("Março")
    case _:
        print("Mês desconhecido")

print("\nFim do tutorial!")
