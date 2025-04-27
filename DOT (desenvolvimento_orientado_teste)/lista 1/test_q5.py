from q5 import peso_ideal

assert peso_ideal(1,1.60) == 54.66

assert peso_ideal(2,1.70) == 65.59

#testa se user digita opção do sexo errado
assert peso_ideal('a',1.50) == 'opção inválida'

assert peso_ideal(-3,1.80) == 'opção inválida'

#testa se user digite tipo da altura errado
assert peso_ideal(1,'b') == 'valor inválido na altura'

assert peso_ideal(2,-3.0) == 'valor inválido na altura'

print('teste tudo OK! da questão 5 lista 1')