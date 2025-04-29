# 18) Ler uma lista X de 10 elementos. A seguir copiar todos os valores negativos da lista X para
# uma lista R, sem deixar elementos vazios entre os valores copiados. Escrever as listas X e R.

from random import randint

def ler_lista(n):
    lista_numero = []
    for i in range(n):
        # num = int(input(f'Digite {i+1} º um número : '))
        lista_numero.append(randint(-10,10))
    return lista_numero

def lista_negativo(numeros : list[int]):
    lista_neg = []
    for i in numeros:
        if i < 0:
            lista_neg.append(i)

    return lista_neg





def main():
    while True:
        try:
            lista_x = ler_lista(10)
            resul_list_neg = lista_negativo(lista_x)
            print(f'Lista X {lista_x}')
            print(f'Lista R {resul_list_neg}')

            break
        except ValueError:
            print('Valor invalidor')





if __name__ == '__main__':
    main()