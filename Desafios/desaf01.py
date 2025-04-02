n = int(input('Informe um número: '))
# suc = n + 1
# ant = n - 1
# print('O número escolhido foi {}. O seu sucessor é o {} e o seu antecessor é o {}'.format(n, suc, ant))
# como aqui temos poucas variantes, podemos utilizar o formatador para fazer a conta direto
print('O número escolhido foi {}. O seu sucessor é o {} e o seu antecessor é o {}'.format(n, (n + 1), (n - 1)))
n1 = int(input('Informe outro número: '))
doub = n1 * 2
trip = n1 * 3
raiz = n1 ** (1 / 2)  # para tirar a raiz quadrada
print('O número informado foi {}. O dobro dele é {}, o triplo {}, e a raiz quadrada é {}'.format(n1, doub, trip, raiz))
########################################################################################################################

nota1 = float(input('Informe a sua primeira nota: '))
nota2 = float(input('Informa a sua segunda nota: '))
print('Suas notas foram AV1 {} e AV2 {}\nSua média na disciplina foi de {}'.format(nota1, nota2, (nota1 + nota2) / 2))
########################################################################################################################

valor = float(input('Informe o valor em metros: '))
# utiliza o {:.0f} para mostrar sem casa decimal
print('O valor informado {}m tem {:.0f}cm e {:.0f}mm'.format(valor, (valor * 100), (valor * 1000)))
########################################################################################################################

num = int(input('Informe o número da tabuada você quer visualizar: '))
print('{} x {:2} = {}'.format(num, 1, num))
print('{} x {:2} = {}'.format(num, 2, num * 2))
print('{} x {:2} = {}'.format(num, 3, num * 3))
print('{} x {:2} = {}'.format(num, 4, num * 4))
print('{} x {:2} = {}'.format(num, 5, num * 5))
print('{} x {:2} = {}'.format(num, 6, num * 6))
print('{} x {:2} = {}'.format(num, 7, num * 7))
print('{} x {:2} = {}'.format(num, 8, num * 8))
print('{} x {:2} = {}'.format(num, 9, num * 9))
print('{} x {} = {}'.format(num, 10, num * 10))
########################################################################################################################

valor = float(input('Informe quanto em R$ você tem na carteira: '))
dol = valor / 5.74
eur = valor / 6.19
francSuic = valor / 6.5
print(
    'Você tem R$ {:.2f} em sua carteira.\nA conversão em US$ {:.2f} (Dólar)\nA conversão em € {:.2f} (Euro)\nA conversão em CHF {:.2f} (Franco suiço)'.format(
        valor, dol, eur, francSuic))
########################################################################################################################

larg = float(input('Informe a largura da parede: '))
alt = float(input('Informe a altura da parede: '))
areaPintar = larg * alt
print('A parede tem dimensão de {:.2f}x{:.2f}\nA sua área é de {:.2f}m².'.format(larg, alt, areaPintar))
pintura = (areaPintar / 2)  # para cada m² é utilizado 2l de tinta
print('A quantidade de tinta necessário para pintar {:.2f}m² é de {:.2f}l'.format(areaPintar, pintura))
