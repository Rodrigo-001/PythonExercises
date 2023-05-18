'''
AULA 12-05 - TRABALHANDO COM LISTAS
    Este programa recebe tamanho da lista, percorre os elementos usando for in e imprime-os na tela. 
    Usado: funções, lista
Feito por Rodrigo 12-05

'''

def tamanho_da_lista():   
    '''--função sem parametro
        retorna t
        valor recebido do usuário--''' 
    print("-*TAMANHO DA LISTA-*")
    t = int(input("Tamanho da lista: "))
    return t

def criar_lista(t):    
    '''--retorna uma lista
    --parametro:--
        t
    --retorno:string
        --o valor de t determina quantos números o função irá solicitar
    '''
    print("-*CRIAR UMA LISTA-*")
    print("---------------------")
    lista = []
    i = 0
    while i < t:
        n = (input("Número: "))
        lista.append(n)  # append incrementa n na lista
        i += 1
    return lista


def imprimir(lista):
    '''função sem retorno
    --imprime lista na tela--
    percorre cada elemento da lista, exibindo-o e cada rodada'''
    print("-*IMPRIMINDO A LISTA-*")
    print("---------------------")
    for i in lista:  # a cada elemento da lista o i irá recebe-lo
        print(f"Elemento:{i}")

# PRINCIPAL
t = tamanho_da_lista()
lista = criar_lista(t)
imprimir(lista)

