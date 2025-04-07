# 8) Dada uma lista contendo letras do alfabeto, elabore um programa para verificar quantas vezes
# ocorreu a letra ‘A’.
# OBS: Fazer crítica na entrada do caractere para aceitar somente letras.


def verficar_letra_A():
    cont = 0
    lista_letras = ['B','C','A','A','D']
    for i in lista_letras:
        if i == 'A':
            cont +=1
    return cont 




def main():
    while True:
        try:
            caractere = input('Digite letra "A" :  ').strip().upper()
            if 'B' <= caractere <= 'Z':
                print('Letra invalidor . Digite letra A : ')
            elif caractere == 'A':
                resul = verficar_letra_A()
                print(f'Letra A repetiu : {resul}')
                break
            else:
                print('valor invalidor. Digite novamente')
                


        except ValueError:
            print('Valor invalidor!')





if __name__ == '__main__':
    main()