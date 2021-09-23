# Obtenha, usando requests ou urllib, o conteúdo sobre 
# as PyLadies no link http://brasil.pyladies.com/about e:

# Conte todas as palavras no corpo da página, 
# e indique quais palavras apareceram apenas uma vez.

# Conte quantas vezes apareceu a palavra ladies no conteúdo da página

from bs4 import BeautifulSoup
import requests, lxml

html = requests.get("http://brasil.pyladies.com/about/").text

soup = BeautifulSoup(html, "lxml")

textos = []

paragrafos = soup.find_all(name="p")
for paragrafo in paragrafos:
    texto = paragrafo.getText()
    textos.append(texto)

contador = 0
lista_palavras = []
for texto in textos:
    palavras = texto.split()
    for i in range(len(palavras)):
        lista_palavras.append(palavras[i])
        if "ladies" in palavras[i]:
            contador += 1

palavras_unicas = []
for palavra in lista_palavras:
    if lista_palavras.count(palavra) == 1:
        palavras_unicas.append(palavra)


print(f"O texto possui {len(lista_palavras)} palavras.")
print()
print("As palavras que aparecem uma única vez são:")
print(palavras_unicas)
print()
print(f"A palavra 'ladies' aparece {contador} vezes.")