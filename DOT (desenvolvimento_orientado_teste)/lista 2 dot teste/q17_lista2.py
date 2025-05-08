# 17) Ler uma lista W de 10 elementos, depois ler um valor V. Contar e escrever quantas vezes o
# valor V ocorre na lista W e escrever também em que posições (índices) da lista W o valor V
# aparece.
# Caso o valor V não ocorra nenhuma vez na lista W, escrever uma mensagem informando isto.

def contador_ocorrecia(lista_w : list[int],num : int):
    if type(lista_w) != list or not all(isinstance(i,int)for i in lista_w) or len(lista_w) == 0:
        return Exception
    if type(num) != int:
        return Exception

    cont = 0
    for i in lista_w:
        if i == num:
            cont += 1


    posicao = lista_w.index(num)

    return f'Seu número {num}\nQuantas repetiu {cont}\nSua Posição {posicao+1}'

assert contador_ocorrecia([2, 2, 4, 4, 5],4) == 'Seu número 4\nQuantas repetiu 2\nSua Posição 3'

#verficar parâmetro é tipo list

assert contador_ocorrecia(3.6,3.0) == Exception

assert contador_ocorrecia([],3) == Exception

assert contador_ocorrecia('a',4) == Exception

assert contador_ocorrecia([5],'d') == Exception

#verficar elemento da list é int

assert contador_ocorrecia(['a'],'d') == Exception

assert contador_ocorrecia([1.6],5)

print('Teste tudo Ok! da questão 17 da lista 2')