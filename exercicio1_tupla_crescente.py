# Usando o Thonny, escreva um programa em Python que leia uma tupla
# contendo 3 números inteiros, (n1, n2, n3) e os imprima em ordem crescente.

tupla = ()

n1 = int(input("Informe o primeiro número.\n"))
n2 = int(input("Informe o próximo número.\n"))
n3 = int(input("Informe o próximo número.\n"))

tupla += (n1,)
tupla += (n2,)
tupla += (n3,)

print("Tupla original:", tupla)

tupla = sorted(tupla)

for numeros in tupla:
    print(numeros)
