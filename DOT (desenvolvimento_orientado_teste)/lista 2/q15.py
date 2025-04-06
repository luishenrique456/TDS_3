# 15) Ler uma lista D de 10 elementos. Criar uma lista E, com todos os elementos de D na ordem
# inversa, ou seja, o último elemento passará a ser o primeiro, o penúltimo será o segundo e assim
# por diante. Escrever todo a lista D e todo a lista E.
def ler_lista(n):
    lista_num = []
    for i in range(n):
        num = int(input(f'Digite {i+1} º um número : '))
        lista_num.append(num)

    return lista_num

def inverter_lista(lista_d):
    lista_d.reverse()
    return lista_d
    



def main():
    while True:
        try:
            lista_d = ler_lista(5)
            print(f'lista D : {lista_d}')
            resul = inverter_lista(lista_d)
            print(f'Lista E : {resul}')
            

            break
        except ValueError:
            print('Valor invalidor')





if __name__ == '__main__':
    main()