name = str(input('Digite seu nome completo: ').strip())  # tira os espaços que podem aparecer antes ou depois do nome
print('Analisando nome........')
print('O nome transformado para maiúsculo: {}'.format(name.upper()))
print('O nome transformado para minúsculo: {}'.format(name.lower()))
# conta quantas letras tem no nome inteiro com os espaços depois subtrai a quantidade de espaços que tem no nome
print('Seu nome tem {} letras'.format(len(name) - name.count(' ')))
# vai pegar quantos caracteres leva até achar o primeiro espaço e vai mostrar qual posição ele está
# print('Seu primeiro nome tem {} letras'.format(name.find(' ')))
separa = name.split()  # separa vai receber o nome separado pos listas, o primeiro nome inicia no 0
# vai mostrar meu primeiro nome que está localizado na posição da lista 0 e a quantidade de espaços que ele tem
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))
