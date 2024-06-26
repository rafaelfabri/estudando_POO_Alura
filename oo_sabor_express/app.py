from modelo.restaurante_final import Restaurante

def main():
    restaurante_praca = Restaurante('praca', 'gourmet')
    restaurante_mex = Restaurante('Mexican Food', 'Mexicana')
    restaurante_japa = Restaurante('Japa', 'Japonesa')

    restaurante_praca.receber_avaliacao('Rafa', 10)
    restaurante_praca.receber_avaliacao('Mah', 5)

    restaurante_praca.listar_restaurantes()
    #restaurante_praca.receber_avaliacao('Mah', 6)



if __name__=='__main__':
    main()