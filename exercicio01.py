# CRIE UM PROGRAMA QUE LEIA UM NUMERO INTEIRO E DIGA SE O NÚMERO É PAR OU ÍMPAR, USE %

numero = int(input('Digite um número: '))

if numero % 2 == 0:
    print(numero, "é um número par.")
else:
    print(numero, 'é um número impar.')