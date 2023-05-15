'''
feito por Rodrigo em 14-05
'''
# def entrada_de_dados():
def entrada_de_dados():
    x = int(input("Digite x: "))
    y = int(input("Digite y: "))
    return x,y
# def verificar_maior(x, y):
def verificar_maior(x,y):
    if x > y:
        return x
    else:
        return y
# def imprimir_mensagem(x, y, maior):
def imprimir_mensagem(x, y, maior):
    if maior==x:
        print(f"O número {x} é maior do que {y}")
    else:
        print(f"O número {y} é maior do que {x}")
# # programa_principal():
x, y = entrada_de_dados()
maior = verificar_maior(x,y)
imprimir_mensagem(x,y,maior)


