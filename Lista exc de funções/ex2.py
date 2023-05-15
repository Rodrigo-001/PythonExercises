def encontrar_maior_numero(lista):
    maior = lista[0]  # Assume que o primeiro número da lista é o maior
    
# a linha for numero in lista: está dizendo que, para cada numero presente na lista, o bloco de código dentro do loop será executado. O loop percorre todos os elementos da lista, um por um, atribuindo cada elemento à variável numero e executando o código dentro do loop para cada elemento.    
    for numero in lista:
        if numero > maior:           
            maior = numero            
    return maior

numeros = [10, 5, 8, 12, 3, 6]
resultado = encontrar_maior_numero(numeros)
print(f'\nMaior: {resultado}\n')  # Saída: 12