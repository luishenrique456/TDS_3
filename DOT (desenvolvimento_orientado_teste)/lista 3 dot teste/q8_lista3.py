# 8) Escreva uma função que recebe uma lista com n números inteiros, e retorna o valor
# mais próximo da média de valores da lista. Ex [2.5, 7.5, 10.0, 4.0] = 7.5

def proximo_media(lista_numeros):
    if type(lista_numeros) != list or not all(isinstance(i,float)for i in lista_numeros) or len(lista_numeros) == 0:
        return Exception
    media = sum(lista_numeros) / len(lista_numeros)
    for i in range(len(lista_numeros)):
        if lista_numeros[i] > media:
            return lista_numeros[i]






assert proximo_media([2.5,7.5,10.0,4.0]) == 7.5

assert proximo_media(3) == Exception

assert proximo_media(4.6) == Exception

assert proximo_media('a') == Exception

assert proximo_media(['a']) == Exception

assert proximo_media([2]) == Exception

assert proximo_media([]) == Exception

print('Teste tudo OK! da questão 8 da lista 3')