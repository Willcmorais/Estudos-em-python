# ler o comprimento do cateto oposto(vertical) e do cateto adjacente(horizontal) de um triângulo retângulo. calcule e mostre o
# comprimento da hipotenusa (ligação entre eles). o quadrado da hipotenusa = a soma dos quadrados dos catetos.
import math
import random
import pygame
########################################################################################################################

co = float(input('informe o valor do cateto oposto: '))
ca = float(input('informe o valor do cateto adjacente: '))
# hi = (co ** 2 + ca ** 2) ** (1 / 2) -> metodo matemático
# a função matemática da hypotenusa, que calcula ela através dos dois valores oferecidos no input acima
hi = math.hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))
########################################################################################################################

# programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo. O eixo horizontal é o sen e o vertical cos
# infomamos qualquer ângulo para saber a medida de sen e cos para achar a tangente (o ponto de encontro com o cículo)
ang = float(input('informe um valor para o ângulo: '))
# porém, as funções de sin,cos e tan retornam radiano, precisa ser transformada com o 'radians'
print('O seu seno é {:.2f}'.format(math.sin(
    math.radians(ang))))  # pega o ângulo digitado, converte para radiano, pega a conversão e calcula o seno dele
print('O seu cosseno é {:.2f}'.format(math.cos(math.radians(ang))))
print('A sua tangente é {:.2f}'.format(math.tan(math.radians(ang))))
########################################################################################################################

# faça um sorteio entre 4 alunos aleatórios
a1 = input('Informe o primeiro nome: ')
a2 = input('Informe o segundo nome: ')
a3 = input('Informe o terceiro nome: ')
a4 = input('Informe o quarto nome: ')
lista = [a1, a2, a3, a4]  # cria uma lista com esses valores (arrays)
print('o nome sorteado foi o {}!'.format(random.choice(lista)))
########################################################################################################################

# fazer um programa que sorteie a ordem de apresentação do trabalho dos alunos
a1 = input('Informe o primeiro grupo: ')
a2 = input('Informe o segundo grupo: ')
a3 = input('Informe o terceiro grupo: ')
a4 = input('Informe o quarto grupo: ')
lista = [a1, a2, a3, a4]  # cria uma lista com esses valores (arrays)
random.shuffle(lista)
print('a ordem dos grupos sorteados foi {}!'.format(lista))
########################################################################################################################

# fazer um programa que abra e reproduza um áudio de um arquivo mp3
pygame.init()  # inicia a bilioteca
pygame.mixer.music.load('gorila.mp3')  # carrega o documento em formato de music informado com o mixer pelo pygame
pygame.mixer.music.play()  # aqui ele vai dar o play na música
input() # precisa colocar para tocar a música
pygame.event.wait()  # aqui ele diz que ele espera o evento terminar para finalizar

