# 14) Ler uma lista C de 10 elementos inteiros, trocar todos os valores negativos da lista C por 0.
# Escrever a lista C modificada.
from random import randint

def ler_lista(num):
    lista_num = []
    for i in range(num):
        # numero = int(input(f'Digite {i+1}º um número : '))
        lista_num.append(randint(-10,10))
    return lista_num

def mundar_valor_neg(numeros : list[int])-> list[int]:
    
    for i in range(len(numeros)):
        if numeros[i] < 0:
            numeros[i]= 0
    return numeros



def main():
    while True:
        try:
            listas_numeros = ler_lista(10)
            resul = mundar_valor_neg(listas_numeros)
            print(resul)

            break
        except ValueError:
            print('Valor invalidor')





if __name__ == '__main__':
    main()