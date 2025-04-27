from q14 import fatorial , formular

assert fatorial(5) == 120

assert fatorial(1) == 1

assert fatorial(2) == 2

assert fatorial(3) == 6

assert formular(5) == 2.67

# testa entrada inválida 

assert fatorial(2.3) == Exception

assert fatorial('a') == Exception

assert fatorial(-2) == Exception

assert formular('b') == Exception

assert formular(-4) == Exception

assert formular(5.0) == Exception

print('Teste tudo OK! da questão 14 da lista 1')