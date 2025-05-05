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

assert calcular_poligono(3,4) == 'TRIÂNGULO e o valor do seu perímetro é 12cm'

assert calcular_poligono(4,5) == 'QUADRADO e o valor da sua área é 16cm'

assert calcular_poligono(5,6) == 'É um PENTÁGONO'

#verificar se user digita errado lado
assert calcular_poligono('a',6) == 'valores do lado tem que ser 3 , 4 ou 5'

assert calcular_poligono(-1,7) == 'valores do lado tem que ser 3 , 4 ou 5'

#verificar se user digita errado medida_lado

assert calcular_poligono(3,'a') == 'medida lado inválida'

assert calcular_poligono(3,-4) == 'medida lado inválida'

print('teste tudo OK! da questão 6 da lista 1')