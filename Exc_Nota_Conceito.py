# Pede 3 notas para o aluno calcula sua média e retorna conceito com condicional
#Else if e match case
print('\nOBTENHA SUA MÉDIA AQUI\n')
nota1 = float(input('Digite primeira nota: '))
nota2 = float(input('Digite segunda nota: '))
nota3 = float(input('Digite terceira nota: '))
media = (nota1 + nota2 + nota3) /3

if media >= 9:
    conceito = 'A'       
elif media >=8:
    conceito = 'B'    
elif media >= 7:
    conceito = 'C'     
elif media >= 6:
    conceito = 'D'    
else:
    conceito = 'E'
       
match conceito:
    case 'A':
        print(f'\nSua média é: {media: .1f}')
        print('\nSeu conceito foi A\n')
    case 'B':
        print(f'\nSua média é: {media: .1f}')
        print('\nSeu conceito foi B\n')
    case 'C':
        print(f'\nSua média é: {media: .1f}')
        print('\nSeu conceito foi C\n')
    case 'D':
        print(f'\nSua média é: {media: .1f}')
        print('\nSeu conceito foi D\n')
    case _:
        print(f'\nSua média é: {media: .1f}')
        print('\nSeu conceito foi E\n')

        