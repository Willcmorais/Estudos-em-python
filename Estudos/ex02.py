nome = input('informe o seu nome: ')  # ou nome = str(input('texto'))

# faz com que, crie um espaço de 20 caracteres para o espaço na memória
print('Prazer em te conhecer, {:20}!'.format(nome))
print('Prazer em e conhecer, {:>20}!'.format(nome))  # coloca os espaços que sobram antes do nome
print('Prazer em te conhecer, {:^20}!'.format(nome))  # centraliza o nome em 20 espaços
# centraliza o nome no meio de 20 espaços e nos espaços livres adiciona o símbolo de '='
print('Prazer em te conhecer, {:=^20}!'.format(nome))
print('Prazer em te conhecer, {:.^20}!'.format(nome))

n1 = int(input('Informe um número: '))
n2 = int(input('informe outro número: '))
# criamos sem variável e formatando direto. Quando precisamos desse valor depois, em algum outro processo, eu crio, se não, pode formatar direto
# print('A soma desses números é {}'.format(n1 + n2))
s = n1 + n2
sub = n1 - n2
div = n1 / n2
mult = n1 * n2
fat = n1 ** n2
rest = n1 % n2
pInt = n1 // n2

print(
    'A soma entre {} e {} é {}\nA subtração é {}\nA divisão é {}\nA múltiplicação é {}\nO fatorial é {}\nO resto da divisão é {}\nA parte inteira do resultado é {}'.format(
        n1, n2, s, sub, div, mult, fat, rest, pInt))
