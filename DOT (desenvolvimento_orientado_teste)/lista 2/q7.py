# 7) Dada uma lista contendo 10 elementos numéricos, elabore um programa que verifique se um
# outro valor dado pertence ou não à lista.
def verficar_valor(num):
    lista_numeros = [1,20,3,4,5,30,60,44,33,9]
    for i in lista_numeros:
        if i == num:
            return f'Seu número estar na lista {num}'
        else:
            return f'Seu número não estar na lista {num}'





def main():
    while True:
        try:
            
            num = int(input('Digite um número : '))
            resul = verficar_valor(num)
            print(resul)
            break


        except ValueError:
            print('Valor invalidor.Digite novamente')





if __name__ == '__main__':
    main()