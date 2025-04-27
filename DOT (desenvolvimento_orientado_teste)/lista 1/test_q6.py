from q6 import calcular_poligono

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