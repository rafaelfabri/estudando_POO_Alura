from modelo.Avaliacao import Avaliacao

class Restaurante():

    _restaurantes_ = []

    #MÉTODO ESPECIAL
    #__init__ é um método denominado construtor 
    #sempre que criamos a instancia para construir um objeto ele vai chamar esse metodo construtor
    def __init__(self, nome, categoria):
        #atributos dessa classe
        self._nome = nome
        self._categoria = categoria
        #colocando como privado para mostrar que esse atributo nao deve ser alterado pelo usuario
        self._ativo = False
        self._avaliacao = []


        Restaurante._restaurantes_.append(self)

    #MÉTODO ESPECIAL
    def __str__(self):
        return " {} - {} ".format(self.nome, self.categoria)
    
    #MÉTODO DA CLASS
    @classmethod
    def listar_restaurantes(cls):
        print('{} | {} | {} | {}'.format('Nome'.ljust(25), 'Categoria'.ljust(25), 'Avaliacao'.ljust(25), 'Status'.ljust(25)))
        #for restaurante in Restaurante_2.restaurantes:
        
        for restaurante in cls._restaurantes_:
            print('{} | {} | {} | {}'.format(restaurante._nome.ljust(25), 
                                             restaurante._categoria.ljust(25), 
                                             str(restaurante.media_avaliacao).ljust(25),
                                             restaurante.ativo.ljust(25)))

    #modificar a forma que o arquivo sera lido
    #usar para fazer operacao matematica - agragacao etc
    @property
    def ativo(self):
        return 'ativo' if self._ativo else 'desativado'
    
    #MÉTODO PARA OS OBJETOS
    def alterar_estado(self):
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente: str, nota: float):
        print('a')
        avaliacao = Avaliacao(cliente, nota)
        self._avaliacao.append(avaliacao)

    @property
    def media_avaliacao(self):
        if not self._avaliacao:
            return 0
        soma = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_notas = len(self._avaliacao)
        media = round(soma / quantidade_notas, 1)
        return media