# Escreva um programa que faça o computador "pensar" num número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi
# o número escolhido pelo computador. O programa deverá escrever na tela se venceu ou perdeu
from random import randint

print('-=-' * 20)  # faz com que printemos o que está informado 20 vezes
print('\033[7m SORTEEI UM NÚMERO ENTRE 0 E 5, ACHA QUE CONSEGUE ADIVINHAR? \033[m')
print('-=-' * 20)
n1 = randint(0, 5)  # faz com que o n1 receba um número aleatório que o computador sortear entre 0 e 5
n2 = int(
    input('Informe um número inteiro entre \033[1;32m0\033[m e \033[1;32m5\033[m:  '))  # recebe a tentativa de chute
print('PROCESSANDO SUA RESPOSTA...')
# se um valor for igual ao outro vai dizer que acertamos, se não, diz que erramos
print(
    '\033[1;32mParabéns! Você acertou o número sorteado.\033[m' if n1 == n2 else '\033[1;31mQue pena, você errou! Tente novamente mais tarde.\033[m')
print('')
##########################################################################################################################

# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80, mostre que ele foi multado. A multa vai custar 7 por cada km acima do limite
print('-=-' * 20)
print('\033[1;;41m RADAR ELETRÔNICO! LIMITE DE VELOCIDADE: 80KM/H \033[m')
print('-=-' * 20)
vel = randint(50, 100)
print('O veículo passou no radar com a velocidade de \033[7m {}km/h \033[m'.format(vel))
if vel <= 80:
    print('\033[1;32mEstá tudo bem, o veículo está no limite de velocidade!\033[m')
else:
    multa = (vel - 80) * 7
    velExc = vel - 80
    print('\033[1;31mO veículo excedeu o limite de 80km/h permitido pelo radar. O excesso foi de {}km\033[m'.format(
        velExc))
    print('O valor da multa será aplicada de acordo com a velocidade excedida...')
    print('\033[1;30;43m ==== VALOR DA MULTA: R${:.2f} ==== \033[m'.format(multa))
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
