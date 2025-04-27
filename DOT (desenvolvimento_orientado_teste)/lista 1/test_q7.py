from q7 import fatorial

assert fatorial(5) == 120

assert fatorial(0) == 1

assert fatorial(1) == 1

#testa possivel erro do user

assert fatorial('a') == Exception

assert fatorial(2.0) == Exception

assert fatorial(-4) == Exception

print('teste tudo OK! da questão 7 da lista 1')