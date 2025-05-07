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
    if type(lista_nome) != list or type(add_nome) != str or not all(isinstance(i,str)for i in lista_nome):
        return Exception
    
    lista_nome.append(add_nome)
    #print(f'Nome {add_nome} adicionado com sucesso')
    return lista_nome

def pesquisar_nome(lista_nome,nome_busca):
    if type(lista_nome) != list or type(nome_busca) != str or not all(isinstance(i,str)for i in lista_nome):
        return Exception

    
    if nome_busca in lista_nome:
        return f'{nome_busca} estar na lista'
    else:
        return f'{nome_busca} Não estar na lista'
    
def mostra_lista(lista_nomes):
    if type(lista_nomes) != list or not all(isinstance(i,str)for i in lista_nomes):
        return Exception
    return lista_nomes

def altera(lista_nome,altera_nome,nome_editado):
    if type(lista_nome) != list or type(altera_nome) != str or type(nome_editado) != str or not all(isinstance(i,str)for i in lista_nome):
        return Exception
    
    if altera_nome in lista_nome:
        index = lista_nome.index(altera_nome)
        lista_nome[index] = nome_editado
        return f'\nnome atigo {altera_nome} foi editado para {nome_editado} com sucesso'
    else:
        return f'Nome {altera_nome} Não estar na lista'
    
def excluir(lista_nome,nome_excluir,op):
    if type(lista_nome) != list or type(nome_excluir) != str or type(op) != str or not all(isinstance(i,str)for i in lista_nome):
        return Exception

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

#testa função cadastar_nome(list_nomes[] : list[] ,nome : str) -> list[str]
assert cadastar_nome([],'Luis') == ['Luis']

assert cadastar_nome([] , '') == ['']

#testa pesquisar_nome(lista_nome : list[] ,nome_busca : str) -> str

assert pesquisar_nome(['Luis','João'], 'João') == 'João estar na lista'

assert pesquisar_nome(['Luis','Carlos'] ,'Lucas') == 'Lucas Não estar na lista'


#testa função mostra_lista(lista_nomes : list[]) -> list[]

assert mostra_lista([]) == []

assert mostra_lista(['Pedro','Luis']) == ['Pedro','Luis']

#testa função altera(lista_nome : list[] ,altera_nome : str ,nome_editado : str) -> str

assert altera(['Luis','Felipe','Pedro'],'Luis','João') == '\nnome atigo Luis foi editado para João com sucesso'

assert altera(['Luis','Felipe','Pedro'],'Lucas','João') == 'Nome Lucas Não estar na lista'

#testa função excluir(lista_nome : list[] ,nome_excluir : str ,op : str) -> str

assert excluir(['Luis','Felipe','Pedro'],'Pedro','S' ) == 'Nome excluindo com sucesso'

assert excluir(['Luis','Lucas'],'Lucas','N') == 'opção de Excluir foi cancelado'

assert excluir(['Luis','Kallya'],'Pedro','S') == 'Nome Pedro não estar na lista para excluir'

assert excluir(['Luis','Kallya'],'Pedro','E') == 'Opção inválida'

# verficar entrada do parâmetro é do tipo list def função cadastar_nome(lista_nome : list[str] , add_nome : str)

assert cadastar_nome('a','Kallya') == Exception

assert cadastar_nome(['luis'],2) == Exception

assert cadastar_nome([1],'Carlos') == Exception

assert cadastar_nome([1.2],3.0) == Exception

# verficar entrada do parâmetro é do tipo list def função pesquisar_nome(lista_nome : list[str],nome_busca : str)

assert pesquisar_nome(['Luis'],1) == Exception

assert pesquisar_nome('b','Ryan') == Exception

assert pesquisar_nome([3.5],'Luis') == Exception

assert pesquisar_nome([1],[2]) == Exception

assert pesquisar_nome([1],3.5) == Exception

# verficar entrada do parâmetro é do tipo list def função mostra_lista(lista_nomes : list[])

assert mostra_lista('b') == Exception

assert mostra_lista(3.5) == Exception

assert mostra_lista([1]) == Exception

assert mostra_lista([3.0]) == Exception

# verficar entrada do parâmetro é do tipo list def função altera(lista_nome : list[str] ,altera_nome : str , nome_editado : str)

assert altera(['Pedro'],1,'Lucas') == Exception

assert altera([2],'Ângela','Andressa') == Exception

assert altera(['Luis'],'Luis',3) == Exception

assert altera(3.0,'luis','pedro') == Exception

assert altera([2.4],'Murilo','Ryan') == Exception

# verficar entrada do parâmetro é do tipo list def função excluir(lista_nome : list[] , nome_excluir : str , op : str)

assert excluir(1,'Lucas','João') == Exception

assert excluir([4],'Lucas','Pedro') == Exception

assert excluir(3.0,'Luis','Caio') == Exception

assert excluir([1.5],'Luis','Kaio') == Exception

assert excluir(['Luis'],2,'Pedro') == Exception

assert excluir(['Luis'],['kaio'],'Caio') == Exception

assert excluir(['Luis'],'Henrique',1) == Exception

print('Teste tudo OK! da questão 11 da lista 2')