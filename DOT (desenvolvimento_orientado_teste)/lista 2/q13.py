# 13) Tentando descobrir se um dado era viciado, um dono de cassino honesto (ha! ha! ha! ha!) o
# lançou n vezes. Dados os n resultados dos lançamentos, determinar o número de ocorrências de
# cada face.
from random import randint

def dado_user():
    lista_vezes = []
    lancamento = int(input('Digite número do lançamento do seu dado : '))
    for i in range(lancamento):
        lista_vezes.append(randint(1,6))
    return lista_vezes





def ocorrencia(lista_dado : list[int],face1):
    cont = 0
    for i in lista_dado:
        if i == face1:
            cont +=1
    return cont

        

    



def main():
    while True:
        try:
            lista_dados = dado_user()
            print(lista_dados)
            face1 = int(input('Digite número da face 1 º : '))
            if 1<= face1 <= 6:
                resul = ocorrencia(lista_dados,face1)
                print(f'Face 1º {resul} vezes')
                break
            else:
                print('Só pode números 1 a 6. Digite Novamente')
            

            

            
        except ValueError:
            print('Valor invalidor')





if __name__ == '__main__':
    main()