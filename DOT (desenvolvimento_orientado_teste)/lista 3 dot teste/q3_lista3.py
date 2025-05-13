# 3) Escreva uma função que recebe uma lista com n números inteiros, e determina a
# maior soma de um segmento com 2 valores. Ex: [5, -2, -2, -7, 3, 15, 10, -3, 9, -6,
# # 4, 1] = 25

def maiores_segmentos(lista_numeros):
    if type(lista_numeros) != list or not all(isinstance(i,int)for i in lista_numeros) or len(lista_numeros) == 0:
        return Exception
    soma_maior = 0
    for i in range(len(lista_numeros)-1):
        soma = lista_numeros[i] + lista_numeros[i+1]
        if soma > soma_maior:
            soma_maior = soma
    return soma_maior


assert maiores_segmentos([1,2,30,4]) == 34

assert maiores_segmentos(1) == Exception

assert maiores_segmentos('a') == Exception

assert maiores_segmentos(2.0) == Exception

assert maiores_segmentos([]) == Exception

assert maiores_segmentos(['a']) == Exception

assert maiores_segmentos([1.9]) == Exception

print('Teste tudo OK! da questão 3 da lista 3')