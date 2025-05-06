# 8) Dada uma lista contendo letras do alfabeto, elabore um programa para verificar quantas vezes
# ocorreu a letra ‘A’.
# OBS: Fazer crítica na entrada do caractere para aceitar somente letras.

def verficar_letra_A(caractere):
    if type(caractere) != str or 'B' <= caractere.upper() <= 'Z':
        return Exception

    cont = 0
    lista_letras = ['B','C','A','A','D']
    for caractere in lista_letras:
        if caractere == 'A':
            cont +=1
        
    return cont 

assert verficar_letra_A('A') == 2

assert verficar_letra_A(1) == Exception

assert verficar_letra_A(3.0) == Exception

assert verficar_letra_A([2]) == Exception

assert verficar_letra_A('B') == Exception

assert verficar_letra_A('C') == Exception

assert verficar_letra_A('R') == Exception

assert verficar_letra_A('r') == Exception

print('teste tudo OK! da questão 8 da lista 2')