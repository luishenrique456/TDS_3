#Escreva um programa que leia o raio de um círculo e faça duas funções
#uma função chamada área que calcula e retorna a área do círculo
# e outra função chamada perímetro  que calcula e retorna o perímetro do círculo
def area_circulo(r):
    area = 3.14 * r **2
    return area

def perimetro_circulo(r):
    perimetro = 3.14 * 2 * r
    return perimetro

while True:

    try:

        r = float(input('Digite raio do círculo :'))
        r = float(input('Digite perímetro do círculo :'))
        print(f'Raio do círculo é {area_circulo(r)}')
        print(f'Raio do círculo é {perimetro_circulo(r)}')
        break

    except ValueError:
        print('Invalidor')