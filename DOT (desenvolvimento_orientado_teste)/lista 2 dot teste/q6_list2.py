# 6) Dadas duas listas, uma contendo a quantidade e a outra o preço de 20 produtos, elabore um
# programa que calcule e exiba o faturamento que é igual a quantidade x preço. Calcule e exiba
# também o faturamento total que é o somatório de todos os faturamentos, a média dos faturamentos
# e quantos faturamentos estão abaixo da média.

def faturamento(lista_qtd : list[int],lista_preco: list[int,float])-> list[int]:
    if type(lista_qtd) != list or type(lista_preco) != list:
        return Exception
    elif not all(isinstance(i,int) and i >= 0 for i in lista_qtd):
        return Exception
    elif not all(isinstance(i,(int,float)) and i >= 0 for i in lista_preco):
        return Exception
    elif len(lista_qtd) == 0 or len(lista_preco) == 0:
        return Exception

    lista_faturamento = []
    for i in range(len(lista_qtd)):
        lista_faturamento.append(lista_qtd[i]*lista_preco[i])
    
    return lista_faturamento

def faturamento_total(lista_qtd,lista_preco):
    if type(lista_qtd) != list or type(lista_preco) != list:
        return Exception
    elif not all(isinstance(i,int) and i >= 0 for i in lista_qtd):
        return Exception
    elif not all(isinstance(i,(int,float))and i >= 0 for i in lista_preco):
        return Exception
    elif len(lista_qtd) == 0 or len(lista_preco) == 0:
        return Exception


    cont = 0
    lista_faturamento = faturamento(lista_qtd,lista_preco)
    for i in lista_faturamento:
        cont += i
    return cont
    
def media_faturamento(lista_qtd,lista_preco):
    if type(lista_qtd) != list or type(lista_preco) != list:
        return Exception
    elif not all(isinstance(i,int) and i >= 0 for i in lista_qtd):
        return Exception
    elif not all(isinstance(i,(int,float)) and i >= 0 for i in lista_preco):
        return Exception
    elif len(lista_qtd) == 0 or len(lista_preco) == 0:
        return Exception

    #calcular media
    somar = faturamento_total(lista_qtd,lista_preco)
    media = somar / len(lista_qtd)
    

    lista_faturamento = faturamento(lista_qtd,lista_preco)
    cont_med = 0
    for i in lista_faturamento:
        if i < media:
            cont_med += 1
    return media,cont_med
    
assert faturamento([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19],[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]) == [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361]

assert faturamento_total([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19],[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]) == 2470

assert media_faturamento([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19],[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]) == (123.5,12)

assert faturamento([1,2,3,4],[2.0,4.0,5.0,1.5]) == [2,8,15,6]

#verficar parâmetro é tipo list

assert faturamento('s',[3]) == Exception

assert faturamento([2],'a') == Exception

assert faturamento_total([3],'f') == Exception

assert faturamento_total('2',[4]) == Exception

assert media_faturamento('w',[5]) == Exception

assert media_faturamento([6],'g') == Exception

#verficar elemento da list é lista_qtd[int] e lista_preco[int ou float]

assert faturamento(['a'],[2]) == Exception

assert faturamento([1.5],[2]) == Exception

assert faturamento([],[2]) == Exception

assert faturamento([3],[]) == Exception

assert faturamento([-1],[4]) == Exception 

assert faturamento([2],[-4.0]) == Exception

assert faturamento_total([-1],[4]) == Exception

assert faturamento_total([2],[-4]) == Exception

assert faturamento_total([],[]) == Exception

assert faturamento_total([4],[]) == Exception

assert faturamento_total([],[5]) == Exception

assert media_faturamento([-4],[3]) == Exception

assert media_faturamento([5],[-6]) == Exception

assert media_faturamento([],[]) == Exception

assert media_faturamento([2],[]) == Exception

assert media_faturamento([],[3]) == Exception

assert faturamento([2],['j']) == Exception

assert faturamento_total(['a'],[1]) == Exception

assert faturamento_total([2],['f']) == Exception

print('teste tudo ok! da questão 6 da lista 2')