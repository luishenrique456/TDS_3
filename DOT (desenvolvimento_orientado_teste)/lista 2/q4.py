# 4) Faça um programa que grave uma lista com 15 posições, calcule e mostre:
# a) O maior elemento da lista e em que posição esse elemento se encontra;
# b) O menor elemento da lista e em que posição esse elemento se encontra.
def maior():
    pass



def main():
    while True:
        try:
            lista_numeros = []
            for i in range(15+1):
                num = int(input(f'Digite {i+1} um número : '))
                lista_numeros.append(num)
            
            print(lista_numeros)
            break


        except ValueError:
            print('Valor invalidor')





if __name__ == '__main__':
    main()