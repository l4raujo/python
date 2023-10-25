vel = int(input('Digite a velocidade: '))
result = vel - 80
result1 = result * 7 


if vel <= 80:
    print('Você está dentro da velocidade permitida')
else:
    print(f'Você ultrapassou a velocidade permitida, o valor a ser pago da multa é de R$ {result1}')    