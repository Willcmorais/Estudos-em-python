# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento
# para sal superiores a 1.250, calcular aumento de 10% e para inferiores ou iguais, aumento de 15%
sal = float(input('Informe aqui o seu salário atual: '))
aumnt1 = sal * 0.1
aumnt2 = sal * 0.15
if sal > 1250:
    print(
        'O salário atual é de R${}, receberá um aumento de 10%, ou seja R${}. O valor final do reajuste será R${}'.format(
            sal, aumnt1, sal + aumnt1))
else:
    print(
        'O salário atual é de R${}, receberá um aumento de 15%, ou seja R${}. O valor final do reajuste será R${}'.format(
            sal, aumnt2, sal + aumnt2))
##########################################################################################################################

# Desenvolver um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo
l1 = int(input('Informe um valor para o primeiro lado: '))
l2 = int(input('Informe um valor para o segundo lado: '))
l3 = int(input('Informe um valor para o terceiro lado: '))
if l1 + l2 > l3:
    print('O triângulo pode ser formado!')
if l1 + l3 > l2:
    print('O triângulo pode ser formado!')
if l3 + l2 > l1:
    print('O triângulo pode ser formado!')
else:
    print('O triângulo não pode ser formado!')
