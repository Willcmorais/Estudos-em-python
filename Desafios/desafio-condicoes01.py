# Escreva um programa que faça o computador "pensar" num número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi
# o número escolhido pelo computador. O programa deverá escrever na tela se venceu ou perdeu
from random import randint

print('-=-' * 20)  # faz com que printemos o que está informado 20 vezes
print('SORTEEI UM NÚMERO ENTRE 0 E 5, ACHA QUE CONSEGUE ADIVINHAR?')
print('-=-' * 20)
n1 = randint(0, 5)  # faz com que o n1 receba um número aleatório que o computador sortear entre 0 e 5
n2 = int(input('Informe um número inteiro entre 0 e 5: '))  # recebe a tentativa de chute
print('PROCESSANDO SUA RESPOSTA...')
# se um valor for igual ao outro vai dizer que acertamos, se não, diz que erramos
print(
    'Parabéns! Você acertou o número sorteado.' if n1 == n2 else 'Que pena, você errou! Tente novamente mais tarde.')
print('')
##########################################################################################################################

# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80, mostre que ele foi multado. A multa vai custar 7 por cada km acima do limite
print('-=-' * 20)
print('RADAR ELETRÔNICO! LIMITE DE VELOCIDADE: 80KM/H')
print('-=-' * 20)
vel = randint(50, 100)
print('O veículo passou no radar com a velocidade de {}km/h'.format(vel))
if vel <= 80:
    print('Está tudo bem, o veículo está no limite de velocidade!')
else:
    multa = (vel - 80) * 7
    velExc = vel - 80
    print('O veículo excedeu o limite de 80km/h permitido pelo radar. O excesso foi de {}km'.format(velExc))
    print('O valor da multa será aplicada de acordo com a velocidade excedida...')
    print('==== VALOR DA MULTA: R${:.2f} ===='.format(multa))
print('')
##########################################################################################################################

# Escreva se o número informado foi par ou impar.
print('-=-' * 20)
print('INFORME UM NÚMERO E DIREI A VOCÊ SE ELE É PAR OU É IMPAR')
print('-=-' * 20)
num = int(input('Informe o número: '))
print('PROCESSANDO SUA RESPOSTA...')
# Se o resto da divisão do número por 2 for igual a 0, quer dizer que o número é par, se não é impar.
# Pois, números pares quando dividimos por 2 vai sempre dar resto 0.
print('O número informado é PAR!' if num % 2 == 0 else 'O número informado é IMPAR!')
