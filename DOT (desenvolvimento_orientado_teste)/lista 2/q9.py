# 9) Dada uma lista X numérica contendo 5 elementos, fazer um programa que crie e exiba na tela
# uma lista Y. A lista Y deverá conter o mesmo conteúdo da lista X na ordem inversa.
def inverter(listas_num):
    listas_num.reverse()
    return listas_num






def main():
    while True:
        try:
            lista_x = []
            for i in range(5):
                num = int(input('Digite um número : '))
                lista_x.append(num)

            lista_x_copida = lista_x[:] #fazer uma copia da lista original

            print(f'Lista X {lista_x_copida}')

            print(f'Lista Y {inverter(lista_x)}')
            break
            
            


        except ValueError:
            print('Valor invalidor')





if __name__ == '__main__':
    main()