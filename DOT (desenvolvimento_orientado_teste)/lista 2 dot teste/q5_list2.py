# 5) Faça um programa que leia duas listas de 10 elementos numéricos cada um e intercale os
# elementos deste em uma outra lista de 20 elementos.

def intercalar_lista(listaA,listaB):
    if type(listaA) != list or type(listaB) != list or not all(isinstance(i,int)for i in listaA):
        return Exception
    
    elif not all(isinstance(i,int)for i in listaB):
        return Exception
    
    lista_intercalar = []
    for i in range(len(listaA)):
        lista_intercalar.append(listaA[i])
        lista_intercalar.append(listaB[i])
    return lista_intercalar

assert intercalar_lista([1,2,3,4],[7,8,9,10]) == [1,7,2,8,3,9,4,10]

#verficar parâmetro é tipo list

assert intercalar_lista('a','3') == Exception

assert intercalar_lista('a',[3]) == Exception

assert intercalar_lista([1],'b') == Exception


#verficar elemento da list é int

assert intercalar_lista([1,'a',3],[4,6,5]) == Exception

assert intercalar_lista([1,2,3],['a',3,5]) == Exception


print('Teste tudo OK! da questão 5 da lista 2')