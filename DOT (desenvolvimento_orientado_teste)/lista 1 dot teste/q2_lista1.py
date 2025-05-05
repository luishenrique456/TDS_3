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

assert area_circulo(4.0) == 50.24

assert area_circulo('a') == Exception

assert area_circulo(-1) == Exception


assert perimetro_circulo(4.0) == 25.12

assert perimetro_circulo('a') == Exception

assert perimetro_circulo(-2) == Exception

print('Teste tá tudo Ok! da questão 2 da lista 1')