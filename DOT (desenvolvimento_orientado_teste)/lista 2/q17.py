# 17) Ler uma lista W de 10 elementos, depois ler um valor V. Contar e escrever quantas vezes o
# valor V ocorre na lista W e escrever também em que posições (índices) da lista W o valor V
# aparece.
# Caso o valor V não ocorra nenhuma vez na lista W, escrever uma mensagem informando isto.
from random import randint

def ler_lista(n):
    lista_numero = []
    for i in range(n):
        # num = int(input(f'Digite {i+1}º um número : '))
        lista_numero.append(randint(1,5))
    return lista_numero

def contador_ocorrecia(lista_w : list[int],num : int):
    cont = 0
    for i in lista_w:
        if i == num:
            cont += 1


    posicao = lista_w.index(num)

    return f'Seu número {num}\nQuantas repetiu {cont}\nSua Posição {posicao+1}'




def main():
    while True:
        try:
            lista_w = ler_lista(5)
            valor = int(input('Digite um número da lista : '))
            if valor in lista_w:
                resul = contador_ocorrecia(lista_w,valor)
                print(f'Lista {lista_w}')
                print(resul)
                break
            else:
                print(f'Esse valor {valor} não estar na lista.Digite Novamente!')
            
            



        except ValueError:
            print('Valor invalidor')





if __name__ == '__main__':
    main()