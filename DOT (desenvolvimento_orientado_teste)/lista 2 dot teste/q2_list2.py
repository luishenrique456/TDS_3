# 2) Faça um programa que grave uma lista com dez números reais, calcule e mostre a quantidade
# de números negativos e a soma dos números positivos dessa lista.

def conta_negativo(numeros : list[int])-> int:
    if type(numeros) != list or not all(isinstance(i,int)for i in numeros):
        return Exception
    cont_neg = 0
    for i in range(len(numeros)):
        if numeros[i] < 0:
            cont_neg += 1

    return cont_neg

def somar_lista(numeros):
    if type(numeros) != list or not all(isinstance(i,int)for i in numeros):
        return Exception
    cont = 0
    for i in numeros:
        if i > 0:
            cont += i
    return cont

assert conta_negativo([1,2,-3,5,-4]) == 2

assert somar_lista([1,2,-3,5,-4]) == 8

#verficar parâmetro é tipo list

assert conta_negativo('a') == Exception

assert somar_lista(True) == Exception

#verficar elemento da list é int

assert conta_negativo([1,'2']) == Exception

assert somar_lista([2,3.4]) == Exception


print('Teste tudo OK! da questão 2 da lista 2')