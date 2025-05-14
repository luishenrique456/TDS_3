# 7) Escreva uma função que recebe uma lista com n números inteiros, e retorna True
# caso algum elemento apareça mais de uma vez ou False caso nenhum elemento
# apareça mais de uma vez. Ex [1, 2, 3, 1] = True. Ex. [3, 7, 2, 4] = False

def verificar_numero_rep(lista_original):
    if type(lista_original) != list or not all(isinstance(i,int)for i in lista_original) or len(lista_original) == 0:
        return Exception
    lista_new = []
    for i in range(len(lista_original)):
        if lista_original[i] in lista_new:
            return True
        else:
            lista_new.append(lista_original[i])
    return False

assert verificar_numero_rep([1,2,3,1]) == True

assert verificar_numero_rep([3,7,2,4]) == False

assert verificar_numero_rep(3) == Exception

assert verificar_numero_rep(4.6) == Exception

assert verificar_numero_rep('a') == Exception

assert verificar_numero_rep(['a']) == Exception

assert verificar_numero_rep([2.4]) == Exception

assert verificar_numero_rep([]) == Exception

print('Teste tudo OK! da questão 7 da lista 3')