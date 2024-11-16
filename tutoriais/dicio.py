# tutorial_dicionarios.py

# ===== Introdução aos Dicionários =====
print("===== Introdução aos Dicionários =====")

# Dicionários em Python são coleções de pares chave-valor, onde cada chave é única e está associada a um valor.
# Exemplo de dicionário:
dicionario_exemplo = {
    "nome": "Maria",
    "idade": 28,
    "profissao": "Engenheira"
}

print(f"Dicionário de exemplo: {dicionario_exemplo}")

# ===== Acessando Itens do Dicionário =====
print("\n===== Acessando Itens do Dicionário =====")

# 1. Acessando valores pelo nome da chave
nome = dicionario_exemplo["nome"]
print(f"Nome: {nome}")  # Saída: Maria

# 2. Usando o método get() para acessar valores (caso a chave não exista, retorna None ou um valor padrão)
idade = dicionario_exemplo.get("idade")
print(f"Idade: {idade}")  # Saída: 28

# 3. Acessando valor com chave inexistente com get() (sem gerar erro)
telefone = dicionario_exemplo.get("telefone", "Não disponível")
print(f"Telefone: {telefone}")  # Saída: Não disponível

# ===== Adicionando e Modificando Itens =====
print("\n===== Adicionando e Modificando Itens =====")

# 4. Adicionando um novo par chave-valor
dicionario_exemplo["email"] = "maria@email.com"
print(f"Dicionário após adicionar email: {dicionario_exemplo}")

# 5. Modificando o valor de uma chave existente
dicionario_exemplo["idade"] = 29
print(f"Dicionário após modificar a idade: {dicionario_exemplo}")

# ===== Removendo Itens =====
print("\n===== Removendo Itens =====")

# 6. Removendo um item com `del`
del dicionario_exemplo["profissao"]
print(f"Dicionário após remover 'profissao': {dicionario_exemplo}")

# 7. Usando o método pop() para remover um item e obter seu valor
email_removido = dicionario_exemplo.pop("email")
print(f"Email removido: {email_removido}")  # Saída: maria@email.com
print(f"Dicionário após pop('email'): {dicionario_exemplo}")

# 8. Usando o método popitem() para remover e obter o último item inserido
ultimo_item = dicionario_exemplo.popitem()
print(f"Último item removido com popitem(): {ultimo_item}")
print(f"Dicionário após popitem(): {dicionario_exemplo}")

# 9. Limpar todos os itens com clear()
dicionario_exemplo.clear()
print(f"Dicionário após clear(): {dicionario_exemplo}")  # Dicionário vazio: {}

# ===== Iterando sobre Dicionários =====
print("\n===== Iterando sobre Dicionários =====")

# 10. Iterando pelas chaves
dicionario = {"a": 1, "b": 2, "c": 3}
print("Iterando pelas chaves:")
for chave in dicionario:
    print(chave)

# 11. Iterando pelos valores
print("\nIterando pelos valores:")
for valor in dicionario.values():
    print(valor)

# 12. Iterando pelas chaves e valores
print("\nIterando pelas chaves e valores:")
for chave, valor in dicionario.items():
    print(f"{chave}: {valor}")

# ===== Compreensão de Dicionários =====
print("\n===== Compreensão de Dicionários =====")

# 13. Compreensão de dicionários: criar um dicionário de quadrados
quadrados = {x: x**2 for x in range(5)}
print(f"Dicionário de quadrados: {quadrados}")  # Saída: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# ===== Verificando a Existência de Chaves =====
print("\n===== Verificando a Existência de Chaves =====")

# 14. Verificando se uma chave existe no dicionário com 'in'
existe_chave = "nome" in dicionario_exemplo
print(f"A chave 'nome' existe no dicionário? {existe_chave}")  # Saída: False (dicionário está vazio)

# 15. Verificando se uma chave não existe com 'not in'
existe_chave = "idade" not in dicionario_exemplo
print(f"A chave 'idade' não existe no dicionário? {existe_chave}")  # Saída: True

# ===== Copiando Dicionários =====
print("\n===== Copiando Dicionários =====")

# 16. Usando copy() para criar uma cópia rasa do dicionário
dicionario_copia = dicionario.copy()
print(f"Cópia do dicionário: {dicionario_copia}")

# ===== Dicionários Aninhados =====
print("\n===== Dicionários Aninhados =====")

# 17. Dicionários aninhados (dicionários dentro de dicionários)
dicionario_aninhado = {
    "aluno1": {"nome": "João", "idade": 20},
    "aluno2": {"nome": "Ana", "idade": 22}
}
print(f"Dicionário aninhado: {dicionario_aninhado}")

# Acessando valores em dicionários aninhados
nome_aluno1 = dicionario_aninhado["aluno1"]["nome"]
print(f"Nome do aluno1: {nome_aluno1}")  # Saída: João

# ===== Fim do Tutorial =====
print("\n===== Fim do Tutorial =====")
