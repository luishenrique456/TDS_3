from q2 import area_circulo , perimetro_circulo

assert area_circulo(4.0) == 50.24

assert area_circulo('a') == Exception

assert area_circulo(-1) == Exception


assert perimetro_circulo(4.0) == 25.12

assert perimetro_circulo('a') == Exception

assert perimetro_circulo(-2) == Exception

print('Teste tá tudo Ok! da questão 2 da lista 1')