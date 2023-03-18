valor = float(input('\nDigite o valor do produto: '))
quantidade = float(input('\nDigite a quantidade: '))
total = valor * quantidade


if total < 100:
    print('\nTotal da sua compra: ',total)
    print('\nNão houve desconto\n')

elif total <= 199:
    total -= (total * 0.10)
    print('\nTotal da sua compra: ',total)
    print('\nO desconto foi de 10%\n')

elif total <= 299:
    total -= (total * 0.20)
    print('\nTotal da sua compra: ',total)
    print('\nO desconto foi de 20%\n')

elif total <= 400:
    total -= (total * 0.30)
    print('\nTotal da sua compra: ',total)
    print('\nO desconto foi de 30%\n')
     

elif total > 400:
    total -= (total * 0.40)
    print('\nTotal da sua compra: ',total)
    print('\nO desconto foi de 40%')
