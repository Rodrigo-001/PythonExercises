# Programa pede para usuario digitar valor e quantidade do produto desejado, e aplica desconto com condicional
# Se total >= 100, então desconto de 10%
# Feito por Rodrigo

print('\nAsistente de compra\n')

valor = float(input('Digite o valor do produto: '))

quantidade = int(input('\nDigite a quantidade desejada: '))

total = quantidade * valor

if total >= 100:
    # exibe o total com desconto
    total = total * 0.9
    
elif total >= 200:
    total = total * 0.20

elif total >= 300:
    total = total * 0.30
    
elif total > 400:
    total = total * 0.40
    
else:
    print(f'\nTotal da compra: {total: .2f}')

print(f'\nTotal da sua compra: {total: .2f}')



