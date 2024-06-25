#Classe Restaurante
class Restaurante():

    #atributos dessa classe
    nome = ''
    categoria = ''
    ativo = False


#um objeto é uma instancia de uma classe
restaurante_praca = Restaurante()
restaurante_praca.nome = 'Praça'
restaurante_praca.categoria = 'Gourmet'

restaurante_pizza = Restaurante()

restaurantes = [restaurante_pizza, restaurante_praca]

print('Local em memória = ',restaurantes)

print('trazendo todas os atributos dessa classe Restaurante = ',dir(restaurante_praca))

print('dicionario com os atributos dessa classe = ', vars(restaurante_praca))