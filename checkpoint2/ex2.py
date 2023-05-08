'''
Feito por Rodrigo Camargo e Pedro Marques em 05-05-23

Este programa recebe usuario e senha, verifica se ambos conferem com o cadastrado e permite redenir as credenciais caso erre 3 vezes
'''
print("--CADASTRO--\n")
usuario = input("Crie seu usuário: ")
senha = int(input("Crie senha numerica: "))
print("\n--LOGIN--\n")
# USANDO LAÇO WHILE
'''
tentativas = 3
while tentativas >0:    
    valida_usuario = input("Digite usuário: ")
    valida_senha = int(input("Digite senha numerica: "))
    if valida_usuario==usuario and valida_senha==senha:
        print("\nlogin efetuado com sucesso!!\n")
        break
    else:
        print("\n--Login ou senha inválidos--\n")
        tentativas -=1
    if tentativas==0:
        usuario = input("Crie novo usuário: ")
        senha = int(input("Crie nova senha: "))
        tentativas = 3
'''
# USANDO WHILE E FOR
while True:
    for i in range(4):
        valida_usuario = input("Digite seu usuario: ")
        valida_senha = int(input("Digite sua senha: "))
        if valida_usuario==usuario and valida_senha==senha:
            print("\nLogin efetuado com sucesso!\n")
            break
        else:
            print("\nLogin e/ou senha incorretos\n")
    else:
        usuario = input("Crie *novo* usuário: ")
        senha = int(input("Crie *nova* senha: "))
        continue # recomeça o loop while externo
    break # Se o login for bem-sucedido, sai do loop while externo


