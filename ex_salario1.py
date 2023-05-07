'''
Feito por Rodrigo em 28-04

usado: in, range, append, len

Recebe 4 salarios, calcula a média salarial e retorna os salarios que estão abaixo da média
'''
salarios = []
soma = 0

for i in range(4):
    salario = float(input('salario: '))
    soma+=salario
    # metodo append aloca espaço na memoria e adiciona na lista(semelhante a uma fila)
    salarios.append(salario)
media = soma/len(salarios)

for salario in salarios:
    if salario < media:
        print(f'Abaixo da média: R${salario:.2f}')


