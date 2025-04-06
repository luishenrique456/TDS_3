# 3) Faça um programa que dada uma seqüência de n números, imprimi-la na ordem inversa à da
# leitura.
def reverte_num(numeros: list[int])->list[int]:
    numeros.reverse()
    return numeros





def main():

    while True:
        try:

            lista_numeros = []
            for i in range(10):
                num = int(input(f"Digite {i+1}º um número : "))
                lista_numeros.append(num)
    
            print(reverte_num(lista_numeros))
            break
        except ValueError:
            print('Valor invalidor')

if __name__ == '__main__':
    main()