#Faça uma função que recebe um número int 
#por parâmetro e retorna verdadeiro se ele for par e falso se for ímpar.
def verficar_par_impar(num):
    if type(num) != int or num <= 0:
        return Exception

    if num % 2 == 0:
        return 'É par'
    else:
        return 'É ímpar'

assert verficar_par_impar(2) == 'É par'

assert verficar_par_impar(3) == 'É ímpar'

assert verficar_par_impar('a') == Exception

assert verficar_par_impar(-1) == Exception

assert verficar_par_impar(2.0) == Exception

print('teste tudo Ok! da questão 1 da lista 1')