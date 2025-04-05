# 6) Dadas duas listas, uma contendo a quantidade e a outra o preço de 20 produtos, elabore um
# programa que calcule e exiba o faturamento que é igual a quantidade x preço. Calcule e exiba
# também o faturamento total que é o somatório de todos os faturamentos, a média dos faturamentos
# e quantos faturamentos estão abaixo da média.

def faturamento(lista_qtd : list[int],lista_preco: list[int])-> list[int]:
    lista_faturamento = []
    for i in range(len(lista_qtd)):
        lista_faturamento.append(lista_qtd[i]*lista_preco[i])
    
    return lista_faturamento

def faturamento_total(lista_qtd,lista_preco):
    cont = 0
    lista_faturamento = faturamento(lista_qtd,lista_preco)
    for i in lista_faturamento:
        cont += i
    return cont
    
def media_faturamento(lista_qtd,lista_preco):
    #calcular media
    somar = faturamento_total(lista_qtd,lista_preco)
    media = somar / len(lista_qtd)
    

    lista_faturamento = faturamento(lista_qtd,lista_preco)
    cont_med = 0
    for i in lista_faturamento:
        if i < media:
            cont_med += 1
    return f'média do faturamento {media}\nfaturamentos estão abaixo da média {cont_med}'
    
    




def main():
    while True:
        try:
            lista_qtd = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
            lista_preco = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
            print(f'lista quantidade {len(lista_qtd)}')
            print(f'lista do preço {lista_preco}')
            print(f'lista de Faturamento {faturamento(lista_qtd,lista_preco)}')
            print(f'faturamento total {faturamento_total(lista_qtd,lista_preco)}')
            print(f'{media_faturamento(lista_qtd,lista_preco)}')

            break


        except ValueError:
            print('Valor invalidor')





if __name__ == '__main__':
    main()