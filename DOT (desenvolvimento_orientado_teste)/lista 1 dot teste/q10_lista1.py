# questão 10 dot
#Escreva um programa composto de uma função Max e o programa principal como segue:
#a) A função Max recebe como parâmetros de entrada quatro números inteiros e retorna o maior. Se forem iguais retorna qualquer um
#deles;
#b) O programa principal lê 4 séries de 4 números a, b , c , d. Para cada série lida imprime o maior dos quatro números usando a função
#Max.
def maior(a,b,c,d):
    if type(a) != int or type(b) != int or type(c) != int or type(d) != int:
        return Exception

    maior = a
    if b > maior:
        maior = b
    if c > maior:
        maior = c
    if d > maior:
        maior = d
    return f'Maior é {maior}'

assert maior(10,20,1,2) == 'Maior é 20'

assert maior('a',2,3,4) == Exception

assert maior(1,'b',3,5) == Exception

assert maior('a','b','c','d') == Exception

print('teste tudo OK! da questão 10 da lista 1')