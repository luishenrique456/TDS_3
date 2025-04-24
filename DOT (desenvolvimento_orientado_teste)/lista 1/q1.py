#Faça uma função que recebe um número int 
#por parâmetro e retorna verdadeiro se ele for par e falso se for ímpar.
def verficar_par_impar(num):
    if type(num) != int or num <= 0:
        return Exception

    if num % 2 == 0:
        return 'É par'
    else:
        return 'É ímpar'

def main():

    while True:
        try:
            num = int(input('Digite um número : '))
            resul = verficar_par_impar(num)
            print(resul)
            break
        except ValueError:
            print('Invalidor')
if __name__ == '__main__':
    main()
        
