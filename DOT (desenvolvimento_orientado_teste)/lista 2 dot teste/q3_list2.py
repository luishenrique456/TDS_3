# 3) Faça um programa que dada uma seqüência de n números, imprimi-la na ordem inversa à da
# leitura.

def reverte_num(numeros: list[int])->list[int]:
    if type(numeros) != list or not all(isinstance(i,int) for i in numeros):
        return Exception
    numeros.reverse()
    return numeros

assert reverte_num([1,2,3,4,5]) == [5,4,3,2,1]

#verficar parâmetro é tipo list
assert reverte_num('b') == Exception


#verficar elemento da list é int
assert reverte_num([1,'d']) == Exception

print('Teste tudo Ok! da questão 3 da lista 2')