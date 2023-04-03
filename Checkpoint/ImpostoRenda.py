# Este programa recebe o salario do funcionario e calcula seu imposto de renda
#Feito por Rodrigo

print("----------------")
print("IMPOSTO DE RENDA")
print("----------------")
nome = input("\nDigite seu nome: ")
salario = float(input("Digite seu salário: "))

if salario < 1257.12:
    print("Você está isento!")

elif salario >= 1257.12 and salario <= 2510.00:
    aliquota = salario * 0.17
    print("Valor a pagar: " + str(aliquota))
    print("Sua aliquota é de: 17%")
elif salario > 2510.00:
    aliquota = salario * 0.28
    print("Valor a pagar: " + str(aliquota))
    print("Sua aliquota é: 28%")