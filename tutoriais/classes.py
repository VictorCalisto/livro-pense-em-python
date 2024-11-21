# tutorial_classes_objetos.py

# 1. Definindo uma Classe e Criando Objetos

class Carro:
    def __init__(self, modelo, cor):
        self.modelo = modelo  # Atributo de instância
        self.cor = cor  # Atributo de instância

    def exibir_informacoes(self):
        print(f"Modelo: {self.modelo}, Cor: {self.cor}")

# Criando objetos da classe Carro
carro1 = Carro("Fusca", "azul")
carro1.exibir_informacoes()  # Saída: Modelo: Fusca, Cor: azul

carro2 = Carro("Civic", "preto")
carro2.exibir_informacoes()  # Saída: Modelo: Civic, Cor: preto


# 2. Atributos de Instância e Método __init__

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome  # Atributo de instância
        self.idade = idade  # Atributo de instância

    def saudacao(self):
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.")

# Criando objetos da classe Pessoa
pessoa1 = Pessoa("Maria", 30)
pessoa1.saudacao()  # Saída: Olá, meu nome é Maria e tenho 30 anos.

pessoa2 = Pessoa("João", 25)
pessoa2.saudacao()  # Saída: Olá, meu nome é João e tenho 25 anos.


# 3. Atributos de Classe

class Carro:
    rodas = 4  # Atributo de classe

    def __init__(self, modelo, cor):
        self.modelo = modelo  # Atributo de instância
        self.cor = cor  # Atributo de instância

    def exibir_informacoes(self):
        print(f"Modelo: {self.modelo}, Cor: {self.cor}, Rodas: {Carro.rodas}")

# Criando objetos da classe Carro
carro1 = Carro("Fusca", "azul")
carro1.exibir_informacoes()  # Saída: Modelo: Fusca, Cor: azul, Rodas: 4

carro2 = Carro("Civic", "preto")
carro2.exibir_informacoes()  # Saída: Modelo: Civic, Cor: preto, Rodas: 4


# 4. Métodos de Classe

class Carro:
    rodas = 4  # Atributo de classe

    def __init__(self, modelo, cor):
        self.modelo = modelo  # Atributo de instância
        self.cor = cor  # Atributo de instância

    @classmethod
    def mudar_rodas(cls, novas_rodas):
        cls.rodas = novas_rodas  # Modifica o atributo de classe

    def exibir_informacoes(self):
        print(f"Modelo: {self.modelo}, Cor: {self.cor}, Rodas: {Carro.rodas}")

# Criando objetos da classe Carro
carro1 = Carro("Fusca", "azul")
carro1.exibir_informacoes()  # Saída: Modelo: Fusca, Cor: azul, Rodas: 4

# Usando o método de classe para mudar o número de rodas
Carro.mudar_rodas(6)

# Verificando se a mudança foi aplicada a todos os objetos
carro2 = Carro("Civic", "preto")
carro2.exibir_informacoes()  # Saída: Modelo: Civic, Cor: preto, Rodas: 6


# 5. Métodos Estáticos

class Calculadora:
    @staticmethod
    def somar(a, b):
        return a + b

    @staticmethod
    def subtrair(a, b):
        return a - b

# Usando os métodos estáticos sem criar instâncias
print("Soma:", Calculadora.somar(5, 3))  # Saída: Soma: 8
print("Subtração:", Calculadora.subtrair(5, 3))  # Saída: Subtração: 2


# 6. Encapsulamento - Acesso aos Atributos

class Pessoa:
    def __init__(self, nome, idade):
        self.__nome = nome  # Atributo privado
        self.idade = idade  # Atributo público

    def obter_nome(self):
        return self.__nome  # Método público para acessar o atributo privado

# Criando uma instância
pessoa = Pessoa("Maria", 30)

# Acessando os atributos
print("Nome:", pessoa.obter_nome())  # Saída: Maria
print("Idade:", pessoa.idade)  # Saída: 30

# Tentativa de acessar o atributo privado diretamente
# Isso gerará um erro porque __nome é privado
# print(pessoa.__nome)  # AttributeError: 'Pessoa' object has no attribute '__nome'




# tutorial_metodos_estaticos_e_de_classe.py

# 1. Diferença entre `staticmethod` e `@classmethod`

# Vamos criar uma classe de exemplo chamada `Produto` para demonstrar os dois tipos de métodos.

class Produto:
    categoria = "Geral"  # Atributo de classe

    def __init__(self, nome, preco):
        self.nome = nome  # Atributo de instância
        self.preco = preco  # Atributo de instância

    # Método Estático (staticmethod)
    @staticmethod
    def aplicar_desconto(preco, desconto):
        """Método estático que aplica um desconto em um preço"""
        return preco * (1 - desconto)

    # Método de Classe (@classmethod)
    @classmethod
    def definir_categoria(cls, nova_categoria):
        """Método de classe que altera o atributo de classe 'categoria'"""
        cls.categoria = nova_categoria


# 2. Exemplo de uso do Método Estático

# Usando o método estático para aplicar um desconto
preco_original = 100
desconto = 0.2
preco_com_desconto = Produto.aplicar_desconto(preco_original, desconto)
print(f"Preço original: {preco_original}")
print(f"Desconto: {desconto * 100}%")
print(f"Preço com desconto: {preco_com_desconto}")  # Saída: Preço com desconto: 80.0


# 3. Exemplo de uso do Método de Classe

# Usando o método de classe para mudar a categoria
Produto.definir_categoria("Eletrônicos")
print(f"Nova categoria de todos os produtos: {Produto.categoria}")  # Saída: Eletrônicos

# Criando instâncias de `Produto` para verificar se a categoria foi alterada
produto1 = Produto("Smartphone", 1500)
produto2 = Produto("Notebook", 5000)

print(f"Categoria de {produto1.nome}: {produto1.categoria}")  # Saída: Eletrônicos
print(f"Categoria de {produto2.nome}: {produto2.categoria}")  # Saída: Eletrônicos


# 4. Diferenças Resumidas:

# Métodos Estáticos (staticmethod)
# - Não recebem o parâmetro `self` ou `cls`.
# - Não podem acessar ou modificar atributos de classe ou de instância.
# - Usados para funções que são relacionadas à classe, mas não precisam acessar seu estado.

# Métodos de Classe (@classmethod)
# - Recebem o parâmetro `cls` (referência à classe).
# - Podem acessar e modificar atributos de classe.
# - Usados para funções que afetam o comportamento da classe como um todo (e não de instâncias específicas).

# 5. Conclusão

# - Use `staticmethod` quando a função não precisar acessar nem instâncias nem atributos de classe.
# - Use `@classmethod` quando a função precisar modificar ou acessar atributos de classe, mas não precisar acessar atributos de instância.
