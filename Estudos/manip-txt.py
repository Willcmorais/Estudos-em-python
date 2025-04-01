# Manipulando cadeias de textos (strings), está entre aspas ' ' ou " ". no exemplo frase = ('Curso em video python') temos 21 caractéres (0-20)
# FATIAMENTO: frase[9] -> o colchete é relacionado a listas. pega apenas a letra que está no índice daquela string.
# podemos também utilizar o comando frase(9:13), pega tudo que está entre a posição 9 e antes do 13. ou seja, para pegar a palavra video é frase(9:14)

frase = ('Curso em Video Python')
frase2 = ('   Aprenda Python  ')

# FATIAMENTO
print(frase[0:5])  # printa o Curso
print(frase[6:8])  # printa o em
print(frase[9:14])  # printa o Video
print(frase[15:21])  # printa o Python
print(frase[0:8:2])  # printa do 'Curso em' pulando de duas em duas casas (Croe)
print(frase[:5])  # quando não colocaos aonde ele começa quer dizer que ele inicia no 0 e vai até onde foi informado
print(frase[15:])  # falamos que vai se iniciar no espaço 15 e vai até o final
print(frase[9::3])  # falamos que vai se iniciar no espaço 9, vai até o final da sentença e pulando de 3 em 3

# ANÁLISES
print(len(frase))  # retorna a quantidade de espaços no container da variável
print(frase.count('o'))  # vai contar quantas vezes o 'o' aparece na sentença
print(frase.count('o', 0, 14))  # pega quantas letras 'o' existem entre o espaço de 0 até 14
print(frase.find('deo'))  # pega na sentença aonde inicia o 'deo'
print(frase.find('Android'))  # como não existe ele aparece -1, ou seja uma sentença falsa
print('Curso' in frase)  # pergunta se na variável frase existe a palavra 'Curso', se sim, ele retorna como true

# TRANSFORMAÇÃO
# Não conseguimos mexer direito nos elementos de uma lista, mas podemos utilizar os métodos para mexer nela.
# Faz com que aonde existia 'Python' atualize para 'Android'. Não substitui direto na string
frase.replace('Python', 'Android')
print(frase.upper())  # printa na tela o que está escrito só que em maiúsculo, podemos usar também o lower.
print(frase.capitalize())  # joga todos os caractéres para minúsculo e só o primeiro caractere ficará maiúsculo
# analiza quantas palavras tem na string e transforma a primeira letra de todas as palavras em maiúsculo
print(frase.title())
print(len(frase2))  # mostra quantos caracteres tem na string da 'frase2'
print(frase2)
# ignora os espaços entre o primeiro caractere vazio e antes do próximo que tenha algum valor, e os após o último caractere
print(frase2.strip())
print(frase2.rstrip())  # faz com que só retire os espaços vazios da direita
print(frase2.lstrip())  # tira apenas os espaços vazios da esquerda

# DIVISÃO
# ele divide a string a partir dos espaços vazios entre os caracteres e coloca ordenado em outra lista
print(frase.split())

# FUNÇÃO
print('-'.join(frase))  # coloca nos espaços entre cada caractere um '-'
# Vai separar os caracteres em uma lista a partir dos seus espaços vazios e antes de cada va colocar '-'
print('-'.join(frase.split()))
