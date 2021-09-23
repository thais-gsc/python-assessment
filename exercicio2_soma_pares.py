# Usando o Thonny, escreva um programa em Python que some todos os 
# números pares de 1 até um dado n, inclusive. 
# O dado n deve ser obtido do usuário. 
# No final, escreva o valor do resultado desta soma.

n = int(input("Informe o último número.\n"))

soma = 0

for i in range(n+1):
    if i %2 == 0:
        soma += i

print(f"A soma dos pares de 1 a {n} é igual a {soma}.")