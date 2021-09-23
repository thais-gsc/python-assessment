#Obtenha, usando requests ou urllib, dentro de seu programa em Python, 
# o csv do link: 
# https://sites.google.com/site/dr2fundamentospython/arquivos/Winter_Olympics_Medals.csv
# E:

# Dentre os seguintes países nórdicos: Suécia, Dinamarca e Noruega,
# verifique: No século XXI (a partir de 2001), qual foi o maior
# medalhista de ouro, considerando apenas as seguintes modalidades:
# Curling
# Patinação no gelo (skating)
# Esqui (skiing)
# Hóquei sobre o gelo (ice hockey)

# Para cada esporte, considere todas as modalidades, 
# tanto no masculino quanto no feminino. 
# Sua resposta deve imprimir um relatório mostrando o total de medalhas
# de cada um dos países e em que esporte, ano, cidade
# e gênero (masculino ou feminino) cada medalha foi obtida.

import requests

url = "https://sites.google.com/site/dr2fundamentospython/arquivos/Winter_Olympics_Medals.csv"

csv = requests.get(url).text

linhas = csv.splitlines()

contador_suecia = 0
contador_dinamarca = 0
contador_noruega = 0

medalhas_suecia = []
medalhas_dinamarca = []
medalhas_noruega = []

for linha in linhas[1:]:
    colunas = linha.split(',')
    ano = int(colunas[0])
    cidade = colunas[1]
    esporte = colunas[2]
    pais = colunas[4]
    genero = colunas[6]
    medalha = colunas[7]
    if ano > 2001:
        if esporte == "Curling" or esporte == "Skating" or esporte == "Skiing" or esporte == "Ice Hockey":
            if medalha == "Gold":
                if genero == 'M':
                    genero = "Masculino"
                elif genero == 'W':
                    genero = "Feminino"
                if pais == "SWE":
                    contador_suecia += 1
                    medalhas_suecia.append("Esporte: " + esporte +  "   Ano: " + str(ano) + "   Cidade: " + cidade + "  Gênero: " + genero)
                elif pais == "DEN":
                    contador_dinamarca += 1
                    medalhas_dinamarca.append("Esporte: " + esporte + " Ano: " + str(ano) + "   Cidade: " + cidade + "  Gênero: " + genero)
                elif pais == "NOR":
                    contador_noruega += 1
                    medalhas_noruega.append("Esporte: " + esporte + "   Ano: " + str(ano) + "   Cidade: " + cidade + "  Gênero: " + genero)

if contador_suecia >= contador_noruega and contador_suecia >= contador_dinamarca:
    print(f"Suécia é o maior medalhista, com {contador_suecia} medalhas de ouro.")
elif contador_dinamarca >= contador_suecia and contador_dinamarca >= contador_noruega:
    print(f"Dinamarca é o maior medalhista, com {contador_dinamarca} medalhas de ouro.")
else:
    print(f"Noruega é o maior medalhista, com {contador_noruega} medalhas de ouro.")

print()

print("-- Relatório de medalhas --")
print("Suécia:")
if not medalhas_suecia:
    print("Não tem uma medalhinha sequer...")
else:
    for resultado in medalhas_suecia:
        print(resultado)
print()
print("Dinamarca:")
if not medalhas_dinamarca:
    print("Não tem uma medalhinha sequer...")
else:
    for resultado in medalhas_dinamarca:
        print(resultado)
print()
print("Noruega:")
if not medalhas_noruega:
    print("Não tem uma medalhinha sequer...")
else:
    for resultado in medalhas_noruega:
        print(resultado)