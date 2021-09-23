# Escreva um programa em Python que leia um vetor de 5 números inteiros
# e o apresente na ordem inversa. 
# Imprima o vetor no final. Use listas.

lista = []

while len(lista) < 5:
    try:
        elemento = int(input("Informe o próximo elemento da lista: "))
        lista.append(elemento)
    except:
        print("Entrada inválida")

print("\nLista original:", lista)

lista.reverse()

print("\nLista invertida:", lista)