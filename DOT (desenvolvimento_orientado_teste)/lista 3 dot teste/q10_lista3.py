# 10)Escreva uma função que recebe uma lista com n números inteiros, e determina a
# maior soma dos números que se repetem da lista. Ex: [5, -2, -2, 5, 3, 5, 10, -2, 3,
# 10, 3, 1] = 20

def maior_somar_repetem(lista_numeros):
    if type(lista_numeros) != list or not all(isinstance(i,int)for i in lista_numeros) or len(lista_numeros) == 0:
        return Exception

    maior_soma = lista_numeros[0]
    
    for numero in lista_numeros:
        ocorrecia = 0
        soma = 0
        for numero_repetido in lista_numeros:
            if numero == numero_repetido:

                ocorrecia += 1
                soma += numero_repetido

            if soma > maior_soma:
                maior_soma = soma

    return maior_soma




assert maior_somar_repetem([5,-2,-2,5,3,5,10,-2,3,10,3,1]) == 20

assert maior_somar_repetem(3) == Exception

assert maior_somar_repetem(4.6) == Exception

assert maior_somar_repetem('a') == Exception

assert maior_somar_repetem(['a']) == Exception

assert maior_somar_repetem([2.4]) == Exception

assert maior_somar_repetem([]) == Exception

print('Teste tudo ok! da questão 10 da lista 3')