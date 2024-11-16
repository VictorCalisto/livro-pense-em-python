#!/usr/bin/env python3


# Simulando um 'do-while' em Python
contador = 0

while True:
    print(contador)
    contador += 1  # Incrementa o contador

    # Condição para continuar ou parar o loop
    if contador >= 5:
        break  # Interrompe o loop quando a condição é satisfeita
