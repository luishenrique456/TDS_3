#Escreva um programa para ler uma temperatura em graus Fahrenheit.
#Faça uma função chamada celsius para calcular e retornar o valor em graus Celsius.

def converter_celsius(temperatura_fah):
    if type(temperatura_fah) != int:
        return Exception
    celsius = ((temperatura_fah-32)/9) * 5
    return round(celsius,2)

assert converter_celsius(100) == 37.78

assert converter_celsius('a') == Exception

print('Teste tudo OK! da questão 3 da lista 1')