# Questão 8 DOT
#Escreva uma função que lê um caractere digitado pelo usuário e retorna este caractere
#somente se ele for igual a S ou N .Se o caractere não for nem S nem N
#a função imprime a mensagem 'Caractere inválido.Digite novamente.
#use esta função em um programa que fica lendo do usuário um número qualquer e imprime este número ao cubo na tela
#O programa deve ficar lendo os números até o usuário responde N à pergunta se ele deseja continuar ou não.
def opcao(caract):
    # caract = input('Deseja continua aperta S ou N para encerrar : ').upper()
    if caract != 'S' and caract != 'N':
        return 'entrada inválida'

    if caract == 'S':
        return 'S'
    elif caract == 'N':
        return 'N'
    
assert opcao('S') == 'S'

assert opcao('N') == 'N'

assert opcao('a') == 'entrada inválida'

print('teste tudo OK! da questão 8 da lista 1')