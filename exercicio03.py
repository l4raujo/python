# FAÇA UM PROGRAMA QUE LEIA 3 NÚMEROS INTEIROS E DIGA QUAL É O MAIOR E O MENOR ENTRE ELES

numero1 = int(input('Digite um número: '))
numero2 = int(input('Digite um segundo número: '))
numero3 = int(input('Digite um terceiro número: '))

# PARA DEFINIR O MENOR 

menor = numero1

if numero2 < numero1 and numero2 < numero3:
    menor = numero2

if numero3 < numero1 and numero3 < numero2:
    menor = numero3

# PARA O MAIOR 

maior = numero1

if numero2 > numero1 and numero2 > numero3: 
    maior = numero2
if numero3 > numero1 and numero3 > numero2:
    maior = numero3

# APARECER NA TELA 

print(f'O maior número é o {maior}')
print(f'O menor número é o {menor}')
