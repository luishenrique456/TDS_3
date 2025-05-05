#Faça um programa que leia a altura e o sexo 
# 1 para feminino e 2 para masculino
# uma função calcular peso ideal que receba altura e o sexo via parâmetro
#e que calcule e retorne seu peso ideal formula

def peso_ideal(sexo,altura):
    if not isinstance(altura,float) or not 0 <= altura:
        return 'valor inválido na altura'

    if not isinstance(sexo,int) or not 1<= sexo <= 2:
        return 'opção inválida'

    if sexo == 1:
        resul_femino = (62.1*altura) - 44.7
        return round(resul_femino,2)
    elif sexo == 2:
        resul_masculino = (72.7*altura) - 58
        return round(resul_masculino,2)
    
assert peso_ideal(1,1.60) == 54.66

assert peso_ideal(2,1.70) == 65.59

#testa se user digita opção do sexo errado
assert peso_ideal('a',1.50) == 'opção inválida'

assert peso_ideal(-3,1.80) == 'opção inválida'

#testa se user digite tipo da altura errado
assert peso_ideal(1,'b') == 'valor inválido na altura'

assert peso_ideal(2,-3.0) == 'valor inválido na altura'

print('teste tudo OK! da questão 5 lista 1')