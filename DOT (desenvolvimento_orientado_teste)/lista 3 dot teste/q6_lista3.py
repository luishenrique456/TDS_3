# 6) Escreva uma função que recebe uma lista com n números inteiros, e retorna True
# caso a lista esteja ordenada em ordem ascendente ou False caso não esteja
# ordenada. Ex [1, 2, 3] = True. Ex. [3, 7, 2] = False

def ordem_crescente(lista_numeros):
    if type(lista_numeros) != list or not all(isinstance(i,int)for i in lista_numeros)or len(lista_numeros) == 0:
        return Exception
    for i in range(len(lista_numeros)-1):
        if lista_numeros[i] > lista_numeros[i+1]:
            return False
    return True

assert ordem_crescente([1,2,3]) == True

assert ordem_crescente([3,2,1]) == False

assert ordem_crescente(3) == Exception

assert ordem_crescente(4.6) == Exception

assert ordem_crescente('a') == Exception

assert ordem_crescente(['a']) == Exception

assert ordem_crescente([2.4]) == Exception

assert ordem_crescente([]) == Exception

print('Teste tudo OK! da questão 6 da lista 3')