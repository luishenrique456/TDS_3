# 9) Escreva uma função que recebe uma lista com n números inteiros, retornar uma
# lista eliminando todas as ocorrências de valores repetidos. Ex: [5, 4, 5, 7, 3, 4] =
# [7, 3]

def tira_ocorrencia(lista_numeros):
    if type(lista_numeros) != list or not all(isinstance(i,int)for i in lista_numeros) or len(lista_numeros) == 0:
        return Exception
    lista_sem_ocorrencia = []
    for numero in lista_numeros:
        ocorrencia = 0
        for numero_comparacacao in lista_numeros:
            if numero == numero_comparacacao:
                ocorrencia +=1
        if ocorrencia == 1:
            lista_sem_ocorrencia.append(numero)

    return lista_sem_ocorrencia



assert tira_ocorrencia([5,4,5,7,3,4]) == [7,3]

assert tira_ocorrencia(3) == Exception

assert tira_ocorrencia(4.6) == Exception

assert tira_ocorrencia('a') == Exception

assert tira_ocorrencia(['a']) == Exception

assert tira_ocorrencia([2.4]) == Exception

assert tira_ocorrencia([]) == Exception

print('Teste tudo OK! da questão 9 da lista 3')