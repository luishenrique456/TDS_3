#Faça uma função que recebe um número int 
#por parâmetro e retorna verdadeiro se ele for par e falso se for ímpar.
def verficar_par_impar(num):
    if num % 2 == 0:
        return 'É par'
    else:
        return 'É ímpar'
while True:
    try:
        num = int(input('Digite um número : '))
        resul = verficar_par_impar(num)
        print(resul)
    except ValueError:
        print('Invalidor')
        break
