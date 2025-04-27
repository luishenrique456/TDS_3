#Escreva um programa que leia o raio de um círculo e faça duas funções
#uma função chamada área que calcula e retorna a área do círculo
# e outra função chamada perímetro  que calcula e retorna o perímetro do círculo
def area_circulo(r):
    if type(r) != float or r <= 0:
        return Exception
    area = 3.14 * r **2
    return area

def perimetro_circulo(r):
    if type(r) != float or r <= 0:
        return Exception
    perimetro = 3.14 * 2 * r
    return perimetro

def main():

    while True:

        try:

            r = float(input('Digite raio do círculo :'))
            print(f'Raio do círculo é {area_circulo(r)}')
            print(f'Raio do círculo é {perimetro_circulo(r)}')
            break

        except ValueError:
            print('Invalidor')
if __name__ == "__main__":
    main()