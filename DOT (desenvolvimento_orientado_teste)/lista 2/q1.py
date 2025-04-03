# 1) Faça um programa que grave uma lista de 100 elementos numéricos inteiros e:
# a) Mostre a quantidade de números pares;
# b) Grave uma lista somente com os números pares e mostre a lista;
# c) Mostre a quantidade de números ímpares;
# d) Grave uma lista somente com os números ímpares e mostre a lista.
def lista_par(list_num : list[int])-> list[int]:
    num_par = []
    num_impar = []
    for i in range(len(list_num)):
        if  i % 2  == 0:
            num_par.append(i)
        else:
            num_impar.append(i)

    cont_impar = 0

    for i in range(len(num_impar)):
        cont_impar +=1

    cont_par = 0
    for i in range(len(num_par)):
        cont_par += 1

    return f'Lista de número pares : {num_par}\nQuantidade de números pares : {cont_par}\nLista de números impar : {num_impar}\nQuantidade de número impares : {cont_impar}'




def main():
    while True:
        try:


            lista_num = []
            for i in range(10+1):
                num = int(input(f'Digite um {i+1} número : '))
                lista_num.append(num)

            resul_par = lista_par(lista_num)
    
            print(f'{resul_par}')
            break
        except ValueError:
            print('valor invalidor')

    


if __name__ == '__main__':
    main()