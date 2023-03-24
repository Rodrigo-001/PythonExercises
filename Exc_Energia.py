# recebe consumo kwh, se consumo for < que 150, valor por kwh é 0,20, se for >= 150, então valor é 0,20 por kwh, se maior que 500, então 0.30 por kwh.
# O valor mínimo para total é 11.


print('----------------')
print('CONTA DE ENERGIA')
print('----------------')
print('\nDigite seu consumo em kilowatts\n')
consumo = float(input())

if consumo <150:
    valorkwh = 0.20
elif consumo >= 150 and consumo <= 500:
    valorkwh = 0.25
else:
    valorkwh = 0.30
total = consumo * valorkwh

if total <= 11.90:
    print('Total a pagar: R$ 11,90')
else:
    print(f'\nTotal a pagar: {total: .2f} \n')
