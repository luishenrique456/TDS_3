# 10) Faça um programa que grave uma lista com 15 posições, calcule e mostre:
# a) O maior elemento da lista e em que posição esse elemento se encontra;
# b) O menor elemento da lista e em que posição esse elemento se encontra.
def ler_lista(n):
    lista_numeros = []
    for i in range(n):
        num = int(input(f'Digite um {i+1}º número : '))
        lista_numeros.append(num)
    return lista_numeros

def maior_posicao(numeros):
    maior = max(numeros)
    posicao_max = numeros.index(max(numeros))
    return f'O maior elemento {maior} da lista e em que posição esse elemento se encontra {posicao_max}'
def menor_posicao(numeros):
    menor = min(numeros)
    posicao_min = numeros.index(min(numeros))
    return f'O menor elemento {menor} da lista e em que posição esse elemento se encontra {posicao_min}'



def main():
    while True:
        try:
            lista_a = ler_lista(15)
            print(maior_posicao(lista_a))
            print(menor_posicao(lista_a))


            break
        except ValueError:
            print('Valor invalidor')





if __name__ == '__main__':
    main()