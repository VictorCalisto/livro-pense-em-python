#!/usr/bin/env python3


# tutorial_metodos_string.py

# ===== Métodos de String =====
print("===== Métodos de String em Python =====")

# 1. upper() - Converte todos os caracteres para maiúsculas
texto = "olá mundo"
resultado_upper = texto.upper()
print(f"upper(): {resultado_upper}")  # Saída: "OLÁ MUNDO"

# 2. lower() - Converte todos os caracteres para minúsculas
texto = "OLÁ MUNDO"
resultado_lower = texto.lower()
print(f"lower(): {resultado_lower}")  # Saída: "olá mundo"

# 3. capitalize() - Converte a primeira letra para maiúscula e o restante para minúscula
texto = "olá mundo"
resultado_capitalize = texto.capitalize()
print(f"capitalize(): {resultado_capitalize}")  # Saída: "Olá mundo"

# 4. title() - Converte a primeira letra de cada palavra para maiúscula
texto = "olá mundo python"
resultado_title = texto.title()
print(f"title(): {resultado_title}")  # Saída: "Olá Mundo Python"

# 5. find() - Encontra a primeira ocorrência de uma substring e retorna o índice (se não encontrar, retorna -1)
texto = "olá mundo python"
resultado_find = texto.find("mundo")
print(f"find('mundo'): {resultado_find}")  # Saída: 4 (índice onde "mundo" começa)

# 6. replace() - Substitui uma substring por outra
texto = "olá mundo python"
resultado_replace = texto.replace("python", "programação")
print(f"replace(): {resultado_replace}")  # Saída: "olá mundo programação"

# 7. strip() - Remove espaços em branco no início e no final da string
texto = "  olá mundo python  "
resultado_strip = texto.strip()
print(f"strip(): '{resultado_strip}'")  # Saída: "olá mundo python" (sem os espaços extras)

# 8. split() - Divide a string em uma lista de substrings com base em um delimitador (por padrão, é o espaço em branco)
texto = "olá mundo python"
resultado_split = texto.split()
print(f"split(): {resultado_split}")  # Saída: ['olá', 'mundo', 'python']

# 9. join() - Junta uma lista de strings em uma única string, com um delimitador especificado
lista = ["olá", "mundo", "python"]
resultado_join = " ".join(lista)
print(f"join(): {resultado_join}")  # Saída: "olá mundo python"

# 10. isalpha() - Retorna True se a string contiver apenas letras (sem números ou símbolos)
texto = "olamundo"
resultado_isalpha = texto.isalpha()
print(f"isalpha(): {resultado_isalpha}")  # Saída: True

# 11. isdigit() - Retorna True se a string contiver apenas números
texto = "12345"
resultado_isdigit = texto.isdigit()
print(f"isdigit(): {resultado_isdigit}")  # Saída: True

# 12. isspace() - Retorna True se a string contiver apenas espaços em branco
texto = "    "
resultado_isspace = texto.isspace()
print(f"isspace(): {resultado_isspace}")  # Saída: True

# 13. startswith() - Retorna True se a string começar com a substring especificada
texto = "olá mundo python"
resultado_startswith = texto.startswith("olá")
print(f"startswith('olá'): {resultado_startswith}")  # Saída: True

# 14. endswith() - Retorna True se a string terminar com a substring especificada
texto = "olá mundo python"
resultado_endswith = texto.endswith("python")
print(f"endswith('python'): {resultado_endswith}")  # Saída: True

# 15. count() - Conta o número de vezes que uma substring aparece na string
texto = "olá mundo python python"
resultado_count = texto.count("python")
print(f"count('python'): {resultado_count}")  # Saída: 2

# 16. zfill() - Preenche a string com zeros à esquerda, até o comprimento especificado
texto = "42"
resultado_zfill = texto.zfill(5)
print(f"zfill(5): {resultado_zfill}")  # Saída: "00042"

# 17. format() - Insere valores dentro de uma string, usando placeholders
nome = "Maria"
idade = 30
resultado_format = "Meu nome é {} e eu tenho {} anos.".format(nome, idade)
print(f"format(): {resultado_format}")  # Saída: "Meu nome é Maria e eu tenho 30 anos."

# 18. f-strings (Literal de String formatada) - Uma forma mais simples de usar a interpolação de variáveis
resultado_fstring = f"Meu nome é {nome} e eu tenho {idade} anos."
print(f"f-string: {resultado_fstring}")  # Saída: "Meu nome é Maria e eu tenho 30 anos."

# Fim do Tutorial
print("\n===== Fim do Tutorial =====")
