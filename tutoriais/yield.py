# tutorial_uso_yield.py

# ===== O que é o `yield`? =====
print("===== O que é o `yield`? =====")

# O `yield` é uma palavra-chave em Python que permite a criação de **geradores**, que são funções especiais que retornam valores de forma preguiçosa (lazy evaluation).
# Quando uma função contém `yield`, ela não retorna imediatamente, mas pausa sua execução, permitindo que o valor seja retornado para o chamador. A execução pode ser retomada mais tarde, do ponto onde foi pausada.

# A principal diferença entre `yield` e `return`:
# - `return`: Retorna um valor e finaliza a execução da função.
# - `yield`: Retorna um valor, mas mantém o estado da função para continuar de onde parou quando chamado novamente.

# Usamos o `yield` quando queremos **gerar valores sob demanda**, sem precisar armazenar todos os valores de uma vez na memória.

# ===== 1. Exemplo Básico de Gerador com `yield` =====
print("\n===== 1. Exemplo Básico de Gerador com `yield` =====")

# Vamos começar com um exemplo simples de um gerador que conta de 1 até um número `n`.

def contador(n):
    count = 1
    while count <= n:
        yield count  # Gera um valor e pausa a execução
        count += 1

# Usando o gerador `contador`
gen = contador(5)

# Vamos percorrer o gerador com um loop:
for numero in gen:
    print(numero)

# Nesse exemplo, o gerador gera os números de 1 a 5, um de cada vez. A função `contador` não retorna todos os valores de uma vez, mas sim um valor por vez, sempre que solicitado.

# ===== 2. Por que Usar o `yield`? =====
print("\n===== 2. Por que Usar o `yield`? =====")

# **Eficiência de Memória**:
# O principal benefício de usar o `yield` é **eficiência de memória**. Quando usamos `yield`, os valores não são armazenados na memória de uma vez, mas gerados conforme necessário.

# Exemplo: Gerar números até 1 milhão
import sys

def contador_grande(n):
    count = 1
    while count <= n:
        yield count  # Gerador que não armazena os valores, apenas gera um a um
        count += 1

# Vamos ver a diferença de memória entre um gerador e uma lista:
gen_grande = contador_grande(1000000)  # Gerador de números de 1 a 1 milhão
print(f"Tamanho do gerador (memória): {sys.getsizeof(gen_grande)} bytes")

# Lista de 1 milhão de elementos
lista_grande = [i for i in range(1, 1000001)]  # Lista que armazena todos os valores na memória
print(f"Tamanho da lista (memória): {sys.getsizeof(lista_grande)} bytes")

# Como podemos ver, o gerador ocupa **muito menos memória** do que a lista, já que ele não precisa armazenar todos os valores.

# ===== 3. Geradores com Expressões Generadoras =====
print("\n===== 3. Geradores com Expressões Generadoras =====")

# Uma **expressão geradora** é uma forma compacta de criar geradores. A sintaxe é similar a uma compreensão de lista, mas usa parênteses ao invés de colchetes.

# Exemplo de expressão geradora:
gen_exp = (x * x for x in range(5))  # Gerador de quadrados de números de 0 a 4

for valor in gen_exp:
    print(valor)

# As expressões geradoras são muito úteis quando você deseja criar um gerador de forma rápida e compacta, sem definir uma função.

# ===== 4. Usando `yield` para Criar Sequências Infinitas =====
print("\n===== 4. Usando `yield` para Criar Sequências Infinitas =====")

# Uma das grandes vantagens do `yield` é a possibilidade de criar sequências infinitas. Como os valores são gerados sob demanda, você pode criar geradores que geram valores infinitos, sem sobrecarregar a memória.

# Exemplo: Gerador que gera números Fibonacci infinitos
def fibonacci():
    a, b = 0, 1
    while True:  # Sequência infinita
        yield a
        a, b = b, a + b

# Vamos testar o gerador de Fibonacci
fib = fibonacci()

for _ in range(10):  # Vamos pegar os primeiros 10 números da sequência Fibonacci
    print(next(fib))

# Aqui, o gerador de Fibonacci nunca termina, mas pode ser interrompido ou utilizado até o número desejado. Ele só gera um número por vez, quando solicitado.

# ===== 5. Usando `yield` com Funções Complexas =====
print("\n===== 5. Usando `yield` com Funções Complexas =====")

# Você também pode usar o `yield` dentro de funções mais complexas para gerar dados de várias fontes ou para processos que envolvem múltiplas etapas.

# Exemplo: Gerador que lê linhas de um arquivo
def ler_linhas_arquivo(nome_arquivo):
    with open(nome_arquivo, 'r') as f:
        for linha in f:
            yield linha.strip()  # Retorna uma linha e pausa a execução

# Suponha que temos um arquivo chamado 'exemplo.txt' com várias linhas.
# Vamos usar o gerador para ler esse arquivo linha por linha:
# (Este código não irá funcionar diretamente aqui, mas seria assim em um script real)
# for linha in ler_linhas_arquivo('exemplo.txt'):
#     print(linha)

# O gerador irá retornar uma linha de cada vez, sem carregar o arquivo inteiro para a memória.

# ===== 6. Usando `yield` com `send()` e `close()` =====
print("\n===== 6. Usando `yield` com `send()` e `close()` =====")

# Além de gerar valores, você também pode **enviar valores de volta** para o gerador usando o método `send()`, o que permite uma interação mais avançada.

# Exemplo: Gerador que recebe valores e os usa para calcular uma soma acumulada
def soma_acumulada():
    total = 0
    while True:
        valor = (yield total)  # Gera o valor acumulado até agora
        if valor is not None:
            total += valor

# Criando o gerador e interagindo com ele
gen_soma = soma_acumulada()

print(next(gen_soma))  # Inicia o gerador e recebe o valor inicial: 0

print(gen_soma.send(5))  # Envia 5 e recebe a soma acumulada: 5
print(gen_soma.send(10))  # Envia 10 e recebe a soma acumulada: 15
print(gen_soma.send(20))  # Envia 20 e recebe a soma acumulada: 35

# O gerador foi interativo: à medida que enviamos valores com `send()`, ele acumula e retorna o novo valor acumulado.

# ===== 7. Usando `yield` com `finally` e `close()` =====
print("\n===== 7. Usando `yield` com `finally` e `close()` =====")

# O `yield` também pode ser usado junto com `finally` para garantir que certos recursos sejam liberados, mesmo quando o gerador for interrompido ou fechado.

# Exemplo: Gerador que simula o uso de um recurso que precisa ser limpo após o uso
def recurso():
    try:
        yield "Recurso aberto"
    finally:
        print("Recurso fechado")

# Usando o gerador
gen_recurso = recurso()
print(next(gen_recurso))  # "Recurso aberto"
gen_recurso.close()  # Isso aciona o `finally` e imprime "Recurso fechado"

# O `finally` é útil quando você precisa garantir que algo seja feito ao final, como liberar recursos ou realizar limpezas.

# ===== Fim do Tutorial =====
print("\n===== Fim do Tutorial =====")


#################################
##### COMPARATIVO DO YIELD ######
######## RUBY VS PYTHON #########

# 1. O que é o yield?
# Ruby:

# No Ruby, o yield é usado para transferir o controle de volta para o bloco que foi passado para o método. O bloco é uma função anônima que pode ser executada dentro do método. O yield permite que você "chame" esse bloco em qualquer ponto da execução do método, e o Ruby espera que o bloco forneça um valor de retorno (quando necessário).
# Python:

# Em Python, o yield é utilizado para criar geradores, ou seja, funções que geram valores sob demanda sem armazená-los na memória. Ele transforma a função em um gerador e, ao invés de retornar um valor de uma vez, ela pode "pausar" sua execução e retomar posteriormente. Isso permite iterar sobre grandes volumes de dados sem precisar carregá-los completamente na memória.

### SAO COISAS TOTALMENTE DIFERENTES ###