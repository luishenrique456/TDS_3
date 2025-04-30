def conta_negativo(numeros : list[int])-> int:
    cont_neg = 0
    for i in range(len(numeros)):
        if numeros[i] < 0:
            cont_neg += 1

    return cont_neg

def somar_lista(numeros):
    cont = 0
    for i in numeros:
        if i > 0:
            cont += i
    return cont

assert conta_negativo([1,2,-3,5,-4]) == 2

assert somar_lista([1,2,-3,5,-4]) == 8

print('Teste tudo OK! da questão 2 da lista 2')