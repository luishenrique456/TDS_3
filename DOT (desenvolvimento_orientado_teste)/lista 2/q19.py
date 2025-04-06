# 19) Ler duas listas: R de 5 elementos e S de 10 elementos. Gerar uma lista X de 15 elementos
# cujas 5 primeiras posições contenham os elementos de R e as 10 últimas posições, os elementos
# de S. Escrever a lista X.
def ler_lista(n):
    lista_numeros = []
    for i in range(n):
        num = int(input(f'Digite {i+1}º um número : '))
        lista_numeros.append(num)

    return lista_numeros




def main():
    while True:
        try:
            lista_r = ler_lista(5)
            lista_s = ler_lista(5)

            break
        except ValueError:
            print('Valor invalidor')





if __name__ == '__main__':
    main()