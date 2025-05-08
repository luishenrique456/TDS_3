# 19) Ler duas listas: R de 5 elementos e S de 10 elementos. Gerar uma lista X de 15 elementos
# cujas 5 primeiras posições contenham os elementos de R e as 10 últimas posições, os elementos
# de S. Escrever a lista X.

def juntar(lista1,lista2):
    if type(lista1) != list or not all(isinstance(i,int)for i in lista1) or len(lista1) == 0:
        return Exception
    if type(lista2) != list or not all(isinstance(i,int)for i in lista2) or len(lista2) == 0:
        return Exception
    return lista1 + lista2

assert juntar([1,2,3,4],[5,6,7,8]) == [1,2,3,4,5,6,7,8]

#verficar parâmetro é tipo list

assert juntar(2.0,[]) == Exception

assert juntar(1,[3]) == Exception

assert juntar([2],1) == Exception

assert juntar('a',2.4) == Exception

assert juntar([3],'b') == Exception

assert juntar([4],4.6) == Exception

assert juntar([5],[]) == Exception

#verficar elemento da list é int

assert juntar(['a'],['1']) == Exception

assert juntar([1.2],[3]) == Exception

assert juntar([],[]) == Exception

assert juntar(['s'],[7]) == Exception

assert juntar([1],[2.5]) == Exception

print('Teste Tudo OK! da questão 19 da lista 2')