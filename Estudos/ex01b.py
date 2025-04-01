n = float(input('Digite um valor: '))
print(n)
print(type(n))

n = str(input('Digite um valor: '))
print(n)
print(type(n))

n = int(input('Digite um valor: '))
print(n)
print(type(n))

n = bool(input('Digite um valor: '))  # se tiver um valor dentro de bool ele é true, se não é false
print(n)
print(type(n))

n = input('Digite um valor: ')
print(n)
print(type(n))
print(n.isnumeric())  # pergunta se o valor é númerico
print(n.isalpha())  # pergunta se o valor é string
print(n.isupper())  # pergunta se o valor está somente em maiúsculo
print(n.isspace())  # é somente espaços?

# operadores aritméticos: +, -, *, /, % (resto da divisão), // (divisão inteira), ** (fatoral(elevado))
# ordem de precedência: () -> ** -> *, /, //, % -> +, -
