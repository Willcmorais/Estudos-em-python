# Pergunte a distãncia de uma viagem em km. Calcule o preço da passagem, cobrando 0,50 por km para viagens até 200km
# e 0,45 para viagens mais longas que 200km
dist = float(input('Informe aqui a distância em Km do local que deseja ir: '))
print('O valor da passagem será informado abaixo, de acordo com a distância informada...')
pssg1 = dist * 0.5
pssg2 = dist * 0.45
if dist <= 200:
    print('O valor da passagem para a distância de {}km ficou em R${:.2f}'.format(dist, pssg1))
else:
    print('O valor da passagem para a distância de {}km ficou em R${:.2f}'.format(dist, pssg2))
##########################################################################################################################

# Um programa que leia um ano qualquer e mostre se ele é BISSEXTO ou não. Para saber se um ano é bissexto ou não, dividimos ele por 4
# Se não houver resto da divisão, então, o ano é bissexto, se não, não é
ano = int(input('Informe o ano que deseja verificar: '))
if ano % 4 == 0:
    print('O ano é bissexto!')
else:
    print('O ano não é bissexto!')
##########################################################################################################################

# um programa que leia dois números e informe qual o maior e qual o menor
n1 = int(input('Informe um número: '))
n2 = int(input('Informe outro número: '))
if n1 > n2:
    print('O maior número é o {} e o menor é {}'.format(n1, n2))
else:
    print('O maior número é o {} e o menor é {}'.format(n2, n1))
