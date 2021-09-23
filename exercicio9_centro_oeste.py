# Obtenha, usando requests ou urllib, 
# a página HTML https://fgopassos.github.io/pagina_exemplo/estadosCentroOeste.html 
# dentro de seu programa em Python e faça:

# Imprima o conteúdo referente apenas à tabela
# apresentada na página indicada.

from bs4 import BeautifulSoup

html = open('pagina_exemplo/estadosCentroOeste.html', encoding="utf8").read()

soup = BeautifulSoup(html, "lxml")

tabela = soup.find(class_="tabela")

conteudo = tabela.getText()

print(conteudo)

#Escreva um programa que obtenha do usuário uma sigla do
# estado da região Centro-Oeste e apresenta suas informações
# correspondentes na tabela. O resultado deve apresentar apenas
# o conteúdo, sem formatação. Ou seja, as tags não devem aparecer.
# Não esqueça de checar se a sigla pertence à região.

centro_oeste = {}

linhas = tabela.find_all(class_="linha")

for linha in linhas:
    celulas = linha.find_all(class_="celula")
    for celula in celulas[0:1]:
        for nome in celulas[1:2]:
            for capital in celulas[2:3]:
                for pop in celulas[3:4]:
                    for area in celulas[4:5]:
                        centro_oeste[celula.text] = nome.text, capital.text, pop.text, area.text

# for estados in centro_oeste:
#     print(estados, centro_oeste[estados])

sigla = input("Informe a sigla do estado do Centro-Oeste que deseja buscar.\n")

while sigla not in centro_oeste:
    print("Você não parece saber geografia. Por favor, informe uma sigla de um estado do Centro-Oeste.\n")
    
    sigla = input("Informe a sigla do estado do Centro-Oeste que deseja buscar.\n")

print(centro_oeste[sigla])