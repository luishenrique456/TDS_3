# 12) Deseja-se publicar o número de acertos de cada aluno em uma prova em forma de testes. A
# prova consta de 30 questões, cada uma com cinco alternativas identificadas por A, B, C, D e E.
# Para isso são dados:
# o cartão gabarito;
# o número de alunos da turma;
# o cartão de respostas para cada aluno, contendo o seu número e suas respostas.
import random

def gera_resposta(num_questao):
    lista_questao = []
    alternativa = ['A','B','C','D']
    for i in range(num_questao):
        lista_questao.append(random.choice(alternativa))
    return lista_questao

def resposta_aluno():
    gabarito = gera_resposta(30)
    resp_aluno = gera_resposta(30)
    acertos = 0
    for i in range(len(gabarito)):
        if resp_aluno[i] == gabarito[i]:
            acertos += 1
            
    return gabarito , resp_aluno , acertos


        








def main():
    while True:
        try:
            
            gabarito , respo_aluno , acerto = resposta_aluno()
            print(f'Gabarito {gabarito}')
            print(f'Resposta do Aluno {respo_aluno}')
            print(f'Acertos do Aluno {acerto}')

            

            

            break
        except ValueError:
            print('Valor invalidor')





if __name__ == '__main__':
    main()