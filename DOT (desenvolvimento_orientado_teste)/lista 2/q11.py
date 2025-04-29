# 11) Faça um programa que alimente uma lista com um número de posições definidas pelo
# usuário.
# Esta lista deverá armazenar um conjunto de nomes em diferentes posições.
# Crie um mecanismo para alimentar elementos da lista e pesquisar por um valor existente.
# ==== =MENU========
# 1)Cadastar nome
# 2)Pesquisar nome
# 3)Listar todos os nome
# 4) Alterar nome
#  ---> O usuario digita o nome que deseja alterar, mostra a posição do nome e pede o novo nome que será colocado
# 5) Excluir nome
#  ---> Perguntar  se o usuário tem certeza que deseja excluir, sem usar o método remove()
# 0) Sair do programa
# ——————–
# Digite sua escolha:_


def cadastar_nome(lista_nome,add_nome):
    
    lista_nome.append(add_nome)
    print(f'Nome {add_nome} adicionado com sucesso')
    return lista_nome

def pesquisar_nome(lista_nome,nome_busca):
    
    if nome_busca in lista_nome:
        return f'{nome_busca} estar na lista'
    else:
        return f'{nome_busca} Não estar na lista'
    
def mostra_lista(lista_nomes):
    return lista_nomes

def altera(lista_nome,altera_nome,nome_editado):
    if altera_nome in lista_nome:
        index = lista_nome.index(altera_nome)
        lista_nome[index] = nome_editado
        return f'\nnome atigo {altera_nome} foi editado para {nome_editado} com sucesso'
    else:
        return f'Nome {altera_nome} Não estar na lista'
    
def excluir(lista_nome,nome_excluir,op):

    if op == 'N':
        return 'opção de Excluir foi cancelado'

    if op == 'S':

        if nome_excluir in lista_nome:
            index_nome = lista_nome.index(nome_excluir)
            del lista_nome[index_nome]
            return f'Nome excluindo com sucesso'
        else:
            return f'Nome {nome_excluir} não estar na lista para excluir'
    else:
        return f'Opção inválida'
    



def main():


    lista_nomes = [] 
    while True:
        try:
        
            print('''
            ==== =MENU========
        1)Cadastar nome
        2)Pesquisar nome
        3)Listar todos os nome
        4)Alterar nome
        5) Excluir nome
        0)Sair do programa
        ——————–--------------

        ''')
            opcao = int(input('Digite sua escolha um número (1 , 2 , 3 , 4 , 5 ou 0) : '))

            if opcao == 0:
                print('Programa encerrado')
                break
            elif opcao == 1:
                add_nome = input('Digite um nome : ').title()
                lista_nomes = cadastar_nome(lista_nomes,add_nome)
            
            elif opcao == 2:
                nome_busca = input('Digite nome pesquisa : ').title()
                print(pesquisar_nome(lista_nomes,nome_busca))
            elif opcao == 3:
                lista_nomes = mostra_lista(lista_nomes)
                print(lista_nomes)
            elif opcao == 4:
                altera_nome = input('Digite um nome estar na lista para Editar : ').title()
                nome_editado = input('Digite nome para ser Editado : ').title()

                print(altera(lista_nomes,altera_nome,nome_editado))

            elif opcao == 5:
                nome_exculir = input('Digite um nome da lista para exculir : ').title()
                op = input('Digite S para continuar ou N para cancelar : ').upper()[0]
                print(excluir(lista_nomes,nome_exculir,op))

            else:
                print('Opção inválida por favor Digite Novamente (1 , 2 , 3 , 4 , 5 ou 0) : ')
            
        except ValueError:
            print('valor invalidor! Digite Novamente')

if __name__ == '__main__':
    main()





