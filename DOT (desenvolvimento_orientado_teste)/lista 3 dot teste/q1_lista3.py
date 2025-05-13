# 1) Escreva uma função que recebe uma lista com n números inteiros, retornar uma
# lista eliminando as repetições. Ex: [5, 4, 5, 7, 3, 4] = [5, 4, 7, 3]




# def gera_lista(n):
#     lista_num = []
#     for i in range(n):
#         num = int(input('Digite um número da lista : '))

#         lista_num.append(num)



#     return lista_num


# print(gera_lista(4))

def del_numeros_rep(lista_num):
    if type(lista_num) != list or not all(isinstance(i,int)for i in lista_num) or len(lista_num) == 0:
        return Exception
    lista_new = []
    for i in lista_num:
        if i not in lista_new:
            lista_new.append(i)

    return lista_new
    





# assert gera_lista(4) == [1,2,3,4] # testando função se lista for [1,2,3,4]

assert del_numeros_rep([5,4,5,7,3,4]) == [5,4,7,3]

assert del_numeros_rep(3) == Exception

assert del_numeros_rep(4.6) == Exception

assert del_numeros_rep('a') == Exception

assert del_numeros_rep(['a']) == Exception

assert del_numeros_rep([2.4]) == Exception

assert del_numeros_rep([]) == Exception

print('teste tudo OK! da questão 1 da lista 3')