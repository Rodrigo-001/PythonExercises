# Pergunta idade e testa maior de idade
# feito por Rodrigo

print('Verifica IDADE')

idade = int(input('Digite sua idade: '))

if idade >= 18:
    #Bloco executado quando a condição for verdadeira
    print('maior de idade')
    print('Você pode ter uma CNH')    
else:
    #Bloco executado quando a condição for falsa
    print('Menor de idade')
    print('Você ainda não completou 18 anos')
    print('Portanto não se qualifica para adquirir CNH')
#executa sempre    
print('FIM DO PROGRAMA!')

