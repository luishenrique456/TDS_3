# 16) Ler uma lista X de 10 elementos inteiros e positivos. Criar uma lista Y da seguinte forma: os
# elementos de Y com índice par receberão os respectivos elementos de X divididos por 2; os
# elementos com índice ímpar receberão os respectivos elementos de X multiplicados por 3.
# Escrever as listas X e Y.

def modificar_lista(lista_x):
    if type(lista_x) != list or not all(isinstance(i,int)for i in lista_x) or len(lista_x) == 0:
        return Exception

    lista_y = []
    for i in range(len(lista_x)):
        if i % 2 == 0:
            lista_y.append(lista_x[i]//2)
        else:
            lista_y.append(lista_x[i]*3)


    return lista_y

assert modificar_lista([1, 8, 6, 7, 6]) == [0, 24, 3, 21, 3]

#verficar parâmetro é tipo list

assert modificar_lista('a') == Exception

assert modificar_lista(3.7) == Exception

assert modificar_lista(2) == Exception

#verficar elemento da list é int

assert modificar_lista(['a']) == Exception

assert modificar_lista([4.6]) == Exception

assert modificar_lista(['']) == Exception

assert modificar_lista([]) == Exception

print('Teste tudo Ok! da questão 16 da lista 2')