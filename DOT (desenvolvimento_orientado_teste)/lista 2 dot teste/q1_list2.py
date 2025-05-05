# 1) Faça um programa que grave uma lista de 100 elementos numéricos inteiros e:
# a) Mostre a quantidade de números pares;
# b) Grave uma lista somente com os números pares e mostre a lista;
# c) Mostre a quantidade de números ímpares;
# d) Grave uma lista somente com os números ímpares e mostre a lista.

def lista_par(list_num : list[int])-> list[int]:
    #verficar função pode recebe do tipo list ou list[int] elemento tem que ser int
    if type(list_num) != list or not all(isinstance(i,int)for i in list_num):
        return Exception

    num_par = []
    num_impar = []
    for i in list_num:
        if  i % 2  == 0:
            num_par.append(i)
        else:
            num_impar.append(i)

    cont_impar = 0

    for i in range(len(num_impar)):
        cont_impar +=1

    cont_par = 0
    for i in range(len(num_par)):
        cont_par += 1

    return num_par , cont_par , num_impar ,cont_impar

assert lista_par([2,3,4,5,6]) == ([2,4,6] , 3 , [3,5] , 2)

#verficar parâmetro é tipo list
assert lista_par('d') == Exception # str

assert lista_par(1) == Exception # int

assert lista_par((1,2)) == Exception # tupla

assert lista_par(2.4) == Exception # float

assert lista_par('') == Exception # str vazia 

assert lista_par(None) == Exception # None

assert lista_par(True) == Exception # bool

assert lista_par({"1":"3"}) == Exception # dict (Dicionário)

#verficar elemento da list é int

assert lista_par([1,'a']) == Exception

assert lista_par([1,2.3]) == Exception

assert lista_par([1,[2]]) == Exception #lista dentro de outra lista

assert lista_par([3,None]) == Exception

assert lista_par([4,'']) == Exception


print('teste tudo OK! da questão 1 da lista 2')