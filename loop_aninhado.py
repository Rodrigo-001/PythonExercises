# Este programa realiza um loop dentro de outro loop.
# Enquanto i for < 3 o segundo loop vai executar enquanto j for < 3. 
# Criado por Rodrigo em 17-04

i = 0 
while i < 3:
    i +=1
    print('i:', i)
    j = 0
    while j < 3:
        print(f'{i,j}')
        j+=1
print('i:', i)
print('j:', j)