# 4) Escreva uma função que recebe uma lista com n números inteiros, e determina a
# maior soma de qualquer seguimento da lista. Ex: Ex: [5, -2, -2, -7, 3, 15, 10, -3, 9,
# -6, 4, 1] = 
# lista[i:s]

def maiores_segmentos(lista_numeros):
    if type(lista_numeros) != list or not all(isinstance(i,int)for i in lista_numeros) or len(lista_numeros) == 0:
        return Exception
    soma_maior = lista_numeros[0]
    for i in range(len(lista_numeros)):
        soma = 0
        for s in range(i ,len(lista_numeros)):
            soma += lista_numeros[s]
            if soma > soma_maior:
                soma_maior = soma
    return soma_maior


assert maiores_segmentos([1,2,3,4,30,4,2,3]) == 49

assert maiores_segmentos([5,-2,-2,-7,3,15,10,-3,9,-6,4,1]) == 34

assert maiores_segmentos(3) == Exception

assert maiores_segmentos(4.6) == Exception

assert maiores_segmentos('a') == Exception

assert maiores_segmentos(['a']) == Exception

assert maiores_segmentos([2.4]) == Exception

assert maiores_segmentos([]) == Exception

print('teste tudo OK! da questão 4 da lista 3')