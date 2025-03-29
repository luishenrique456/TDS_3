#Faça um programa que leia a altura e o sexo 
# 1 para feminino e 2 para masculino
# uma função calcular peso ideal que receba altura e o sexo via parâmetro
#e que calcule e retorne seu peso ideal formula
def peso_ideal(sexo,altura):
    if sexo == 1:
        return (62.1*altura) - 44.7
    elif sexo == 2:
        return (72.7*altura) - 58
    else:
        return f'de acordo com essas opção : 1 para feminino ou 2 para masculino\nVocê digitou {sexo} opcão invalida'
    
while True:

    try:

        sexo = int(input('Digite um número 1 para feminino ou 2 para masculino : '))

        altura = float(input('Digite sua altura : '))

        resul_peso_ideal = peso_ideal(sexo,altura)

        print(f'Resultado do seu peso ideal é {resul_peso_ideal}')
        break
    except ValueError:
        print('valor invalido')

