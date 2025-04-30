def maior(numeros : list[int]):
    maior_num = max(numeros)
    posicao_maior = numeros.index(max(numeros))
    return maior_num , posicao_maior

def menor(numeros):
    menor_num = min(numeros)
    posicao_menor = numeros.index(min(numeros))
    return (menor_num , posicao_menor)


assert maior([2,30,4,5]) == (30 , 1)

assert menor([2,30,4,5]) == (2,0)

print('Teste tudo OK! da questão 4 da lista 2')