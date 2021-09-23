# Obtenha, usando requests ou urllib, dentro de seu 
# programa em Python, o csv do link:
# https://sites.google.com/site/dr2fundamentospython/arquivos/Video_Games_Sales_as_at_22_Dec_2016.csv
#Obtenha, dentre os jogos do gênero de ação (Action), 
# tiro (Shooter) e plataforma (Platform):

# Quais são as três marcas que mais publicaram jogos dos
# três gêneros combinados? Indique também o total de jogos de cada marca.

# Quais são as três marcas que mais venderam os três
# gêneros combinados? Indique também o total de vendas de cada marca.

# Qual é a marca com mais publicações em cada um desses gêneros
# nos últimos dez anos? Indique também o número total de jogos dela.

# Qual foi a marca que mais vendeu em cada um desses gêneros
# nos últimos dez anos, no Japão? Indique também o total de vendas dela.

import requests

url = "https://sites.google.com/site/dr2fundamentospython/arquivos/Video_Games_Sales_as_at_22_Dec_2016.csv"

csv = requests.get(url).text

linhas = csv.splitlines()

dic_distribuidora = {}
dic_vendas = {}

dic_acao = {}
dic_tiro = {}
dic_plataforma = {}

dic_jp_acao = {}
dic_jp_acao_vendas = {}

dic_jp_tiro = {}
dic_jp_tiro_vendas = {}

dic_jp_plataforma = {}
dic_jp_plataforma_vendas = {}

for linha in linhas[1:]:
    colunas = linha.split(',')
    
    nome = colunas[0]
    plataforma = colunas[1]
    ano = colunas[2]
    genero = colunas[3]
    distribuidora = colunas[4]
    vendas_jp = colunas[7]
    vendas_global = colunas[9]
    
    if genero == "Action" or genero == "Shooter" or genero == "Platform":
        if distribuidora not in dic_distribuidora:
            dic_distribuidora[distribuidora] = 0
            dic_vendas[distribuidora] = 0
        else:
            dic_distribuidora[distribuidora] += 1
            dic_vendas[distribuidora] += float(vendas_global)
            if ano != "N/A" and int(ano) >= 2011:
                if genero == "Action":
                    if distribuidora not in dic_acao or distribuidora not in dic_jp_acao:
                        dic_acao[distribuidora] = 0
                        dic_jp_acao[distribuidora] = 0
                        dic_jp_acao_vendas[distribuidora] = 0
                    else:
                        dic_acao[distribuidora] += 1
                        dic_jp_acao[distribuidora] += 1
                        dic_jp_acao_vendas[distribuidora] += float(vendas_jp)
                        
                elif genero == "Shooter":
                    if distribuidora not in dic_tiro or distribuidora not in dic_jp_tiro:
                        dic_tiro[distribuidora] = 0
                        dic_jp_tiro[distribuidora] = 0
                        dic_jp_tiro_vendas[distribuidora] = 0
                    else:
                        dic_tiro[distribuidora] += 1
                        dic_jp_tiro[distribuidora] += 1
                        dic_jp_tiro_vendas[distribuidora] += float(vendas_jp)
                        
                elif genero == "Platform":
                    if distribuidora not in dic_plataforma or distribuidora not in dic_jp_plataforma:
                        dic_plataforma[distribuidora] = 0
                        dic_jp_plataforma[distribuidora] = 0
                        dic_jp_plataforma_vendas[distribuidora] = 0
                    else:
                        dic_plataforma[distribuidora] += 1
                        dic_jp_plataforma[distribuidora] += 1
                        dic_jp_plataforma_vendas[distribuidora] += float(vendas_jp)

numero_jogos = sorted(dic_distribuidora.items(), key=lambda x: x[1], reverse=True)

numero_vendas = sorted(dic_vendas.items(), key=lambda x: x[1], reverse=True)

jogos_acao = sorted(dic_acao.items(), key=lambda x: x[1], reverse=True)

jogos_tiro = sorted(dic_tiro.items(), key=lambda x: x[1], reverse=True)

jogos_plataforma = sorted(dic_plataforma.items(), key=lambda x: x[1], reverse=True)

vendas_acao_jp = sorted(dic_jp_acao_vendas.items(), key=lambda x: x[1], reverse=True)

vendas_tiro_jp = sorted(dic_jp_tiro_vendas.items(), key=lambda x: x[1], reverse=True)

vendas_plataforma_jp = sorted(dic_jp_plataforma_vendas.items(), key=lambda x: x[1], reverse=True)

print("Marcas que mais publicaram jogos:")
for resultado in numero_jogos[:3]:
    distribuidora = resultado[0]
    jogos = resultado[1]
    print(f"{distribuidora:16}:{jogos} jogos")

print()

print("Marcas com maior total de vendas:")
for resultado in numero_vendas[:3]:
    distribuidora = resultado[0]
    vendas = round(resultado[1],2)
    print(f"{distribuidora:16}:{vendas} milhões de vendas")

print()

print("Marca que mais publicou jogos de ação, nos últimos 10 anos:")
for resultado in jogos_acao[:1]:
    distribuidora = resultado[0]
    jogos = resultado[1]
    print(f"{distribuidora}:{jogos} jogos")

print()

print("Marca que mais publicou jogos de tiro, nos últimos 10 anos:")
for resultado in jogos_tiro[:1]:
    distribuidora = resultado[0]
    jogos = resultado[1]
    print(f"{distribuidora}:{jogos} jogos")

print()

print("Marca que mais publicou jogos de plataforma, nos últimos 10 anos:")
for resultado in jogos_plataforma[:1]:
    distribuidora = resultado[0]
    jogos = resultado[1]
    print(f"{distribuidora}:{jogos} jogos")

print()

print("Marca que mais vendeu jogos de ação no Japão, nos últimos 10 anos:")
for resultado in vendas_acao_jp[:1]:
    distribuidora = resultado[0]
    vendas = round(resultado[1],2)
    print(f"{distribuidora}:{vendas} milhões de vendas")

print()

print("Marca que mais vendeu jogos de tiro no Japão, nos últimos 10 anos:")
for resultado in vendas_tiro_jp[:1]:
    distribuidora = resultado[0]
    vendas = round(resultado[1],2)
    print(f"{distribuidora}:{vendas} milhões de vendas")

print()

print("Marca que mais vendeu jogos de plataforma no Japão, nos últimos 10 anos:")
for resultado in vendas_plataforma_jp[:1]:
    distribuidora = resultado[0]
    vendas = round(resultado[1],2)
    print(f"{distribuidora}:{vendas} milhões de vendas")