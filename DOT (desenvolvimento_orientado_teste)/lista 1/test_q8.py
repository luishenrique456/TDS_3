from q8 import opcao

assert opcao('S') == 'S'

assert opcao('N') == 'N'

assert opcao('a') == 'entrada inválida'

assert opcao(1) == Exception

print('teste tudo OK! da questão 8 da lista 1')