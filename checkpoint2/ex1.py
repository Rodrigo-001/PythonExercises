#Rodrigo Camargo 98373
#Pedro Marques 550252 

n = int(input("Quantos números deseja calcular? "))
numeros = []

for i in range(n):
    numeros.append(float(input("Digite o {}º número: ".format(i+1))))

operacoes = ["adição", "subtração", "multiplicação", "divisão"]
resultado = numeros[0]

for i in range(4):
    opcao = input("Deseja realizar {}? (s/n) ".format(operacoes[i]))
    if opcao == "s":
        for j in range(1, n):
            if i == 0:
                resultado += numeros[j]
            elif i == 1:
                resultado -= numeros[j]
            elif i == 2:
                resultado *= numeros[j]
            else:
                resultado /= numeros[j]
        print("Resultado da {}: {}".format(operacoes[i], resultado))

maior = max(numeros)
menor = min(numeros)
soma = sum(numeros)

print("Maior número digitado: ", maior)
print("Menor número digitado: ", menor)
print("Somatório acumulado: ", soma)


