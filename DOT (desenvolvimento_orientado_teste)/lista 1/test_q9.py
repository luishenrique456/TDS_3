from q9 import soma_intervalo

assert soma_intervalo(1,5) == 15

# testa user digita errado tipo num1 errado

assert soma_intervalo('a',5) == Exception

assert soma_intervalo(2,4.0) == Exception

assert soma_intervalo('a','b') == Exception

print('teste tudo OK! da questão 9 da lista 1')