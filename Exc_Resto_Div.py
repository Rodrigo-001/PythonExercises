# Este programa recebe dois valores do usuário e calcula a divisão entre eles, se a operação matematica retornar um resto então exibe que não é uma divisão exata.
# feito em 30-03 por rodrigo

n1 = float(input("\nDigite o primeiro numero: "))
n2 = float(input("Digite o segundo: "))
resto = n1 % n2

if resto == 0:
    print("\n\nA divisão entre " + str(n1) + " e " + str(n2) + " é exata\n\n")
else:
    print("\n\nA divisão entre " + str(n1) + " não é " + str(n2) + " é exata\n\n")

