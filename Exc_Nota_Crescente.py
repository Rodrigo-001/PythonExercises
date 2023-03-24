# Este programa le 3 notas, calcula média e imprime as notas ordenadas de forma crescente e a média obtida.
# Feito em: 24-03

# ---------------------
print('------------------')
print('OBTENHA SUA NOTA')
print('-----------------')
print('\nInsira suas notas: \n')
n1 = float(input('Nota 1: '))
n2 = float(input('Nota 2: '))
n3 = float(input('Nota 3: '))
media = float(n1 + n2 + n3) / 3
notas = [n1, n2, n3]
notas.sort()
print('\nSuas notas: ', notas)
print(f'\nMédia: {media: .1f}')

