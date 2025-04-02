from math import trunc

num = float(input('Informe um número real: '))
print('O número real transformado em inteiro é {}'.format(trunc(num)))
########################################################################################################################

preco = float(input('Informe o preço do produto: '))
desc5 = preco - (preco * 0.05)
desc10 = preco - (preco * 0.10)
desc15 = preco - (preco * 0.15)
print('O valor do produto R$ {:.2f}, com desconto de 5% fica R$ {:.2f}'.format(preco, desc5))
print('O valor do produto R$ {:.2f}, com desconto de 10% fica R$ {:.2f}'.format(preco, desc10))
print('O valor do produto R$ {:.2f}, com desconto de 15% fica R$ {:.2f}'.format(preco, desc15))
########################################################################################################################

sal = float(input('Informe o seu salário: '))
aumento15 = sal + (sal * 0.15)
print('O salário anterior era de R$ {:.2f} e o valor com o reajuste de 15% ficou R$ {:.2f}'.format(sal, aumento15))
########################################################################################################################

km = float(input('Quantos quilômetros foram rodados durante o período de aluguel: '))
qntDias = int(input('Informe por quantos dias contratou o serviço de aluguel: '))
valorFinal = (60 * qntDias) + (0.15 * km)
print('O valor a ser pago pelo serviço do aluguel por {} dias e {:.3f}km rodados é:\nR$ {:.2f}'.format(qntDias, km,
                                                                                                       valorFinal))
