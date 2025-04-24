from q1 import verficar_par_impar


assert verficar_par_impar(2) == 'É par'

assert verficar_par_impar(3) == 'É ímpar'

assert verficar_par_impar('a') == Exception

assert verficar_par_impar(-1) == Exception

assert verficar_par_impar(2.0) == Exception

print('teste tudo Ok! da questão 1')
