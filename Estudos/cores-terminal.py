# padrão ANSI (Padrão de normalização internacional). tem o escape sequences para utilizar no terminal. tudo antes do código
# começa com \. por exemplo, para representar cores no terminal iniciamos o código com '\033[m' (entre o 'colchetes' e o 'm'
# escreveremos o código). essa coisas entre os colchetes e o m pode ser nenhum código, 1, 2 ou 3 códigos
# exemplo com 3 códigos = \033[Style; Text; Background m

# Códigos para estilo = 0 - sem estilo, 1 - negrito, 4 - underline, e 7 - inverte as configurações, o que está em letra vai
# p/ o fundo e o que estiver no fundo vai p/ letra;

# Códigos para texto = 30 até 37. Ordem de cores: branco, vermelho, verde, amarelo, azul, lilás, azul claro, cinza

# Códigos para background = iguais ao de texto, porém, vai de 40 até 47

print('\033[7;40m Olá')
print('\033[1;31;40m Olá 2')
# 7 faz inverter, como não botamos parâmetro para o fundo e ele é preto por padrão, ele se torna branco
# o 40 é o branco, então faz com que fique com o texto fique com a letra preta
