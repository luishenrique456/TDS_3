# 14) Ler uma lista C de 10 elementos inteiros, trocar todos os valores negativos da lista C por 0.
# Escrever a lista C modificada.
def ler_lista(num):
    lista_num = []
    for i in range(num):
        numero = int(input('Digite um número : '))
        lista_num.append(num)
    return lista_num

def mundar_valor_neg():
    pass



def main():
    while True:
        try:
            listas_numeros = ler_lista(10)

            break
        except ValueError:
            print('Valor invalidor')





if __name__ == '__main__':
    main()