def buscaMenor(arr):
    menor = arr[0] #Armazena o menor valor do array
    menor_indice = 0 #Armazena o índice do menor valor
    for i in range(1, len(arr)):
        if arr[i] < menor:
            menor = arr[i]
            menor_indice = i
    return menor_indice

def ordenacaoPorSelecao(arr): #Ordenações em um array
    novoArr = []
    for i in range(len(arr)):
        menor = buscaMenor(arr) #Encontra o menor valor do array e adiciona ao novo array
        novoArr.append(arr.pop(menor))
    return novoArr

print (ordenacaoPorSelecao([5, 3, 6, 2, 10]))
print (ordenacaoPorSelecao([99, 58, 1, 0, 4, 19, 33, 2]))
