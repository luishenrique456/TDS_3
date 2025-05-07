# 14) Ler uma lista C de 10 elementos inteiros, trocar todos os valores negativos da lista C por 0.
# Escrever a lista C modificada.




def mundar_valor_neg(numeros : list[int])-> list[int]:
    if type(numeros) != list or not all(isinstance(i,int)for i in numeros) or len(numeros) == 0:
        return Exception
    for i in range(len(numeros)):
        if numeros[i] < 0:
            numeros[i]= 0
    return numeros

assert mundar_valor_neg([1,2,-3]) == [1,2,0]

assert mundar_valor_neg([-1,2,4,5,-3]) == [0,2,4,5,0]

assert mundar_valor_neg([1,-1,2]) == [1,0,2]

#verficar parâmetro é tipo list

assert mundar_valor_neg('a') == Exception

assert mundar_valor_neg(3.4) == Exception

assert mundar_valor_neg(1) == Exception

assert mundar_valor_neg([]) == Exception

assert mundar_valor_neg(True) == Exception


#verficar elemento da list é int

assert mundar_valor_neg(['a']) == Exception

assert mundar_valor_neg([2.5]) == Exception

assert mundar_valor_neg([bool]) == Exception

print('Teste tudo OK! da questão 14 da lista 2')