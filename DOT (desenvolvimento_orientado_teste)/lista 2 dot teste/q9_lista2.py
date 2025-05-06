# 9) Dada uma lista X numérica contendo 5 elementos, fazer um programa que crie e exiba na tela
# uma lista Y. A lista Y deverá conter o mesmo conteúdo da lista X na ordem inversa.
def inverter(listas_num):
    if type(listas_num) != list or len(listas_num) == 0:
        return Exception
    listas_num.reverse()
    return listas_num


assert inverter([8,7,6,5,4,3,2,1]) == [1,2,3,4,5,6,7,8]

# verficar entrada do parâmetro é do tipo list

assert inverter(1) == Exception

assert inverter(3.0) == Exception

assert inverter('a') == Exception

assert inverter([]) == Exception

print('Teste tudo Ok! da questão 9 da lista 2')