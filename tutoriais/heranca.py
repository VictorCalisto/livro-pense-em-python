# Tutorial sobre Herança em Python

# HERANÇA SIMPLES

class Animal:
    def __init__(self, nome):
        self.nome = nome

    def falar(self):
        return "O animal faz um som."

class Cachorro(Animal):
    def __init__(self, nome, raca):
        super().__init__(nome)  # Chama o construtor da classe base
        self.raca = raca

    def falar(self):
        return "O cachorro late!"

# Exemplo de herança simples:
cachorro = Cachorro("Rex", "Labrador")
print(f"{cachorro.nome} é um {cachorro.raca} e ele diz: {cachorro.falar()}")

# HERANÇA MÚLTIPLA

class Mamifero:
    def __init__(self, cor):
        self.cor = cor

    def mover(self):
        return "O mamífero se move."

class Aquatico:
    def __init__(self, ambiente):
        self.ambiente = ambiente

    def nadar(self):
        return "O aquático nada!"

# Herança múltipla: A classe Baleia herda de Mamifero e Aquatico
class Baleia(Mamifero, Aquatico):
    def __init__(self, cor, ambiente, nome):
        Mamifero.__init__(self, cor)  # Inicializa a classe Mamifero
        Aquatico.__init__(self, ambiente)  # Inicializa a classe Aquatico
        self.nome = nome

    def falar(self):
        return "A baleia canta!"

# Exemplo de herança múltipla:
baleia = Baleia("Azul", "Oceano", "Willy")
print(f"A {baleia.nome} é uma baleia {baleia.cor} que vive no {baleia.ambiente}.")
print(baleia.mover())  # Método herdado de Mamifero
print(baleia.nadar())  # Método herdado de Aquatico
print(baleia.falar())  # Método sobrescrito na classe Baleia

# SOBRESCRITURA DE MÉTODOS HERDADOS

class Veiculo:
    def __init__(self, modelo):
        self.modelo = modelo

    def acelerar(self):
        return "O veículo está acelerando!"

class Carro(Veiculo):
    def __init__(self, modelo, cor):
        super().__init__(modelo)
        self.cor = cor

    # Sobrescrevendo o método 'acelerar'
    def acelerar(self):
        return f"O carro {self.modelo} de cor {self.cor} está acelerando rapidamente!"

# Exemplo de sobrescrição de métodos:
carro = Carro("Fusca", "azul")
print(carro.acelerar())  # Método acelerado sobrescrito

# HERANÇA DE ATRIBUTOS

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

class Aluno(Pessoa):
    def __init__(self, nome, idade, matricula):
        super().__init__(nome, idade)  # Herda os atributos nome e idade
        self.matricula = matricula

# Exemplo de herança de atributos:
aluno = Aluno("João", 20, "12345")
print(f"Nome: {aluno.nome}, Idade: {aluno.idade}, Matrícula: {aluno.matricula}")

# HERANÇA DE MÉTODOS DE CLASSE

class Empresa:
    nome_empresa = "TechCorp"  # Atributo de classe

    @classmethod
    def mostrar_empresa(cls):
        return f"A empresa é {cls.nome_empresa}"

class Funcionario(Empresa):
    def __init__(self, nome, cargo):
        self.nome = nome
        self.cargo = cargo

    # Acessando o método de classe
    def mostrar_dados(self):
        return f"Funcionário: {self.nome}, Cargo: {self.cargo}, Empresa: {self.mostrar_empresa()}"

# Exemplo de herança de métodos de classe:
funcionario = Funcionario("Carlos", "Desenvolvedor")
print(funcionario.mostrar_dados())  # Chama o método de classe herdado

# POLIMORFISMO: Sobrescrevendo comportamentos e chamadas

class Animal:
    def fazer_som(self):
        return "O animal faz um som."

class Gato(Animal):
    def fazer_som(self):
        return "O gato mia!"

class Passaro(Animal):
    def fazer_som(self):
        return "O pássaro canta!"

# Exemplo de polimorfismo:
def chamar_som(animal):
    print(animal.fazer_som())

gato = Gato()
passaro = Passaro()

# Chamando o mesmo método, mas o comportamento muda dependendo da classe
chamar_som(gato)
chamar_som(passaro)

# FIM DO TUTORIAL SOBRE HERANÇA EM PYTHON
