#!/usr/bin/env python3

#Chamada de função
import math
raiz = math.sqrt(4) # raiz = 2

#Chamar so uma parte da funcao
from math import sqrt
raiz = sqrt(4) # nao pega a math toda, mas o que eu quero.

#chama com um apelido pra facilitar o uso
from math import sqrt as raiz_quadrada
raiz = raiz_quadrada(4) # 2

# cria funcao
def imprime(string):
    print(string)
#observe que nao se usa chaves, mas entretando e obrigado a identar corretamente.
type(imprime) # function

# null no java/c/c++ e mesmo nil do ruby e o mesmo None do python
nil = None
