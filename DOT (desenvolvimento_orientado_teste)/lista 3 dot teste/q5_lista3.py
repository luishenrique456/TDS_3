# 5) Escreva uma função que recebe uma lista com n números inteiros, e retorna uma
# lista com a soma cumulativa dos elementos da lista original onde o i-ésimo
# elemento é a soma dos primeiros i+1 elementos da lista original. Ex: [1,2,3] =
# [1,3,6]

def soma_cumulativa(lista_numeros):
    if type(lista_numeros) != list or not all(isinstance(i,int)for i in lista_numeros) or len(lista_numeros) == 0:
        return Exception
    lista_soma = []
    soma = 0
    for i in range(len(lista_numeros)):
        soma += lista_numeros[i]
        lista_soma.append(soma)
    return lista_soma

assert soma_cumulativa([1,2,3]) == [1,3,6]

assert soma_cumulativa(3) == Exception

assert soma_cumulativa(4.6) == Exception

assert soma_cumulativa('a') == Exception

assert soma_cumulativa(['a']) == Exception

assert soma_cumulativa([2.4]) == Exception

assert soma_cumulativa([]) == Exception

print('teste tudo OK! da questão 5 da lista 3')
