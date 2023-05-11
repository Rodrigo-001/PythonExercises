''''
Calculadora Simples
    Este programa exibe menu para escolha da operação, recebe 2 numeros e calcula o resultado
    Usado: funções, laço while, in, if, elif
Feito por Rodrigo 08-10

'''

#Função menu()
def menu():
    print('*-* Menu *-*')
    print('1-Adição')
    print('2-Subtração')
    print('3-Multiplicação')
    print('4-Divisão')

    while True:
        op = int(input("Escolha uma operação: "))
        if op in[1,2,3,4]: #verifica se op está contido nessa lista
            break            
        else:
            print("\nOpção incorreta!!") 
    return op

#Função entrada_de_dados()
def entrada_de_dados():
    print('*-* Entrada de Dados *-*')
    num = int(input('Número: '))
    return num

#Função Adicao()
def adicao(n1, n2):
    print('*-* Adição *-*')
    result = n1 + n2
    return result

#Função Subtracao()
def subtracao(n1, n2):
    print('*-* Subtração *-*')
    result = n1 - n2
    return result

#Função Multiplicação
def multiplicacao(n1, n2):
    print('*-* Multiplicação *-*')
    result = n1 * n2
    return result

#Função divisao()
def divisao(n1, n2):
    print('*-* Divisão *-*')
    result = n1 / n2
    return result

#Função imprime()
def imprime(result):
    print('*-* Imprime Resultado *-*')
    print('\nResultado: ', result,'\n')

#Função Controlador()
def controlador(n1, n2, op):
    print('*-* Controlador *-*')
    if op==1:
        result = adicao(n1, n2)
    elif op==2:
        result = subtracao(n1, n2)
    elif op==3:
        result = multiplicacao(n1, n2)
    elif op==4:
        result = divisao(n1, n2)
    else:
        result = 'Opção inválida!'            
    return result

#======================================
#Programa Principal
print('*-* Principal *-*')
op = menu()
n1 = entrada_de_dados()
n2 = entrada_de_dados()
result = controlador(n1, n2, op)
imprime(result)

# Algoritmo soma
'''
1recebe operação escolhida de função menu guarda na variavel op
2recebe numero vindo de entrada de dados e guarda em n1
3recebe numero vindo de entrada de dados e guarda em n2
4executa função controlador, passando como parametros os valores guardados em op, n1 e n2 e atribui à variável result.
5executa função imprime passando variavel result como parametro

'''