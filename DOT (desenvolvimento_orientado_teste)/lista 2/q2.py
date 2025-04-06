# 2) Faça um programa que grave uma lista com dez números reais, calcule e mostre a quantidade
# de números negativos e a soma dos números positivos dessa lista.

def conta_negativo(numeros : list[int])-> int:
    cont_neg = 0
    for i in range(len(numeros)):
        if numeros[i] < 0:
            cont_neg += 1

    return f'Quantidade de números negativo é {cont_neg}'

def somar_lista(numeros):
    cont = 0
    for i in numeros:
        if i > 0:
            cont += i
    return f'Somar da lista é  {cont}'


def main():
    while True:

        try:

            lista_num_reais = []
            for i in range(5):
                num = int(input(f'Digite {i+1}º seu número : '))
                lista_num_reais.append(num)

            print(conta_negativo(lista_num_reais))
            print(somar_lista(lista_num_reais))
            break
        except ValueError:
            print('valor invalidor')



if __name__ == '__main__':
    main()