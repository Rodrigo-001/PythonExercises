# Este programa recebe o salario do funcionario e calcula seu imposto de renda
#Feito por Rodrigo

print("----------------")
print("IMPOSTO DE RENDA 2023")
print("----------------")
nome = input("\nDigite seu nome: ")
salario = float(input("Digite seu salário: "))


if salario >= 1903.99 and salario <= 2826.65:
    aliquota = salario * (7.5 / 100) #continuar    
    print("\n" + nome + " Sua aliquota é de: 7,5%\n\n")
    print(f"\n\nValor a pagar: {aliquota:.2f}")

elif salario >= 2826.66 and salario <= 3751.05:
    aliquota = salario * (15.5 / 100)
    print("\n" + nome + "Sua aliquota é: 15%")
    print(f"\n\nValor a pagar: {aliquota:.2f}")

elif salario >= 3751.06 and salario <= 4664.68:
    aliquota = salario * (22.5 / 100)
    print("\n" + nome + "Sua aliquota é: 22,5%")
    print(f"\n\nValor a pagar: {aliquota:.2f}")

elif salario > 4664.68:
    aliquota = salario * (27.5 / 100)
    print("\n" + nome + "Sua aliquota é: 27,5%") 
    print(f"\n\nValor a pagar: {aliquota:.2f}")
   
else:
    print("\n\nVocê está isento! \n")

