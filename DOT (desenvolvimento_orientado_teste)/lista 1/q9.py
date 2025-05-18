# QUESTÃO 9 DOT
#Escreva uma função que recebe 2 números inteiros n1 e n2 como entrada e retorna a soma de todos os números inteiros contidos
#no intervalo [n1,n2]. Use esta função em um programa que lê n1 e n2 do usuário e imprime a soma.
def soma_intervalo(num1,num2):
    if type(num1) != int or type(num2) != int:
        return Exception

    soma = 0
    for i in range(num1,num2+1):
        soma += i
    return soma

def main():

    while True:
        try:
            num1 = int(input('Digite número de inicio : '))
            num2 = int(input('Digite número de fim : '))
            if num1 < num2:
                resultado = soma_intervalo(num1,num2)
                print(f'soma do intervalo {num1} e {num2} é {resultado}')
                break
            else:
                print(f'inicio tem que ser menor {num1} e fim tem que ser maior {num2}')

        except ValueError:
            print('\nValor invalidor')
if __name__ == '__main__':
    main()