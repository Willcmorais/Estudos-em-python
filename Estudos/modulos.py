# módulos ou packages pelo comando 'import'. Para importar algo limitado de uma biblioteca utilizamos o 'from import'
# exemplo: import bebida ou para fazer a importação detalhada from bebida import coca
# um exemplo de biblioteca é a 'import math' para fazer arredondamentos, podemos utilizar a funcionalidade 'ceil' p/ arredondar para baixo
# e utilizar o 'floor' p/ arredondar p/ baixo. 'trunc' ele elimina da ',' para frente. 'pow' para potencia. 'sqrt' para calcular a raiz quadrada.
# 'factorial' para calcular um fatorial. além de outras. p/ importar duas funcionalidades fazemos o 'from math import pow, ceil'

from math import sqrt, ceil
import random
import emoji

n1 = int(input('Informe um número: '))
# o randint me da um número aleatório entre dois números escolhidos
n2 = random.randint(1, 100)
print('O número aleatório escolhido foi: {}'.format(n2))
# random.random() faz com que me de um número aleatório entre 0 e 1
raiz = sqrt(n1)
raiz2 = sqrt(n2)
acresc = ceil(raiz2)
# se o import fosse do math inteiro, teriamos que chamar a funcionalidade 'raiz = math.sqrt(n1)'
print('A raiz de {} é {:.2f} '.format(n1, raiz))
print('A raiz de {} arredondada para cima é {:.0f}'.format(n2, acresc))
print('A raiz de {} arredondada para baixo é {:.0f}'.format(n2, acresc))
print('A raiz não arredondada de {} é {}'.format(n2, raiz2))
print(emoji.emojize('Olá, mundo! :smiling_face_with_sunglasses:'))
