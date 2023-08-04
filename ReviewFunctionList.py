# O PROGRAMA CRIA E IMPRIME UMA LISTA COM OS NÚMEROS E TAMANHO INFORMADOS PELO USUÁRIO
# FEITO EM AULA 08-04
def tamanho_lista():
    print("--TAMANHO DA LISTA--")
    print("--------------------")
    t = int(input("Tamanho da lista: "))
    return t

def criar_lista(tamanho):
    print("--CRIAR UM LISTA--")
    print("--------------------")
    lista = []
    i=0
    while i<tamanho:
        n = int(input("Número: "))
        lista.append(n)
        i+=1
    return lista
def imprimir(lista):
    print("--IMPRIMIR A LISTA--")
    print("--------------------")
    for i in lista:
        # print(i, end=' ') #imprime na mesma linha com espaço entre os numeros
        print(f'Elemento: {i}')     #quebra linhas imprimindo os numeros embaixo dos outros

def principal():
    print("--PRINCIPAL--")
    print("--------------------")
    tamanho = tamanho_lista()
    lista = criar_lista(tamanho)
    imprimir(lista)

#PRINCIPAL
principal()