#Escreva uma função em Python que leia uma tupla contendo números inteiros,
# retorne uma lista contendo somente os números ímpares
# e uma nova tupla contendo somente os elementos nas posições pares.

tupla = (8, 43, 62, 11, 97, 23, 0, 55, 31)

def separar_par_impar(tupla):
    lista_impares = []
    tupla_posicoes_pares = ()
    for i in tupla:
        if i%2 != 0:
            lista_impares.append(i)
    for i in range(len(tupla)):
        if i%2 == 0:
            tupla_posicoes_pares += (tupla[i],)
    print(lista_impares)
    print()
    print(tupla_posicoes_pares)

separar_par_impar(tupla)