# questão 11 dot
#Faça uma função que recebe, por parâmetro, um valor inteiro e positivo e retorna o número de divisores desse valor.

#função mostra lista de divisores
def divisore(num:int)-> list[int]:
    if type(num) != int or num <= 0:
        return Exception

    lista_div = []
    for i in range(1,num+1):
        if num % i == 0:
            lista_div.append(i)

    return lista_div

#função mostra quantidade do divisores
def qtd_divisores(num : int)-> int:
    if type(num) != int or num <= 0:
        return Exception

    cont = 0
    for i in range(1,num+1):
        if num % i == 0:
            cont += 1

    return cont

assert divisore(5) == [1,5]

assert qtd_divisores(5) == 2

assert divisore(5.0) == Exception

assert divisore('a') == Exception

assert qtd_divisores('b') == Exception

assert divisore(-1) == Exception

assert qtd_divisores(-2) == Exception

print('teste tudo OK! da questão 11 da lista 1 ')