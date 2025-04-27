# questão 13 dot
#Escreva uma função que recebe por parâmetro um valor inteiro e positivo N e retorna o valor de S.
#S = 1 + 1⁄2 + 1/3 + 1⁄4 + 1/5 + 1/N.
def formular_S(num):
    if type(num) != int or num <= 0:
        return Exception

    s = 1 + 1/2 + 1/3 + 1/4 + 1/5 + 1/num
    return round(s,2)

def main():

    while True:
        try:
            num = int(input('Digite um número : '))
            resultado = formular_S(num)
            print(f'Seu resultado é {resultado:.2f}')
            break

        except ValueError:
            print('valor invalidor')
if __name__ == '__main__':
    main()