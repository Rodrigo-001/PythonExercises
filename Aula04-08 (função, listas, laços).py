# O PROGRAMA:
# CRIA E IMPRIME UMA LISTA COM OS NÚMEROS E TAMANHO INFORMADOS PELO USUÁRIO
#SEPARA E IMPRIME NÚMEROS PARES
#OBTEM NUMERO E RETORNA OCORRÊNCIAS DELE

# FEITO EM AULA 04-08

def tamanho_lista():
    '''recebe entrada do teclado (int)
        retorna t (int)'''
    t = int(input("\nTamanho da lista: "))
    return t

def criar_lista(t):
    '''recebe parâmetro t (int
        retorna lista(list))'''
    print("\n--Criando Lista (Somente num inteiros)--")
    lista = []
    cont = 0    
    i=0
    cont = 1      
    while i < t:
        n = int(input(f"{cont}° Item: "))
        lista.append(n)
        i+=1
        cont+=1
    return lista

def imprimir(lista):
    '''recebe lista(list)
        imprime lista(list)'''
    # print(i, end=' ') #não quebra linha
    print("\n--Imprimindo Lista--") #quebra linha
    cont=1  #exibe numeração antes do item.
    ind=0   #
    for j in lista:
        print(f"\n{cont}° Item: {lista[ind]}")
        cont+=1
        ind+=1

def imprimir_pares(lista):
    '''recebe lista(list)
        imprime elementos pares da lista(print)'''
    print("\n--Imprimindo Pares--")
    pares = []
    for i in lista:
        if i%2==0:
            pares.append(i)
            # print(f"Elemento: {i}") #imprime par pulando linha
    print(f"Pares: ",pares) #imprime a lista de pares
    
def separar_pares(lista):
    '''recebe lista(list)
        retorna lista_pares(list)'''
    lista_pares = []
    for i in lista:
        if i%2==0:
            lista_pares.append(i)
    return lista_pares

def obter_num():
    '''recebe num(int) via teclado
        retorna num (nint)'''
    print("\n--Obtendo um número--")
    num = int(input("Digite um número:"))
    return num

def verificar_ocorrencias(num, lista):
    '''recebe num(int) e lista(list)
        retorna oc(int)'''
    print("\n--Verificando Ocorrências--")
    oc = 0
    for i in lista:
        if num==i:
            oc+=1
        i+1
    return oc

# função mãe
def principal():
    t = tamanho_lista()
    lista = criar_lista(t)
    imprimir(lista)    
    pares = separar_pares(lista)
    # ----------------
    print("--")
    imprimir(pares)
    print("==============")
    num = obter_num()
    qtd_ocorrencias = verificar_ocorrencias(num, lista)
    print(f"\nQuantidade de ocorrências: {qtd_ocorrencias}")
    

# PRINCIPAL
# principal()
help(verificar_ocorrencias)

