# Questão 7 DOT
#Faça um programa para calcular o Fatorial de número .
#Para o cálculo do fatorial , sabemos que N! depende de (N-1)!
#este por sua vez depende de (N-2)! : e,assim por diante , até que N seja 1 ,
#Quando então tem-se que fatorial de 1 igual a 1 mesmo.
#Utilize uma função que recebe como parâmetro de entrada o número a ser calculado o fatorial,
#do tipo inteiro, e retorna o fatorial deste número , também do tipo inteiro.
def fatorial(num):
    if num == 0:
        return 1
    if num == 1:
        return 1
    cont = 1
    for qtd in range(1,num+1):
        cont *= qtd
    return cont


while True:
    try:
        num = int(input('Digite um número : '))
        resul = fatorial(num)
        print(f'Seu número {num}! seu fatorial é {resul}')
        break

    except ValueError:
        print('valor invalidor')