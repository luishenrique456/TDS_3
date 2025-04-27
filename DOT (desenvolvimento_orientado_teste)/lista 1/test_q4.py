
from q4 import media_semestral

assert media_semestral(2,10) == 'PARABÉNS! você foi aprovado!'

assert media_semestral(3,4) == '): você foi reprovado '

#teste nota1 doi 10.5
assert media_semestral(10.5,2) == 'Nota fora do limite' #verficar estar dentro limites de notas 0.0 a 10.0

#teste nota 2 -3.0
assert media_semestral(10,-3.0) == 'Nota fora do limite' #verficar estar dentro limites de notas 0.0 a 10.0

assert media_semestral(10,'a') == 'Nota inválida'

print('teste tudo OK! da questão 4 lista 1')
