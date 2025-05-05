# 4) Faça um programa que grave uma lista com 15 posições, calcule e mostre:
# a) O maior elemento da lista e em que posição esse elemento se encontra;
# b) O menor elemento da lista e em que posição esse elemento se encontra.

def maior(numeros : list[int]):
    if type(numeros) != list or not all(isinstance(i,int)for i in numeros):
        return Exception
    maior_num = max(numeros)
    posicao_maior = numeros.index(max(numeros))
    return maior_num , posicao_maior

def menor(numeros):
    if type(numeros) != list or not all(isinstance(i,int)for i in numeros):
        return Exception
    menor_num = min(numeros)
    posicao_menor = numeros.index(min(numeros))
    return (menor_num , posicao_menor)


assert maior([2,30,4,5]) == (30 , 1)

assert menor([2,30,4,5]) == (2,0)

#verficar parâmetro é tipo list

assert maior('a') == Exception

assert menor('b') == Exception

#verficar elemento da list é int

assert maior([1,'a']) == Exception

assert menor([2,3.4]) == Exception

print('Teste tudo OK! da questão 4 da lista 2')