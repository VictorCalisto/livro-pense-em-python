# Tutorial de Conversão de Tipos em Python

# Exemplo 1: Conversão de String para Inteiro
# Vamos ler uma string do usuário e convertê-la para inteiro.

entrada_usuario = input("Digite um número inteiro: ")  # Recebe uma string do usuário
try:
    numero_inteiro = int(entrada_usuario)  # Converte a string para inteiro
    print(f"O número inteiro é: {numero_inteiro}")
except ValueError:
    print("Erro: A entrada não é um número válido!")

# Exemplo 2: Conversão de Inteiro para String
# Agora, vamos pegar um número inteiro e convertê-lo para uma string.

numero = 10  # Definindo um número inteiro
numero_como_string = str(numero)  # Converte o número para string
print(f"O número como string é: {numero_como_string}")

# Exemplo 3: Conversão de String para Float
# Vamos pedir para o usuário inserir um número decimal e convertê-lo para float.

entrada_decimal = input("Digite um número decimal: ")  # Recebe uma string do usuário
try:
    numero_decimal = float(entrada_decimal)  # Converte a string para float
    print(f"O número decimal é: {numero_decimal}")
except ValueError:
    print("Erro: A entrada não é um número válido!")

# Exemplo 4: Conversão de Float para Inteiro
# Vamos pegar um número decimal (float) e convertê-lo para inteiro (a parte decimal será descartada).

numero_decimal = 3.14  # Número decimal
numero_como_inteiro = int(numero_decimal)  # Converte o float para inteiro (parte decimal é descartada)
print(f"O número inteiro (sem parte decimal) é: {numero_como_inteiro}")

# Exemplo 5: Conversão de Inteiro para Float
# Agora, vamos pegar um número inteiro e convertê-lo para float.

numero_inteiro = 5  # Número inteiro
numero_como_float = float(numero_inteiro)  # Converte o inteiro para float
print(f"O número como float é: {numero_como_float}")

# Exemplo 6: Conversão de String para Booleano
# Vamos mostrar como converter uma string para booleano. Strings vazias são convertidas para False, qualquer outra coisa para True.

entrada_booleana = input("Digite algo para testar a conversão para booleano: ")
# Converte a string para booleano (uma string vazia se torna False)
valor_booleano = bool(entrada_booleana)  
print(f"O valor booleano de '{entrada_booleana}' é: {valor_booleano}")

# Exemplo 7: Conversão de Booleano para String
# Aqui, vamos mostrar como converter um valor booleano para string.

valor_booleano = True  # Valor booleano
valor_como_string = str(valor_booleano)  # Converte o booleano para string
print(f"O valor booleano como string é: '{valor_como_string}'")

# Exemplo 8: Tratamento de Erros durante a Conversão
# Vamos mostrar como usar try/except para lidar com erros de conversão.

entrada = input("Digite um número para testar a conversão (inteiro ou decimal): ")
try:
    numero = float(entrada)  # Tenta converter a entrada para float
    print(f"O número convertido é: {numero}")
except ValueError:
    print("Erro: A entrada não é um número válido!")

# Fim do tutorial de conversão de tipos em Python.
