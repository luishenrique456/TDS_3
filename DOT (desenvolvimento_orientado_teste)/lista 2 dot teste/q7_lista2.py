# 7) Dada uma lista contendo 10 elementos numéricos, elabore um programa que verifique se um
# outro valor dado pertence ou não à lista.
def verficar_valor(num):
    if type(num) != int:
        return Exception
    lista_numeros = [1,20,3,-4,5,30,60,44,33,9]
    if num in lista_numeros:
        return f'Seu número estar na lista {num}'
    else:
        return f'Seu número não estar na lista {num}'

assert verficar_valor(5) == 'Seu número estar na lista 5'

assert verficar_valor(45) == 'Seu número não estar na lista 45'

assert verficar_valor(-4) == 'Seu número estar na lista -4'

# verficar entrada do parâmetro é do tipo int

assert verficar_valor(3.0) == Exception

assert verficar_valor('s') == Exception

assert verficar_valor([1,2,3]) == Exception

print('teste tudo Ok! da questão 7 da lista 2')