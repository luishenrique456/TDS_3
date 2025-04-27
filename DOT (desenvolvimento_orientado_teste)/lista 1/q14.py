#questão 14 dot
#Escreva uma função que recebe por parâmetro um valor inteiro e positivo N e retorna o valor de S.
#S = 1 + 1/1! + 1⁄2! + 1/3! + 1 /N!
def fatorial(num):
    if type(num) != int or num <=0:
        return Exception


    cont = 1
    for qtd in range(1,num+1):
        cont *= qtd
    return cont

def formular(num):
    if type(num) != int or num <= 0:
        return Exception
    
    s = 1 + 1/fatorial(1) + 1/fatorial(2) + 1/fatorial(3) + 1/fatorial(num)
    return round(s,2)

def main():

    while True:
        try:
            num = int(input('Digite um número : '))
            resultado = formular(num)
            resul_fatorial = fatorial(num)
            print(f'Resultado é {resultado:.2f}\n resultado fatorial {resul_fatorial} ')
            break

        except ValueError:
            print('valor invalidor')
if __name__ == '__main__':
    main()