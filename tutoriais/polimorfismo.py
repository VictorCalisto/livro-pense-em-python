# Tutorial sobre Polimorfismo em Python

# Definição:
# O polimorfismo é um princípio da programação orientada a objetos que permite 
# que diferentes tipos de objetos possam ser tratados como instâncias de um 
# mesmo tipo através de uma interface comum. 
# Em Python, o polimorfismo é comumente alcançado por meio de herança e 
# métodos sobrescritos (overriding).

# Vamos começar com um exemplo simples de polimorfismo.

# Classe base (superclasse)
class Animal:
    def fazer_som(self):
        raise NotImplementedError("O método 'fazer_som' deve ser implementado nas subclasses!")

# Classe derivada 1 (subclasse)
class Cachorro(Animal):
    def fazer_som(self):
        return "Au Au!"

# Classe derivada 2 (subclasse)
class Gato(Animal):
    def fazer_som(self):
        return "Miau!"

# Classe derivada 3 (subclasse)
class Vaca(Animal):
    def fazer_som(self):
        return "Muu!"

# Função que recebe qualquer objeto do tipo Animal
def emitir_som_do_animal(animal: Animal):
    print(animal.fazer_som())

# Criando instâncias das subclasses
cachorro = Cachorro()
gato = Gato()
vaca = Vaca()

# Chamada da função que demonstra o polimorfismo
print("Som do cachorro:")
emitir_som_do_animal(cachorro)

print("Som do gato:")
emitir_som_do_animal(gato)

print("Som da vaca:")
emitir_som_do_animal(vaca)

# Explicação:
# O polimorfismo está presente porque a função 'emitir_som_do_animal' pode 
# trabalhar com objetos de diferentes tipos (Cachorro, Gato, Vaca), mesmo que 
# esses tipos implementem o método 'fazer_som' de maneiras diferentes.

# Em resumo:
# - Cada classe filha (Cachorro, Gato, Vaca) implementa sua própria versão do 
#   método 'fazer_som'.
# - A função 'emitir_som_do_animal' trata todas as subclasses de Animal de forma
#   genérica, demonstrando o conceito de polimorfismo.
