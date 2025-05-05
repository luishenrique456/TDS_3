# 10) Faça um programa que grave uma lista com 15 posições, calcule e mostre:
# a) O maior elemento da lista e em que posição esse elemento se encontra;
# b) O menor elemento da lista e em que posição esse elemento se encontra.


def maior_posicao(numeros):
    maior = max(numeros)
    posicao_max = numeros.index(max(numeros))
    return maior , posicao_max
def menor_posicao(numeros):
    menor = min(numeros)
    posicao_min = numeros.index(min(numeros))
    return (menor , posicao_min)

assert maior_posicao([10,20,50,100]) == (100,3)

assert menor_posicao([1,0,3,2]) == (0,1)

print('Teste tudo OK da questão 10 da lista 2')