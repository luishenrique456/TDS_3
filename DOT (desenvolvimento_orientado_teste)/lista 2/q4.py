# 4) Faça um programa que grave uma lista com 15 posições, calcule e mostre:
# a) O maior elemento da lista e em que posição esse elemento se encontra;
# b) O menor elemento da lista e em que posição esse elemento se encontra.
def maior(numeros):
    maior_num = max(numeros)
    posicao_maior = numeros.index(max(numeros))
    return f'Maior número da lista é {maior_num} sua posição {posicao_maior}'

def menor(numeros):
    menor_num = min(numeros)
    posicao_menor = numeros.index(min(numeros))
    return f'Menor da número da lista é {menor_num} sua posição {posicao_menor}'




def main():
    while True:
        try:
            lista_numeros = []
            for i in range(15):
                num = int(input(f'Digite {i+1} um número : '))
                lista_numeros.append(num)
            
            print(f'Sua lista de número {lista_numeros}')
            print(maior(lista_numeros))
            print(menor(lista_numeros))
            break


        except ValueError:
            print('Valor invalidor')





if __name__ == '__main__':
    main()