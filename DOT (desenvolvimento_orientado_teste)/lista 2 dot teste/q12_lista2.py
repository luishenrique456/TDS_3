# 12) Deseja-se publicar o número de acertos de cada aluno em uma prova em forma de testes. A
# prova consta de 30 questões, cada uma com cinco alternativas identificadas por A, B, C, D e E.
# Para isso são dados:
# o cartão gabarito;
# o número de alunos da turma;
# o cartão de respostas para cada aluno, contendo o seu número e suas respostas.

def resposta_aluno(lista_questao : list[str]):
    if type(lista_questao) != list or not all(isinstance(i,str) and i.strip() for i in lista_questao) or len(lista_questao) == 0:
        return Exception


    

    gabarito = ['B', 'D', 'C', 'C', 'B', 'D', 'A', 'A', 'A', 'D', 'D', 'D', 'C', 'A', 'A', 'C', 'D', 'C', 'A', 'A', 'B', 'B', 'A', 'A', 'C', 'C', 'B', 'B', 'D', 'A']

    acerto = 0

    for i in range(len(gabarito)):
        if lista_questao[i] == gabarito[i]:
            acerto += 1

    return acerto

assert resposta_aluno(['C', 'A', 'B', 'C', 'C', 'C', 'B', 'B', 'D', 'C', 'C', 'D', 'A', 'D', 'D', 'B', 'C', 'C', 'B', 'C', 'C', 'B', 'A', 'A', 'C', 'B', 'C', 'A', 'B', 'C']) == 7

#verficar parâmetro é tipo list

assert resposta_aluno(3.6) == Exception

assert resposta_aluno(2) == Exception

#verficar elemento da list é str

assert resposta_aluno([]) == Exception

assert resposta_aluno([1]) == Exception

assert resposta_aluno([3.4]) == Exception

assert resposta_aluno(['']) == Exception

print('Teste tudo OK! da questão 12 da lista 2 ')