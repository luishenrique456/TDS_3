#Escreva um programa para ler uma temperatura em graus Fahrenheit.
#Faça uma função chamada celsius para calcular e retornar o valor em graus Celsius.

def converter_celsius(temperatura_fah):
    celsius = ((temperatura_fah-32)/9) * 5
    return celsius

while True:

    try:
    
        temp_fah = int(input('Digite temperatura em Fahrenheit : '))

        temp_convertido = converter_celsius(temp_fah)

        print(f'Sua temperatura convertida para Celsius é {temp_convertido:.2f}')
        break

    except ValueError:
        print('Valor invalido')