# Pede um numero para o usuário, e sugere o numero com condicional

var = int(input('Digite um numero: '))
match var:
    case 1|2|3|4:
        print('Seu numero é 1 ou 2 ou 3 ou 4')
    case 5|6|7|8:
        print('Seu numero é 5 ou 6 ou 7 ou 8')
    case 9|10|11|12:
         print('Seu numero é 9 ou 10 ou 11 ou 12')
    case _:
        print('Nenhuma opção')
    