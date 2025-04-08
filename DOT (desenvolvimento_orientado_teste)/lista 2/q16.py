# 16) Ler uma lista X de 10 elementos inteiros e positivos. Criar uma lista Y da seguinte forma: os
# elementos de Y com índice par receberão os respectivos elementos de X divididos por 2; os
# elementos com índice ímpar receberão os respectivos elementos de X multiplicados por 3.
# Escrever as listas X e Y.
def ler_lista(n):
    lista_num = []
    for i in range(n):
        num = int(input(f'Digite {i} º um número : '))
        lista_num.append(num)

    return lista_num

def modificar_lista(lista_x):
    lista_par = []
    for i in lista_x:
        if i % 2 == 0:
            lista_par.append(i//2)

    return lista_par

def modificar_lista2(lista_x):
    lista_impar = []
    for i in lista_x:
        if i % 2 != 0:
            lista_impar.append(i*3)

    return lista_impar




def main():
    while True:
        try:
            lista_x = ler_lista(5)
            print(f'Lista Y {modificar_lista(lista_x)}')
            print(f'Lista X {modificar_lista2(lista_x)}')


            break
        except ValueError:
            print('Valor invalidor')





if __name__ == '__main__':
    main()