# questão 15 dot
#Escreva uma função que recebe por parâmetro um valor inteiro e positivo N e retorna o valor de S.
#S = 2/4 + 5/5 + 10/6 + 17/7 + 26/8 + ... +(t^2+1)/(t+3)
def calcular_s(num:int)-> float:
    resp = 0
    for i in range(1,num+1):
        resp = (i**2+1)/(i+3)
    return resp

while True:
    try:
        num = int(input('Digite um número : '))
        if num > 0:
            result = calcular_s(num)
            print(f'seu número {num}\ncom resultado S = 2/4 + 5/5 + 10/6 + 17/7 + 26/8 + ... +(t^2+1)/(t+3)\nresultado é {result:.2f} ')
            break
        else:
            print('valor tem que ser número positivo.Digite novamante! : ')

    except ValueError:
        print('valor invalidor')