# 2) Escreva uma função que recebe uma lista com n números inteiros, conta e imprime
# o número de vezes que cada número ocorre na sequência.

def conta_itens_list(lista_numeros,item):
    if type(lista_numeros) != list or not all(isinstance(i,int)for i in lista_numeros) or len(lista_numeros) == 0:
        return Exception
    if type(item) != int:
        return Exception
    ocorrecia = 0
    for i in lista_numeros:
        if i == item:
            ocorrecia += 1
    return ocorrecia

def tira_numero_rep(lista_num):
    if type(lista_num) != list or not all(isinstance(i,int)for i in lista_num) or len(lista_num) == 0:
        return Exception
    
    lista_new = []
    for i in lista_num:
        if i not in lista_new:
            lista_new.append(i)

    return lista_new

def qtd_cada_itens_list(lista_original,numeros):
    if type(lista_original) != list or not all(isinstance(i,int)for i in lista_original) or len(lista_original) == 0:
        return Exception
    elif type(numeros) != list or not all(isinstance(i,int)for i in numeros) or len(numeros) == 0:
        return Exception
    lista_resultado = []
    for i in numeros:
        qtd = conta_itens_list(lista_original,i)
        lista_resultado.append(f'numero {i} sequência {qtd}')

    return lista_resultado





assert conta_itens_list([1,2,3,2,4,4],2) == 2

assert tira_numero_rep([1,2,3,2,4,4]) == [1,2,3,4]

assert qtd_cada_itens_list([1,2,3,2,4,4],[1,2,3,4]) == ['numero 1 sequência 1','numero 2 sequência 2','numero 3 sequência 1','numero 4 sequência 2']

assert conta_itens_list('a',2) == Exception

assert conta_itens_list([2],2.0) == Exception

assert tira_numero_rep(['a']) == Exception

assert tira_numero_rep(2.0) == Exception

assert qtd_cada_itens_list('a',[2]) == Exception

assert qtd_cada_itens_list([1],'a') == Exception

print('teste tudo OK! da questão 2 da lista 3')