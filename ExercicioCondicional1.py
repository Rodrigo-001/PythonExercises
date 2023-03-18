valor = float(input('Digite o valor do produto: '))
quantidade = float(input('Digite a quantidade: '))
total = valor * quantidade


if total < 100:
    print('Total da sua compra: ',total)
    print('Não houve desconto')

elif total <= 199:
    total -= (total * 0.10)
    print('Total da sua compra: ',total)
    print('O desconto foi de 10%')

elif total <= 299:
    total -= (total * 0.20)
    print('Total da sua compra: ',total)
    print('O desconto foi de 20%')

elif total <= 400:
    total -= (total * 0.30)
    print('Total da sua compra: ',total)
     

elif total > 400:
    total -= (total * 0.40)
    print('Total da sua compra: ',total)
    print('O desconto foi de 40%')
