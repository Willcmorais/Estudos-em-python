# Analisa o nome, transforma para maiúsculo e minúsculo, conta quantas letras tem o nome sem espaços e diz o primeiro nome com qnt de letras
# variável que recebe um input str.
name = str(input('Digite seu nome completo: ').strip())  # tira os espaços que podem aparecer antes ou depois do nome

print('Analisando nome........')
print('O nome transformado para maiúsculo: {}'.format(name.upper()))
print('O nome transformado para minúsculo: {}'.format(name.lower()))
# conta quantas letras tem no nome inteiro com os espaços depois subtrai a quantidade de espaços que tem no nome
print('Seu nome tem {} letras'.format(len(name) - name.count(' ')))
# vai pegar quantos caracteres leva até achar o primeiro espaço e vai mostrar qual posição ele está
# print('Seu primeiro nome tem {} letras'.format(name.find(' ')))
separa = name.split()  # separa vai receber o nome separado das listas, o primeiro nome inicia no 0
# vai mostrar meu primeiro nome que está localizado na posição da lista 0 e a quantidade de espaços que ele tem
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))

# vai dizer qual número está na unidade, na dezena, na centena e na unidade a partir de uma fórmula matemática
# num = str(input('Digite um número: '))
num = int(input('Digite um número: '))
u = num % 10  # vai pegar o número, dividir por 10, e o resto da divisão será a unidade
d = num // 10 % 10  # vai pegar o número dividir por 10, pegar o resto inteiro da divisão e dividir por 10 novamente
c = num // 100 % 10
m = num // 1000 % 10
print('Analisando número.......')
# print('O número presente na casa das unidades é o {}'.format(num[3]))
# print('O número presente na casa das dezenas é o {}'.format(num[2]))
# print('O número presente na casa das centenas é o {}'.format(num[1]))
# print('O número presente na casa do milhar é o {}'.format(num[0]))
print('UNIDADE: {}'.format(u))
print('DEZENA: {}'.format(d))
print('CENTENA: {}'.format(c))
print('MILHAR: {}'.format(m))
