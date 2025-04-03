#questão 14 dot
#Escreva uma função que recebe por parâmetro um valor inteiro e positivo N e retorna o valor de S.
#S = 1 + 1/1! + 1⁄2! + 1/3! + 1 /N!
def fatorial(num):
    cont = 1
    for qtd in range(1,num):
        cont *= qtd
    return cont

def formular(num):
    s = 1 + 1/fatorial(1) + 1/fatorial(2) + 1/fatorial(3) + 1/fatorial(num)
    return s

while True:
    try:
        num = int(input('Digite um número : '))
        resultado = formular(num)
        print(f'Resultado é {resultado:.2f}')
        break

    except ValueError:
        print('valor invalidor')