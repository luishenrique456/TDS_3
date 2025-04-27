from q10 import maior

assert maior(10,20,1,2) == 'Maior é 20'

assert maior('a',2,3,4) == Exception

assert maior(1,'b',3,5) == Exception

assert maior('a','b','c','d') == Exception

print('teste tudo OK! da questão 10 da lista 1')