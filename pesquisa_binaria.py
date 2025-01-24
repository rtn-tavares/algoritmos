def pesquisa_binaria(lista, item):
    baixo = 0 #Declaramos o menor limite da busca
    alto = len(lista) - 1 #Declaramos o mais valor da busca

    while baixo <= alto:  # Enquanto o limite inferior não ultrapassar o superior, continuamos a busca
        meio = (baixo + alto) // 2 # Aqui Calculamos o índice do meio da lista
        chute = lista[meio] # Obtemos o valor do elemento localizado no índice do meio
        if chute == item: # Verificamos se o elemento do meio é igual ao item procurado
            return meio # Retorna o índice do item encontrado
        if chute > item:
            alto = meio - 1
        else:
            baixo = meio + 1
    return None

minha_lista = [1, 3, 5, 7, 9]

# Testamos a função de pesquisa binária com diferentes valores
print(pesquisa_binaria(minha_lista, 3))  # Deve retornar 1 (índice do valor 3 na lista)
print(pesquisa_binaria(minha_lista, -1)) # Deve retornar None (valor não encontrado)
print(pesquisa_binaria(minha_lista, 4))  # Deve retornar None (valor não encontrado)
print(pesquisa_binaria(minha_lista, 9))  # Deve retornar 4 (índice do valor 9 na lista)
