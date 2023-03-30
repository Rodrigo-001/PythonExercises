# Este programa le 3 notas, calcula média e imprime as notas ordenadas de forma crescente e a média obtida.
# Feito em: 24-03 por Rodrigo

# Usando função sort
# print('-----------------')
# print('OBTENHA SUA NOTA')
# print('-----------------')
# print('\nInsira suas notas: \n')
# n1 = float(input('Nota 1: '))
# n2 = float(input('Nota 2: '))
# n3 = float(input('Nota 3: '))
# media = float(n1 + n2 + n3) / 3
# notas = [n1, n2, n3]
# notas.sort()
# print('\nSuas notas: ', notas)
# print(f'\nMédia: {media: .1f}')

# Usando if else
print('-----------------')
print('OBTENHA SUA NOTA')
print('-----------------')
print('\nInsira suas notas: \n')
n1 = float(input('Nota 1: '))
n2 = float(input('Nota 2: '))
n3 = float(input('Nota 3: '))
media = float(n1 + n2 + n3) / 3
# condicional
if n1 < n2 and n1 < n3 and n2 < n3:##
    print("Suas notas: ", n1, n2, n3)## 
elif n2 < n1 and n2 <n3 and n1 < n3:##
    print("Suas notas: ", n2, n1, n3)##
elif n1 < n3 and n1 < n2 and n3 < n2:##
    print("Suas notas: ", n1, n3, n2 )##
elif n3 < n1 and n3 < n2 and n1 < n2:
    print("Suas notas: ", n3, n1, n2)##
elif n2 < n1 and n2 < n3 and n3 < n1:##
    print("Suas notas: ", n2, n3, n1) #--------
else:
    print("Suas notas: ", n3, n2, n1)
