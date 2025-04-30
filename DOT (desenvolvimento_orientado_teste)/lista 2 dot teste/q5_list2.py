def intercalar_lista(listaA,listaB):
    lista_intercalar = []
    for i in range(len(listaA)):
        lista_intercalar.append(listaA[i])
        lista_intercalar.append(listaB[i])
    return lista_intercalar

assert intercalar_lista([1,2,3,4],[7,8,9,10]) == [1,7,2,8,3,9,4,10]

print('Teste tudo OK! da questão 5 da lista 2')