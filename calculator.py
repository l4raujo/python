# Função de Adição 
def add(x, y):
    return x + y

# Função de Subtração 
def subtract(x, y):
    return x - y

# Função de Multiplicação 
def multiply(x, y):
    return x * y

# Função de Divisão
def divide(x, y):
    if y == 0:
        return "Erro! Divisão por zero."
    return x / y

# Apresentação das opções ao usuário
print("Selecione a operação:")
print("1. Adição")
print("2. Subtração")
print("3. Multiplicação")
print("4. Divisão")

# Solicitação de entrada do usuário 
escolha = input("Digite a opção (1/2/3/4): ")

# Solicitação de entrada dos números 
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# Realiza a operação com base na escolha do usuário 
if escolha == '1':
    print("Resultado:", add(num1, num2))
elif escolha == '2':
    print('Resultado:', subtract(num1, num2))
elif escolha == '3':
    print('Resultado:', multiply(num1, num2))
elif escolha == '4':
    print('Resultado:', divide(num1, num2))
else:
    print('Opção inválida')