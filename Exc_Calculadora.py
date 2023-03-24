#Programa que simula uma calculadora simples. 
# Feito em 24-03

print('--------------------')
print('CALCULADORA SIMPLES')
print('--------------------')
print('\nEscolha a operação\n')

print('1 - Adição')
print('2 - Subtração')
print('3 - Multiplicação')
print('4 - Divisão')
op = int(input('\nOperação: \n'))

n1 = int(input('\nNumero 1: '))
n2 = int(input('Numero 2: '))

match op:
    case 1:
        r = n1 + n2
    case 2:
        r = n1 - n2
    case 3:
        r = n1 * n2
    case 4:
        r = n1 / n2
    case _:
        r = 'nd'

# Teste do valor de r, antes da impressão
if r != 'nd':
    print('\nResultado: ', r)
else: 
    print('\nOpção inválida!')
