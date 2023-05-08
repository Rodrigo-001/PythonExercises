#Rodrigo Camargo 98373
#Pedro Marques 550252 
tabuada = int(input("Escolha uma tabuada: "))
cont = tabuada
for i in range(1,11):
    cont *= i
    print(f'{tabuada} x {i} = {cont}')
    cont = tabuada
print('Fim')
    
    