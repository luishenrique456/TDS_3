#Escreva um programa para ler as notas das duas avalições de um aluno no semestre.
# Faça um procedimento que receba as duas notas por parâmetro e calcule e escreva 
# a média semestral e a mensagem " PARABÉNS! você foi aprovado! "
#somente se o aluno foi aprovado (considere 6.0 a média mínima para aprovação)

def media_semestral(nota1,nota2):
    if not isinstance(nota1,(float,int)) or not isinstance(nota2,(float,int)):
        return 'Nota inválida'
    
    if 0.0 <= nota1 <= 10.0 and 0.0 <= nota2 <= 10.0:
        media = nota1+nota2/ 2
        if media >= 6.0:
            return f'PARABÉNS! você foi aprovado!'
        else:
            return f'): você foi reprovado '
    else:
        return f'Nota fora do limite'
    
def main():

    while True:

        try:
            nota1 = float(input('Digite sua nota 1 : '))

            nota2 = float(input('Digite sua nota 2 : '))

            resultado = media_semestral(nota1,nota2)

            print(f'{resultado}')
            break

        except ValueError:
            print('valor invalidor')
if __name__ == '__main__':
    main()



