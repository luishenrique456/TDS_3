# QUESTÃO 9 DOT
#Escreva uma função que recebe 2 números inteiros n1 e n2 como entrada e retorna a soma de todos os números inteiros contidos
#no intervalo [n1,n2]. Use esta função em um programa que lê n1 e n2 do usuário e imprime a soma.
def soma_intervalo(num1,num2):
    if type(num1) != int or type(num2) != int:
        return Exception

    cont = 0
    for qtd in range(num1,num2+1):
        cont += qtd
    return cont

assert soma_intervalo(1,5) == 15

# testa user digita errado tipo num1 errado

assert soma_intervalo('a',5) == Exception

assert soma_intervalo(2,4.0) == Exception

assert soma_intervalo('a','b') == Exception

print('teste tudo OK! da questão 9 da lista 1')