# Este programa recebe calcula o salário do vendedor levando em conta sua comissão
# Por Rodrigo
print("--------------------------")
print("Calculo Comissão de Vendas")
print("--------------------------")
nome = input("Digite seu nome, por favor: ")
salFixo = float(input("Digite seu salário fixo: "))
totalVendas = float(input("Digite suas vendas desse mês: "))
salarioLiquido = salFixo + (totalVendas * 0.15)

print(nome + f" Seu salario mensal é: {salarioLiquido:.2f}")