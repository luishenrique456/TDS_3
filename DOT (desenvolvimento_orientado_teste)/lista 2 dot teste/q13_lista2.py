# 13) Tentando descobrir se um dado era viciado, um dono de cassino honesto (ha! ha! ha! ha!) o
# lançou n vezes. Dados os n resultados dos lançamentos, determinar o número de ocorrências de
# cada face.
def ocorrencia(lista_dado : list[int], face1 : int):
    if type(lista_dado) != list or not all(isinstance(i,int) and i >= 0  for i in lista_dado) or len(lista_dado) == 0:
        return Exception
    if type(face1) != int:
        return Exception


    cont = 0
    for i in lista_dado:
        if i == face1:
            cont +=1
    return cont

assert ocorrencia([3, 5, 3, 6, 2],3) == 2

#verficar parâmetro é tipo list função ocorrencia(lista_dado : list[int], face1 : int)
assert ocorrencia(2,3) == Exception

assert ocorrencia(3.5,4) == Exception

assert ocorrencia('a',5) == Exception

assert ocorrencia([],6) == Exception

assert ocorrencia(False,7) == Exception

assert ocorrencia([1],'a') == Exception

assert ocorrencia([4],3.0) == Exception

assert ocorrencia([10],True) == Exception


#verficar elemento da list é int

assert ocorrencia(['a'],4) == Exception

assert ocorrencia([-1],5) == Exception

assert ocorrencia([3.5],3) == Exception

assert ocorrencia([''],6) == Exception


print('teste tudo OK! da questão 13 da lista 2')
