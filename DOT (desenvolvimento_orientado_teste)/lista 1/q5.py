#Faça um programa que leia a altura e o sexo 
# 1 para feminino e 2 para masculino
# uma função calcular peso ideal que receba altura e o sexo via parâmetro
#e que calcule e retorne seu peso ideal formula

def peso_ideal(sexo,altura):
    if not isinstance(altura,float) or not 0 <= altura:
        return 'valor inválido na altura'

    if not isinstance(sexo,int) or not 1<= sexo <= 2:
        return 'opção inválida'

    if sexo == 1:
        resul_femino = (62.1*altura) - 44.7
        return round(resul_femino,2)
    elif sexo == 2:
        resul_masculino = (72.7*altura) - 58
        return round(resul_masculino,2)
    
def main():

    while True:

        try:

            sexo = int(input('Digite um número 1 para feminino ou 2 para masculino : '))

            altura = float(input('Digite sua altura (EX: 1.60) : '))

            resul_peso_ideal = peso_ideal(sexo,altura)

            print(f'Resultado do seu peso ideal é {resul_peso_ideal}')
            break
        except ValueError:
            print('valor invalido')
if __name__ == '__main__':
    main()

