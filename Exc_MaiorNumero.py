# Este programa recebe N números do usuário, obtém o maior número e o imprime na tela.
# A operação é encerrada ao digitar zero
# Feito em 14-04 por Rodrigo 

# --------------------
# ALGORITMO DESCRITIVO
# --------------------
# recebe valor e guarda em num
# cria maiorNum e guarda num dentro dela
# laço: enquanto num for diferente de 0:
    # condicional: Se num for maior que 'maiorNum':
        # imprima que num foi guardado
        # guarde num em maiorNum
    #peça outro numero e guarde em num
#se numero digitado for diferente de zero imprima o numero da tela
#senão, peça para o usuário digitar um numero diferente de zero

print('--------------------')
print('Obtém o maior número')
print('--------------------\n\n')

num = int(input('Digite um número: '))
maiorNum = num
while num != 0:
    if num > maiorNum:
        print(f'O numéro {num} foi guardado')
        maiorNum = num
    num = int(input('Digite outro: '))
if maiorNum != 0:
    print(f'\nMaior: {maiorNum}\n')
else:
    print('\n\nO numero precisa ser diferente de zero!!\n')
