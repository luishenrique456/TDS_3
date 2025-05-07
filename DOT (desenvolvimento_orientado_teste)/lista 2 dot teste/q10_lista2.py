# 10) Faça um programa que grave uma lista com 15 posições, calcule e mostre:
# a) O maior elemento da lista e em que posição esse elemento se encontra;
# b) O menor elemento da lista e em que posição esse elemento se encontra.


def maior_posicao(numeros : list[int]):
    if type(numeros) != list or len(numeros) == 0 or not all(isinstance(i,int)for i in numeros):
        return Exception
    
    maior = max(numeros)
    posicao_max = numeros.index(max(numeros))
    return (maior , posicao_max)
def menor_posicao(numeros):
    if type(numeros) != list or len(numeros) == 0 or not all(isinstance(i,int)for i in numeros):
        return Exception

    menor = min(numeros)
    posicao_min = numeros.index(min(numeros))
    return (menor , posicao_min)

assert maior_posicao([10,20,50,100]) == (100,3)

assert menor_posicao([1,0,3,2]) == (0,1)

# verficar entrada do parâmetro é do tipo list

assert maior_posicao(2.3) == Exception

assert maior_posicao('a') == Exception

assert maior_posicao(True) == Exception

assert menor_posicao('f') == Exception

assert menor_posicao(False) == Exception

assert menor_posicao(4.0) == Exception

#verficar elemento da list é int
assert maior_posicao([]) == Exception

assert maior_posicao(['']) == Exception

assert maior_posicao([1,'a']) == Exception

assert menor_posicao([2,1.7]) == Exception

assert menor_posicao([]) == Exception

assert menor_posicao(['']) == Exception

assert menor_posicao([3,'f']) == Exception

assert menor_posicao([1.5,3]) == Exception

print('Teste tudo OK da questão 10 da lista 2')