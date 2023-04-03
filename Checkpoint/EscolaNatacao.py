# Este programa recebe idade do candidato a aula de natação e devolve sua categoria de acordo com a iade
# Feito por Rodrigo

print("--------------------")
print("ESCOLINHA DE NATAÇÃO")
print("--------------------")

idade = int(input("\nDigite sua idade: "))

if idade >= 5 and idade <= 7:
    print("\nsua categoria é: Infantil A")
elif idade >= 8 and idade <= 10:
    print("\nsua categoria é: Infantil B")
elif idade >= 11 and idade <= 13:
    print("\nsua categoria é: Juvenil A")
elif idade >= 14 and idade <= 17:
    print("\nsua categoria é: Juvenil B")
elif idade >= 18:
    print("\nsua categoria é: Senior")
else:
    print("\nVocê não possui idade suficiente!")
