# questão 6 DOT
# Escreva um programa para ler o número de lados de um polígono regular
# e a medida do lado (em cm) . Faça um procedimento que receba como parâmetro
# o número de lados e a medida do lado deste polígono e calcule e imprima
# se o número de lados for igual 3 , escreva TRIÂNGULO e o valor do seu perímetro.
# se o número de lados for igual 4 , escreva QUADRADO e o valor da sua área.
# se o número de lados for igual 5 , escreva PENTÁGONO. (OBS : considere que usuário só informará os valores 3,4 ou 5)
def calcular_poligono(lado,medida_lado):
    if type(lado) != int or not 3<= lado <= 5:
        return 'valores do lado tem que ser 3 , 4 ou 5'
    if type(medida_lado) != int or medida_lado <= 0:
        return 'medida lado inválida'

    perimetro = lado * medida_lado

    area = lado **2

    if lado == 3:
        return f'TRIÂNGULO e o valor do seu perímetro é {perimetro}cm'
    elif lado == 4:
        return f'QUADRADO e o valor da sua área é {area}cm'
    elif lado == 5:
        return 'É um PENTÁGONO'


def main():

    while True:
        try:
            lado = int(input('Digite número de lados (3 , 4 ou 5) : '))
            medida_lado = int(input('Digite número da medida do lado : '))
            resultado = calcular_poligono(lado,medida_lado)
            print(resultado)
            break

        except ValueError:
            print('valor invalidor')
if __name__ == '__main__':
    main()