# 5) Faça um programa que leia duas listas de 10 elementos numéricos cada um e intercale os
# elementos deste em uma outra lista de 20 elementos.
from random import randint

def ler_lista(numero : int)-> list[int]:
    lista_num = []
    for i in range(numero):
        # num = int(input(f'Digite {i+1}º um número : '))
        lista_num.append(randint(1,5))

    return lista_num

def intercalar_lista(listaA,listaB):
    lista_intercalar = []
    for i in range(len(listaA)):
        lista_intercalar.append(listaA[i])
        lista_intercalar.append(listaB[i])
    return f'Lista A e B intercalada  {lista_intercalar}'


def main():
    while True:
        try:
            listaA = ler_lista(10)
            listaB = ler_lista(10)

            print(f'Lista A {listaA}')

            print(f'Lista B {listaB}')

            intercale = intercalar_lista(listaA,listaB)

            print(intercale)
            break


        except ValueError:
            print('Valor invalidor')





if __name__ == '__main__':
    main()