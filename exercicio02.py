# DESENVOLVA UM PROGRAMA QUE PERGUNTE A DISTÂNCIA DE UMA VIAGEM E CALCULE O PREÇO DA PASSAGEM,
# COBRANDO R$ 0,50 POR KM EM VIAGENS ATE 200KM E R$ 0,45 EM VIAGENS ACIMA DE 200KM.

viagem = float(input('Qual a distância de sua viagem? '))
viagem1 = viagem * 0.50
viagem2 = viagem * 0.45

if viagem <= 200:
    print('O preço da sua viagem irá custar: ', viagem1)
else:
    print('O preço da sua viagaem irá custar: ', viagem2)