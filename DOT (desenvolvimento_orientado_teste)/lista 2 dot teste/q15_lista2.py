# 15) Ler uma lista D de 10 elementos. Criar uma lista E, com todos os elementos de D na ordem
# inversa, ou seja, o último elemento passará a ser o primeiro, o penúltimo será o segundo e assim
# por diante. Escrever todo a lista D e todo a lista E.

def inverter_lista(lista_d):
    if type(lista_d) != list or not all(isinstance(i,int)for i in lista_d) or len(lista_d) == 0:
        return Exception
    lista_d.reverse()
    return lista_d

assert inverter_lista([1,2,3]) == [3,2,1]

#verficar parâmetro é tipo list

assert inverter_lista('a') == Exception

assert inverter_lista(3.0) == Exception

assert inverter_lista(2) == Exception

#verficar elemento da list é int

assert inverter_lista(['a']) == Exception

assert inverter_lista([3.0]) == Exception

print('Teste tudo Ok! da questão 15 da lista 2')