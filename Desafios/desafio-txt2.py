# Vai pegar o nome da minha cidade, transformar para apenas primeira letra em maiúsculo e vai perguntar se tem esse nome nela, se tiver é tru
city = str(input('Informe qual é a sua cidade: ')).strip().upper()
# print(city [:6] == 'Recife') -> se tiver escrito recife vai retornar true, se não, retorna false e não considera os espaços antes e depois
print('RECIFE' in city)

# quero saber se existe o nome 'Morais' no que for digitado
nome2 = str(input('Informe seu nome completo: ')).strip().lower()
print('morais' in nome2)  # operador in do python, não é um metodo

# quero saber quantas letras a tem na frase, em qual posição o primeiro a está e a posição da ultima letra a
letras = str(input('Digite uma frase aqui: ')).strip().lower()
print('A letra a apareceu {} vezes na frase'.format(letras.count('a')))
# adiciona +1 para facilitar visualmente a conta
print('A primeira letra a apareceu na posição {}'.format(letras.find('a') + 1))
# faz com que o find inicie da direita para esquerda
print('A última letra a apareceu na posição {}'.format(letras.rfind('a') + 1))
