# Pergunte a distãncia de uma viagem em km. Calcule o preço da passagem, cobrando 0,50 por km para viagens até 200km
# e 0,45 para viagens mais longas que 200km
print('-=-' * 20)
print('VERIFIQUE AQUI O VALOR DA PASSAGEM. INFORME A DISTÂNCIA EM KM DO LOCAL QUE DESEJA IR')
print('-=-' * 20)
dist = float(input('Informe a distância: '))
print('CALCULANDO...')
pssg1 = dist * 0.5
pssg2 = dist * 0.45
if dist <= 200:
    print('O valor da passagem para a distância de {}km ficou em R${:.2f}'.format(dist, pssg1))
else:
    print('O valor da passagem para a distância de {}km ficou em R${:.2f}'.format(dist, pssg2))
print(' ')
##########################################################################################################################

# Um programa que leia um ano qualquer e mostre se ele é BISSEXTO ou não. Para saber se um ano é bissexto ou não, dividimos ele por 4
# Se não houver resto da divisão, então, o ano é bissexto, se não, não é
print('-=-' * 20)
print('INFORME ABAIXO O ANO QUE DESEJA VERIFICAR E EU TE DIREI SE É BISSEXTO!')
print('-=-' * 20)
ano = int(input('Informe o ano: '))
if ano % 4 == 0:
    print('O ano é bissexto!')
else:
    print('O ano não é bissexto!')
print(' ')
##########################################################################################################################

# um programa que leia dois números e informe qual o maior e qual o menor
print('-=-' * 20)
print('AGORA, INFORME ABAIXO DOIS NÚMEROS QUAISQUER. VOU TE FALAR QUAL O MENOR E QUAL O MAIOR')
print('-=-' * 20)
n1 = int(input('Informe um número: '))
n2 = int(input('Informe outro número: '))
if n1 > n2:
    print('O maior número é o {} e o menor é {}'.format(n1, n2))
else:
    print('O maior número é o {} e o menor é {}'.format(n2, n1))
