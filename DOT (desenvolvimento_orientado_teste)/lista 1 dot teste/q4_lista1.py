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
    
assert media_semestral(2,10) == 'PARABÉNS! você foi aprovado!'

assert media_semestral(3,4) == '): você foi reprovado '

#teste nota1 doi 10.5
assert media_semestral(10.5,2) == 'Nota fora do limite' #verficar estar dentro limites de notas 0.0 a 10.0

#teste nota 2 -3.0
assert media_semestral(10,-3.0) == 'Nota fora do limite' #verficar estar dentro limites de notas 0.0 a 10.0

assert media_semestral(10,'a') == 'Nota inválida'

print('teste tudo OK! da questão 4 lista 1')