# tutorial_tratamento_erros.py

# ===== Introdução ao Tratamento de Erros =====
print("===== Introdução ao Tratamento de Erros =====")

# Em Python, erros são chamados de **exceções**. Quando um erro ocorre, o fluxo normal do programa é interrompido.
# O tratamento de erros é feito com as instruções `try`, `except`, `else` e `finally`.

# A estrutura básica do tratamento de erros é a seguinte:
# try:
#     # código que pode gerar um erro
# except <TipoDeErro>:
#     # código que será executado se o erro ocorrer
# else:
#     # código que será executado se não houver erro
# finally:
#     # código que sempre será executado, com ou sem erro

# ===== 1. A Estrutura Básica do try-except =====
print("\n===== 1. A Estrutura Básica do try-except =====")

# Exemplo simples: Divisão por zero
try:
    x = 10 / 0  # Isso vai gerar um erro: ZeroDivisionError
except ZeroDivisionError:
    print("Erro: Não é possível dividir por zero!")
    
# O código dentro de `except` é executado quando ocorre uma exceção do tipo especificado (neste caso, `ZeroDivisionError`).

# ===== 2. Tratando Múltiplos Erros =====
print("\n===== 2. Tratando Múltiplos Erros =====")

# Podemos ter múltiplos blocos `except` para tratar diferentes tipos de exceções.

try:
    a = int(input("Digite um número: "))
    resultado = 10 / a
except ZeroDivisionError:
    print("Erro: Não é possível dividir por zero!")
except ValueError:
    print("Erro: Você não digitou um número válido!")
except Exception as e:
    print(f"Erro inesperado: {e}")

# Nesse caso, temos 3 blocos `except`: 
# - Um para tratar `ZeroDivisionError`,
# - Outro para tratar `ValueError` (caso o usuário não digite um número),
# - E um para capturar qualquer outro erro genérico.

# ===== 3. O Bloco else =====
print("\n===== 3. O Bloco else =====")

# O bloco `else` é executado se **nenhuma exceção for gerada** no bloco `try`.

try:
    numero = int(input("Digite um número: "))
    resultado = 10 / numero
except ZeroDivisionError:
    print("Erro: Não é possível dividir por zero!")
except ValueError:
    print("Erro: Você não digitou um número válido!")
else:
    print(f"Resultado da divisão: {resultado}")  # Esse código só será executado se não houver erro.

# ===== 4. O Bloco finally =====
print("\n===== 4. O Bloco finally =====")

# O bloco `finally` será executado **sempre**, independentemente de uma exceção ter ocorrido ou não.

try:
    numero = int(input("Digite um número: "))
    resultado = 10 / numero
except ZeroDivisionError:
    print("Erro: Não é possível dividir por zero!")
except ValueError:
    print("Erro: Você não digitou um número válido!")
else:
    print(f"Resultado da divisão: {resultado}")
finally:
    print("Bloco 'finally' sempre executado!")

# Mesmo se ocorrer um erro ou não, a mensagem do `finally` será sempre impressa.

# ===== 5. Levantando Exceções (raise) =====
print("\n===== 5. Levantando Exceções (raise) =====")

# Às vezes, queremos forçar a ocorrência de um erro. Podemos usar a palavra-chave `raise` para isso.

def valida_idade(idade):
    if idade < 0:
        raise ValueError("A idade não pode ser negativa!")
    return True

try:
    idade = int(input("Digite sua idade: "))
    valida_idade(idade)
    print("Idade válida.")
except ValueError as ve:
    print(f"Erro: {ve}")

# Aqui, estamos usando `raise` para gerar uma exceção personalizada quando a idade fornecida for negativa.

# ===== 6. Exceções Personalizadas =====
print("\n===== 6. Exceções Personalizadas =====")

# Podemos criar nossas próprias exceções definindo uma classe que herda da classe base `Exception`.

class IdadeInvalidaError(Exception):
    """Exceção personalizada para idades inválidas"""
    pass

def valida_idade_personalizada(idade):
    if idade < 0:
        raise IdadeInvalidaError("A idade não pode ser negativa!")
    return True

try:
    idade = int(input("Digite sua idade: "))
    valida_idade_personalizada(idade)
    print("Idade válida.")
except IdadeInvalidaError as e:
    print(f"Erro personalizado: {e}")
    
# Criamos a exceção `IdadeInvalidaError` e a usamos no código acima para tratar uma condição específica.

# ===== 7. Exceções em Funções com Parâmetros =====
print("\n===== 7. Exceções em Funções com Parâmetros =====")

# Também podemos passar argumentos para exceções personalizadas.

class SaldoInsuficienteError(Exception):
    def __init__(self, saldo, valor_solicitado):
        self.saldo = saldo
        self.valor_solicitado = valor_solicitado
        super().__init__(f"Saldo insuficiente! Saldo: {saldo}, Valor solicitado: {valor_solicitado}")

def sacar(saldo, valor):
    if saldo < valor:
        raise SaldoInsuficienteError(saldo, valor)
    return saldo - valor

try:
    saldo_atual = 100
    valor_saque = 150
    saldo_atual = sacar(saldo_atual, valor_saque)
except SaldoInsuficienteError as e:
    print(f"Erro: {e}")

# Aqui, a exceção personalizada `SaldoInsuficienteError` é gerada com dois parâmetros: saldo e valor solicitado.

# ===== 8. Usando Tracebacks para Depuração =====
print("\n===== 8. Usando Tracebacks para Depuração =====")

# O módulo `traceback` pode ser utilizado para obter mais detalhes sobre onde e por que ocorreu uma exceção.

import traceback

try:
    x = 10 / 0  # Erro de divisão por zero
except ZeroDivisionError:
    print("Erro: Divisão por zero!")
    traceback.print_exc()  # Exibe o traceback detalhado do erro.

# O `traceback.print_exc()` exibe um traceback detalhado que pode ser muito útil durante o processo de depuração.

# ===== Fim do Tutorial =====
print("\n===== Fim do Tutorial =====")
