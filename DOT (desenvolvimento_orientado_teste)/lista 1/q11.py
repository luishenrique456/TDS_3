# questão 11 dot
#Faça uma função que recebe, por parâmetro, um valor inteiro e positivo e retorna o número de divisores desse valor.

#função mostra lista de divisores
def divisore(num:int)-> list[int]:
    lista_div = []
    for i in range(1,num+1):
        if num % i == 0:
            lista_div.append(i)

    return lista_div

#função mostra quantidade do divisores
def qtd_divisores(num : int)-> int:
    cont = 0
    for i in range(1,num+1):
        if num % i == 0:
            cont += 1

    return cont


while True:
    try:
        num = int(input('Digite um número : '))
        if num > 0:
            resul = divisore(num)
            total_div = qtd_divisores(num)
            print(f'Seu número : {num}\nseu divisores : {resul}\nTotal de divisores : {total_div}')
            break
        else:
            print('valor tem que ser positivo.Digite novamente : ')

    except ValueError:
        print('valor invalidor')
