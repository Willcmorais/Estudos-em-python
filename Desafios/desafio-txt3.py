# quero mostrar o primeiro nome e o último
name = input('Informe seu nome completo: ').strip().title().split()
print('Muito prazer em te conhecer!')
print('Seu primeiro nome é {}'.format(name[0]))
# peço que ele pegue o tamanho do len da name e diminua 1 do valor, o valor será referente a posição do último nome, pois ele começa no 0
print('Seu último nome é {}'.format(name[len(name) - 1]))
