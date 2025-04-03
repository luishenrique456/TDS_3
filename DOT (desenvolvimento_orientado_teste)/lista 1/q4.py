#Escreva um programa para ler as notas das duas avalições de um aluno no semestre.
# Faça um procedimento que receba as duas notas por parâmetro e calcule e escreva 
# a média semestral e a mensagem " PARABÉNS! você foi aprovado! "
#somente se o aluno foi aprovado (considere 6.0 a média mínima para aprovação)

def media_Semestral(nota1,nota2):
    media = nota1+nota2/ 2
    if 6.0 < media:
        return f'PARABÉNS! você foi aprovado!'
    else:
        return f'): você foi reprovado '
while True:

    try:
        nota1 = float(input('Digite sua nota 1 : '))

        nota2 = float(input('Digite sua nota 2 : '))

        resultado = media_Semestral(nota1,nota2)

        print(f'{resultado}')
        break

    except ValueError:
        print('valor invalidor')



