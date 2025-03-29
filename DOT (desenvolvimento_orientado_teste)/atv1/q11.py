# questão 11 dot
#Faça uma função que recebe, por parâmetro, um valor inteiro e positivo e retorna o número de divisores desse valor.

def divisore(num):
    lista_div = []
    for i in range(1,num+1):
        if num % i == 0:
            lista_div.append(i)

    return lista_div


while True:
    try:
        num = int(input('Digite um número : '))
        if num > 0:
            resul = divisore(num)
            print(f'seu número {num} seu divisores : {resul}')
            break
        else:
            print('valor tem que ser positivo.Digite novamente : ')

    except ValueError:
        print('valor invalidor')
