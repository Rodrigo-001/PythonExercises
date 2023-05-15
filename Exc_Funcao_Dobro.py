'''
Este programa le um numero do teclado, calcula o dobro e imprime.
Funções: entrada de dados, calcular o dobro, imprimir resultado, programa principal

Feito por Rodrigo em 14-05'''

def entrada_dados():
    nr = int(input("\nNumero: \n"))
    return nr
def calcular_dobro(nr):
    dobro = nr * 2
    return dobro
def imprimir_resultado(dobro):
    print(f'\nO dobro de {nr} é {dobro}\n')

# **Principal**
nr = entrada_dados()
dobro = calcular_dobro(nr)
imprimir_resultado(dobro)
print("Fim")
