# Este programa recebe calcula o salário do vendedor levando em conta sua comissão
# Por Rodrigo

nome = input("Digite seu nome, por favor: ")
salFixo = float(input("Digite seu salário fixo: "))
totalVendas = float(input("Digite suas vendas desse mês: "))
salarioLiquido = salFixo + (totalVendas * 0.15)

print(nome + "Seu salario é: " + str(salarioLiquido))