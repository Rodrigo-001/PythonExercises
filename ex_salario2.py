'''
Recebe 4 salarios, calcule a média salarial e imprime os salarios menores
que a média

Feito por Rodrigo em 28-04

usado: variaveis, condicional if, listas, while, len
'''


#jeito arcaico
'''
soma = 0
salario_0 = float(input('Salario: '))
soma += salario_0
salario_1 = float(input('Salario: '))
soma += salario_1
salario_2 = float(input('Salario: '))
soma += salario_1
salario_3 = float(input('Salario: '))
soma += salario_3

media = soma/4

if salario_0 < media:
    print(f'Abaixo da média: R$ {salario_0:.2f}')
if salario_1 < media:
    print(f'Abaixo da média: R$ {salario_1:.2f}')
if salario_2 < media:
    print(f'Abaixo da média: R$ {salario_2:.2f}')
if salario_3 < media:
    print(f'Abaixo da média: R$ {salario_3:.2f}')
'''

#melhorou com listas
salarios = [0,0,0,0]
soma = 0
salarios[0] = float(input('Salario: '))
soma+=salarios[0]
salarios[1] = float(input('Salario: '))
soma+=salarios[1]
salarios[2] = float(input('Salario: '))
soma+=salarios[2]
salarios[3] = float(input('Salario: '))
soma+=salarios[3]
media = soma/4
print(f'Media: R${media:.2f}')
if salarios[0] < media:
    print(f'Abaixo da media: R${salarios[0]:.2f}')
if salarios[1] < media:
    print(f'Abaixo da media: R${salarios[1]:.2f}')
if salarios[2] < media:
    print(f'Abaixo da media: R${salarios[2]:.2f}')
if salarios[3] < media:
    print(f'Abaixo da media: R${salarios[3]:.2f}')


# melhorando com listas e laços

salarios = [0,0,0,0]
soma = 0
i=0
  # enquanto i for menor que o tamanho da lista
while i<len(salarios):
    salarios[i] = float(input('Salario: '))
    soma+=salarios[i]
    i+=1
media = soma / len(salarios)
i=0
while i<len(salarios):
    if salarios[i]<media:
        print(f'Abaixo da media: R${salarios[i]:.2f}')
        