#!/usr/bin/env python3

# tutorial_manipulacao_arquivos.py

# ===== Abertura e Fechamento de Arquivos =====
print("===== Abertura e Fechamento de Arquivos =====")

# Abrindo um arquivo para leitura
# O modo 'r' abre o arquivo apenas para leitura
try:
    arquivo = open('exemplo.txt', 'r')  # Tente abrir um arquivo que já exista
    print("Arquivo aberto com sucesso!")
    # Lendo o conteúdo do arquivo
    conteudo = arquivo.read()
    print("Conteúdo do arquivo:")
    print(conteudo)  # Exibe o conteúdo do arquivo
finally:
    # Fechando o arquivo depois de usá-lo
    arquivo.close()
    print("\nArquivo fechado.")


# ===== Criando e Escrevendo em Arquivos =====
print("\n===== Criando e Escrevendo em Arquivos =====")

# Abrindo ou criando um arquivo para escrita
# O modo 'w' cria o arquivo (se não existir) e sobrescreve seu conteúdo se já existir
with open('exemplo_escrita.txt', 'w') as arquivo:
    arquivo.write("Este é um arquivo de exemplo para escrita.\n")
    arquivo.write("Python é uma linguagem muito poderosa!\n")
    print("Texto escrito com sucesso no arquivo!")

# Também podemos usar 'a' (append) para adicionar texto sem sobrescrever o conteúdo existente
with open('exemplo_escrita.txt', 'a') as arquivo:
    arquivo.write("Esta linha foi adicionada ao final do arquivo.\n")
    print("Texto adicionado ao final do arquivo com sucesso!")

# ===== Lendo Arquivo Linha por Linha =====
print("\n===== Lendo Arquivo Linha por Linha =====")

# O modo 'r' é usado para ler o conteúdo do arquivo
try:
    with open('exemplo_escrita.txt', 'r') as arquivo:
        print("Lendo o arquivo linha por linha:")
        for linha in arquivo:
            print(linha.strip())  # strip() remove os espaços em branco do início e final
except FileNotFoundError:
    print("O arquivo não foi encontrado.")

# ===== Manipulação de Arquivos com JSON =====
print("\n===== Manipulação de Arquivos com JSON =====")

import json

# Vamos criar um dicionário para salvar em um arquivo JSON
dados = {
    "nome": "João",
    "idade": 30,
    "profissao": "Desenvolvedor"
}

# Escrevendo um arquivo JSON
with open('dados.json', 'w') as arquivo_json:
    json.dump(dados, arquivo_json, indent=4)
    print("Dados JSON escritos com sucesso!")

# Lendo um arquivo JSON
try:
    with open('dados.json', 'r') as arquivo_json:
        dados_lidos = json.load(arquivo_json)
        print("\nDados lidos do arquivo JSON:")
        print(dados_lidos)
except FileNotFoundError:
    print("O arquivo JSON não foi encontrado.")

# ===== Manipulação de Arquivos CSV =====
print("\n===== Manipulação de Arquivos CSV =====")

import csv

# Dados para um arquivo CSV
dados_csv = [
    ["Nome", "Idade", "Profissão"],
    ["Ana", 28, "Designer"],
    ["Carlos", 35, "Engenheiro"],
    ["Mariana", 22, "Estudante"]
]

# Escrevendo em um arquivo CSV
with open('pessoas.csv', 'w', newline='') as arquivo_csv:
    escritor = csv.writer(arquivo_csv)
    escritor.writerows(dados_csv)
    print("Dados CSV escritos com sucesso!")

# Lendo um arquivo CSV
try:
    with open('pessoas.csv', 'r') as arquivo_csv:
        leitor = csv.reader(arquivo_csv)
        print("\nConteúdo do arquivo CSV:")
        for linha in leitor:
            print(linha)
except FileNotFoundError:
    print("O arquivo CSV não foi encontrado.")


# ===== Manipulação de Arquivos com Dados Binários =====
print("\n===== Manipulação de Arquivos Binários =====")

# Escrevendo dados binários em um arquivo
dados_binarios = bytes([120, 3, 255, 0, 100, 255])
with open('dados_binarios.bin', 'wb') as arquivo_binario:
    arquivo_binario.write(dados_binarios)
    print("Dados binários escritos com sucesso!")

# Lendo dados binários de um arquivo
try:
    with open('dados_binarios.bin', 'rb') as arquivo_binario:
        dados_lidos_binarios = arquivo_binario.read()
        print("\nDados binários lidos do arquivo:")
        print(dados_lidos_binarios)
except FileNotFoundError:
    print("O arquivo binário não foi encontrado.")


# ===== Trabalhando com Arquivos Temporários =====
print("\n===== Trabalhando com Arquivos Temporários =====")

import tempfile

# Criando um arquivo temporário
with tempfile.NamedTemporaryFile(delete=False) as arquivo_temporario:
    arquivo_temporario.write(b"Este é um arquivo temporário criado em Python.")
    print(f"Arquivo temporário criado: {arquivo_temporario.name}")

# O arquivo temporário não será apagado automaticamente quando o bloco for concluído, já que `delete=False` foi usado


# Fim do Tutorial
print("\n===== Fim do Tutorial =====")
