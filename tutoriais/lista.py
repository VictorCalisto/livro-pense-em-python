# tutorial_listas_operacoes.py

# ===== Introdução às Listas =====
print("===== Introdução às Listas =====")

# Listas em Python são coleções ordenadas e mutáveis de itens.
# Elas podem conter diferentes tipos de dados, incluindo números, strings, listas, etc.
# Exemplo básico de lista:
lista_exemplo = [1, 2, 3, 4, 5]
print(f"Exemplo de lista: {lista_exemplo}")

# ===== Operadores com Listas =====
print("\n===== Operadores com Listas =====")

# 1. Operador + (Concatenação de listas)
# O operador + permite juntar duas ou mais listas.
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(f"Concatenação de listas (a + b): {c}")  # Saída: [1, 2, 3, 4, 5, 6]

# 2. Operador * (Repetição de listas)
# O operador * permite repetir uma lista por um número especificado de vezes.
repeticao = [0] * 4
print(f"Repetição da lista [0] * 4: {repeticao}")  # Saída: [0, 0, 0, 0]

# Repetindo uma lista com múltiplos elementos
lista_repetida = [1, 2, 3] * 3
print(f"Repetição da lista [1, 2, 3] * 3: {lista_repetida}")  # Saída: [1, 2, 3, 1, 2, 3, 1, 2, 3]

# ===== Acessando Elementos da Lista =====
print("\n===== Acessando Elementos da Lista =====")

# 3. Acessando elementos por índice
# Podemos acessar elementos da lista usando índices, começando de 0.
primeiro_elemento = lista_exemplo[0]
print(f"Primeiro elemento da lista: {primeiro_elemento}")  # Saída: 1

# 4. Acessando elementos negativos
# Índices negativos começam do final da lista, com -1 sendo o último elemento.
ultimo_elemento = lista_exemplo[-1]
penultimo_elemento = lista_exemplo[-2]
print(f"Último elemento da lista: {ultimo_elemento}")  # Saída: 5
print(f"Penúltimo elemento da lista: {penultimo_elemento}")  # Saída: 4

# ===== Operações Comuns com Listas =====
print("\n===== Operações Comuns com Listas =====")

# 5. Adicionando elementos
# Usamos o método append() para adicionar um item ao final da lista
lista_exemplo.append(6)
print(f"Lista após append(6): {lista_exemplo}")  # Saída: [1, 2, 3, 4, 5, 6]

# 6. Inserindo elementos em uma posição específica
# O método insert() permite inserir um elemento em um índice específico.
lista_exemplo.insert(2, 10)  # Inserir 10 na posição 2
print(f"Lista após insert(2, 10): {lista_exemplo}")  # Saída: [1, 2, 10, 3, 4, 5, 6]

# 7. Removendo elementos
# Usamos o método remove() para remover o primeiro elemento encontrado na lista
lista_exemplo.remove(10)
print(f"Lista após remove(10): {lista_exemplo}")  # Saída: [1, 2, 3, 4, 5, 6]

# 8. Removendo o último elemento
# O método pop() remove o último item da lista e retorna o valor removido
ultimo_valor = lista_exemplo.pop()
print(f"Valor removido com pop(): {ultimo_valor}")  # Saída: 6
print(f"Lista após pop(): {lista_exemplo}")  # Saída: [1, 2, 3, 4, 5]

# 9. Removendo um elemento em um índice específico
# Podemos passar um índice para o método pop() para remover o item dessa posição
valor_removido = lista_exemplo.pop(2)  # Remove o valor na posição 2 (elemento 3)
print(f"Valor removido com pop(2): {valor_removido}")  # Saída: 3
print(f"Lista após pop(2): {lista_exemplo}")  # Saída: [1, 2, 4, 5]

# ===== Listas e Slicing =====
print("\n===== Listas e Slicing =====")

# 10. Utilizando slicing (fatiamento)
# O slicing permite extrair partes de uma lista usando a notação [início:fim:passo]
sub_lista = lista_exemplo[1:4]  # Itens da posição 1 até 3 (não inclui a posição 4)
print(f"Sub-lista com slicing (1:4): {sub_lista}")  # Saída: [2, 4, 5]

# 11. Usando o passo em slicing
# O passo define quantos itens são pulados entre os elementos selecionados
sub_lista_com_passo = lista_exemplo[::2]  # Pega um item a cada 2 posições
print(f"Sub-lista com slicing com passo (2): {sub_lista_com_passo}")  # Saída: [1, 4]

# ===== Compreensão de Listas =====
print("\n===== Compreensão de Listas =====")

# 12. Compreensão de listas (List Comprehension)
# Compreensões de lista são uma maneira concisa de criar listas.
# Por exemplo, criar uma lista com o quadrado de cada número em uma lista existente:
quadrados = [x**2 for x in range(1, 6)]
print(f"Compreensão de lista para quadrados: {quadrados}")  # Saída: [1, 4, 9, 16, 25]

# ===== Ordenação e Reversão de Listas =====
print("\n===== Ordenação e Reversão de Listas =====")

# 13. Ordenando a lista
# O método sort() ordena a lista em ordem crescente (modifica a lista original)
lista_numeros = [5, 3, 8, 6, 2]
lista_numeros.sort()
print(f"Lista ordenada: {lista_numeros}")  # Saída: [2, 3, 5, 6, 8]

# 14. Revertendo a lista
# O método reverse() reverte a ordem dos itens na lista original
lista_numeros.reverse()
print(f"Lista após reverse(): {lista_numeros}")  # Saída: [8, 6, 5, 3, 2]

# ===== Verificando a Existência de Elementos =====
print("\n===== Verificando a Existência de Elementos =====")

# 15. Verificando se um elemento está na lista
# Usamos o operador `in` para verificar se um valor existe na lista
valor_existe = 3 in lista_numeros
print(f"3 está na lista? {valor_existe}")  # Saída: True

# 16. Contando a quantidade de ocorrências de um valor
# O método count() retorna o número de vezes que um elemento aparece na lista
quantidade = lista_numeros.count(5)
print(f"Quantidade de vezes que 5 aparece: {quantidade}")  # Saída: 1

# ===== Fim do Tutorial =====
print("\n===== Fim do Tutorial =====")
