from q11 import divisore , qtd_divisores

assert divisore(5) == [1,5]

assert qtd_divisores(5) == 2

assert divisore(5.0) == Exception

assert divisore('a') == Exception

assert qtd_divisores('b') == Exception

assert divisore(-1) == Exception

assert qtd_divisores(-2) == Exception

print('teste tudo OK! da questão 11 da lista 1 ')