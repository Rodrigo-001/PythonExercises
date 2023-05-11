''''
Tabuada com funções
    Este programa recebe a tabuada desejada tal como o tamanho dela e imprime na tela
    
Feito por Rodrigo 08-10

'''

def tabuada():
    tabuada = int(input('Qual tabuada deseja realizar? '))
    return tabuada

def tamanho_tabuada():
    tamanho = int(input('Digite o tamanho da tabuada em número:  '))
    return tamanho

# função executa_tabuada
def executa_tabuada(tabuada,tamanho_tabuada ):
    cont = 1
    for i in range(1,(tamanho_tabuada+1)):
        cont *= i
        print(f'{tabuada} x {i} = {cont}')
        cont = tabuada
    print("Fim")

# Programa principal
nr_tabuada = tabuada()
tamanho = tamanho_tabuada()
executa_tabuada(nr_tabuada,tamanho)

# Continuar: fazer a tabuada funcionar com funções