# tutorial_tuplas.py

# ===== Introdução às Tuplas =====
print("===== Introdução às Tuplas =====")

# Tuplas são coleções ordenadas de itens, semelhantes às listas, mas **imutáveis** (não podem ser alteradas após a criação).
# Elas podem conter diferentes tipos de dados, incluindo números, strings, listas e outras tuplas.

# Exemplo de uma tupla:
tupla_exemplo = (1, 2, 3, 4, 5)
print(f"Tupla de exemplo: {tupla_exemplo}")

# ===== Acessando Elementos da Tupla =====
print("\n===== Acessando Elementos da Tupla =====")

# 1. Acessando elementos por índice
# Como as tuplas são ordenadas, podemos acessar os elementos pelo índice, assim como nas listas.
primeiro_elemento = tupla_exemplo[0]
print(f"Primeiro elemento da tupla: {primeiro_elemento}")  # Saída: 1

# 2. Acessando elementos negativos
# Tuplas, assim como listas, permitem o uso de índices negativos para acessar os elementos a partir do final.
ultimo_elemento = tupla_exemplo[-1]
penultimo_elemento = tupla_exemplo[-2]
print(f"Último elemento da tupla: {ultimo_elemento}")  # Saída: 5
print(f"Penúltimo elemento da tupla: {penultimo_elemento}")  # Saída: 4

# ===== Tuplas com um único elemento =====
print("\n===== Tuplas com um único elemento =====")

# 3. Definindo uma tupla com um único elemento
# Para criar uma tupla com um único item, é necessário colocar uma vírgula após o valor.
tupla_unica = (5,)
print(f"Tupla com um único elemento: {tupla_unica}")  # Saída: (5,)

# Se não colocarmos a vírgula, o Python irá tratar como um valor entre parênteses e não como uma tupla.
nao_e_tupla = (5)
print(f"Não é uma tupla, é um valor: {nao_e_tupla}")  # Saída: 5

# ===== Concatenando e Repetindo Tuplas =====
print("\n===== Concatenando e Repetindo Tuplas =====")

# 4. Concatenando tuplas
# O operador `+` pode ser usado para concatenar duas ou mais tuplas.
tupla1 = (1, 2, 3)
tupla2 = (4, 5, 6)
tupla_concatenada = tupla1 + tupla2
print(f"Tupla concatenada: {tupla_concatenada}")  # Saída: (1, 2, 3, 4, 5, 6)

# 5. Repetindo tuplas
# O operador `*` pode ser usado para repetir uma tupla um determinado número de vezes.
tupla_repetida = (0,) * 4
print(f"Tupla repetida: {tupla_repetida}")  # Saída: (0, 0, 0, 0)

# ===== Verificando Existência de Elementos =====
print("\n===== Verificando Existência de Elementos =====")

# 6. Verificando se um item existe na tupla com `in`
# O operador `in` verifica se um valor está presente na tupla.
existe_elemento = 3 in tupla_exemplo
print(f"O valor 3 está na tupla? {existe_elemento}")  # Saída: True

# 7. Contando a quantidade de ocorrências de um valor
# O método `count()` retorna o número de vezes que um item aparece na tupla.
contagem = tupla_exemplo.count(2)
print(f"Quantidade de vezes que o número 2 aparece na tupla: {contagem}")  # Saída: 1

# ===== Desempacotamento de Tuplas =====
print("\n===== Desempacotamento de Tuplas =====")

# 8. Desempacotando tuplas
# Podemos desempacotar uma tupla diretamente para várias variáveis, desde que o número de variáveis seja igual ao número de elementos da tupla.
a, b, c, d, e = tupla_exemplo
print(f"Valores desempacotados: {a}, {b}, {c}, {d}, {e}")  # Saída: 1, 2, 3, 4, 5

# 9. Desempacotamento com asterisco (*)
# Podemos usar o asterisco `*` para pegar múltiplos elementos ao mesmo tempo.
# Exemplo: Pegar os dois primeiros elementos e o restante em outra variável.
primeiro, segundo, *resto = tupla_exemplo
print(f"Primeiro: {primeiro}, Segundo: {segundo}, Resto: {resto}")  # Saída: 1, 2, [3, 4, 5]

# ===== Tupla como chave de um Dicionário =====
print("\n===== Tupla como chave de um Dicionário =====")

# 10. Tupla pode ser usada como chave de dicionário
# Dicionários em Python exigem que as chaves sejam imutáveis. Como as tuplas são imutáveis, elas podem ser usadas como chaves.
dicionario = {tupla_exemplo: "Valores importantes"}
print(f"Dicionário com tupla como chave: {dicionario}")

# ===== Tuplas e Imutabilidade =====
print("\n===== Tuplas e Imutabilidade =====")

# 11. Tuplas são imutáveis
# Uma das características mais importantes das tuplas é que elas são imutáveis.
# Ou seja, não podemos alterar, adicionar ou remover elementos após a criação da tupla.

try:
    tupla_exemplo[0] = 10  # Tentativa de alteração de valor
except TypeError as e:
    print(f"Erro: {e}")  # Saída: 'tuple' object does not support item assignment

# ===== Fim do Tutorial =====
print("\n===== Fim do Tutorial =====")
