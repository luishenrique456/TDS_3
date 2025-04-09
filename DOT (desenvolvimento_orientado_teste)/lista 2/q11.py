# 11) Faça um programa que alimente uma lista com um número de posições definidas pelo
# usuário.
# Esta lista deverá armazenar um conjunto de nomes em diferentes posições.
# Crie um mecanismo para alimentar elementos da lista e pesquisar por um valor existente.
# ==== =MENU========
# 1)Cadastar nome
# 2)Pesquisar nome
# 3)Listar todos os nome
# 0) Sair do programa
# ——————–
# Digite sua escolha:_


def cadastar_nome():
    add_nome = input('Digite um nome : ').title()
    lista_nomes.append(add_nome)
    print(f'Nome {add_nome} adicionado com sucesso')
    return lista_nomes

def pesquisar_nome(lista_nome):
    nome = input('Digite nome pesquisa : ').title()
    if nome in lista_nome:
        return f'{nome} estar na lista'
    else:
        return f'{nome} Não estar na lista'
    
def mostra_lista(lista_nomes):
    return lista_nomes



    
    





lista_nomes = [] #variavel global
while True:
    try:
        
        print('''
        ==== =MENU========
     1)Cadastar nome
     2)Pesquisar nome
     3)Listar todos os nome
     0) Sair do programa
     ——————–--------------

        ''')
        opcao = int(input('Digite sua escolha um número (1,2,3 ou 0) : '))

        if opcao == 0:
            print('Programa encerrado')
            break
        elif opcao == 1:
            lista_nomes = cadastar_nome()
            
        elif opcao == 2:
            print(pesquisar_nome(lista_nomes))
        elif opcao == 3:
            lista_nomes = mostra_lista(lista_nomes)
            print(lista_nomes)
        else:
            print('Opção invalidor por favor Digite Novamente (1,2,3 ou 0) : ')
            
        
    
    


    except ValueError:
        print('valor invalidor! Digite Novamente')





