nome = input('Qual é o seu nome: ')
# print('É um grande prazer te conhecer,', nome)
# o {} formata o que vier após ele dentro do format()
print('É um grande prazer em te conhecer, {}!'.format(nome))

n1 = int(input('Informe um número: '))
print(type(n1))

n2 = int(input('Informe outro número: '))
print(type(n2))

s = n1 + n2

print('A soma vale {}'.format(s))
print('A soma entre {} e {} vale {}'.format(n1, n2, s))
