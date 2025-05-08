# 18) Ler uma lista X de 10 elementos. A seguir copiar todos os valores negativos da lista X para
# uma lista R, sem deixar elementos vazios entre os valores copiados. Escrever as listas X e R.

def lista_negativo(numeros : list[int]):
    if type(numeros) != list or not all(isinstance(i,int)for i in numeros) or len(numeros) == 0:
        return Exception
    lista_neg = []
    for i in numeros:
        if i < 0:
            lista_neg.append(i)

    return lista_neg

assert lista_negativo([-1,2,3]) == [-1]

assert lista_negativo([2,3,-4,-5,6,-7]) == [-4,-5,-7]

#verficar parâmetro é tipo list

assert lista_negativo(10) == Exception

assert lista_negativo(2.8) == Exception

assert lista_negativo('a') == Exception

assert lista_negativo([]) == Exception

#verficar elemento da list é int

assert lista_negativo(['a']) == Exception

assert lista_negativo([2.4]) == Exception

print('Teste Tudo OK! da questão 18 da lista 2')