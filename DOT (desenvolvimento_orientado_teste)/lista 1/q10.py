# questão 10 dot
#Escreva um programa composto de uma função Max e o programa principal como segue:
#a) A função Max recebe como parâmetros de entrada quatro números inteiros e retorna o maior. Se forem iguais retorna qualquer um
#deles;
#b) O programa principal lê 4 séries de 4 números a, b , c , d. Para cada série lida imprime o maior dos quatro números usando a função
#Max.
def maior(a,b,c,d):
    maior = a
    if b > maior:
        maior = b
    if c > maior:
        maior = c
    if d > maior:
        maior = d
    return f'Maior é {maior}'


while True:
    try:
        n1 = int(input('Digite um número : '))
        n2 = int(input('Digite um número : '))
        n3 = int(input('Digite um número : '))
        n4 = int(input('Digite um número : '))

        resultado = maior(n1,n2,n3,n4)

        print(f'Maior é {resultado}')
        break
    
    except ValueError:
        print('valor invalidor')