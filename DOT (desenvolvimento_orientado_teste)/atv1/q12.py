# questão 12 dot
#Escreva uma função que recebe, por parâmetro, um valor inteiro e positivo e retorna o somatório desse valor.
def somatorio(num):
    cont = 0
    for i in range(num+1):
        cont += i

    return cont


while True:
    try:
        num = int(input('Digite um número : '))
        resultado_somatorio = somatorio(num)
        print(f'Seu somatório é {resultado_somatorio}')
        break


    except ValueError:
        print('valor invalidor')