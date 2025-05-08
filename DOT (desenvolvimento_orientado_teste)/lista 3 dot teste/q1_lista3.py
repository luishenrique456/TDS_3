# 1) Escreva uma função que recebe uma lista com n números inteiros, retornar uma
# lista eliminando as repetições. Ex: [5, 4, 5, 7, 3, 4] = [5, 4, 7, 3]

# from random import randint


def gera_lista(n):
    lista_num = []
    for i in range(n):
        num = int(input('Digite um número da lista : '))

        lista_num.append(num)

        # lista_num.append(randint(1,5))

    return lista_num


# print(gera_lista(4))

def del_numeros_rep(lista_num):
    pass




assert gera_lista(4) == [1,2,3,4]

print('teste tudo OK! da questão 1 da lista 3')