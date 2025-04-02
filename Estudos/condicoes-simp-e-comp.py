# Condições são tipos de caminhos que podem ser feitos de um ponto até outro de formas diferentes.
# É feito por uma estrutura sequencial de instruções, ou é executado uma intrução, ou é exucatada outra, nunca terão duas.
# Utilizamos o 'if' para estruturas simples e 'if e else' para compostas.
########################################################################################################################

tempo = int(input('Quantos anos tem seu carro: '))
# Outra forma de representar o if. print Carro novo se o tempo for menor ou igual a 3, senão, print carro velho.
print('Carro Novo!' if tempo <= 3 else 'Carro Velho!')
# if tempo <= 3:
#    print('Carro Novo!')
# else:
#    print('Carro Velho!')
print('---- FIM ----')
########################################################################################################################

# informa o nome e se esse nome for William ele vai printar duas mensagens, se não, vai printar apenas uma.
nome = str(input('Informe o seu nome: '))
if nome == 'William':
    print('Que nome lindo você tem!')
print('Olá, {}. Tenha um bom dia.'.format(nome))
########################################################################################################################

# pega a nota1 e a 2, tira a média e se for acima mostra uma coisa, se não mostra outra.
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
print('A sua média foi {}'.format(m))
# ou print('O aluno está abaixo da média. ESTUDE MAIS!' if m < 7 else 'o aluno alcançou a média da disciplina. PARABÉNS!')
if m < 7:
    print('O aluno está abaixo da média na disciplina. ESTUDE MAIS!')
else:
    print('O aluno alcançou a média da disciplina. PARABÉNS!')
print('==== FIM =====')
########################################################################################################################




