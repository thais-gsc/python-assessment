# Usando a biblioteca ‘pygame’, escreva um programa que desenha
# na tela em posição aleatória um quadrado amarelo
# de tamanho 50 (cinquenta), toda vez que a tecla espaço
# for pressionada ou o botão direito for clicado.

import pygame, random

pygame.init()

LARGURA_TELA, ALTURA_TELA = 800, 600
TELA = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))

AMARELO = (255, 255, 0)

terminou = False
while not terminou:
    pygame.display.update()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminou = True
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pygame.draw.rect(TELA, AMARELO, (random.randint(0, LARGURA_TELA-50), random.randint(0, ALTURA_TELA-50), 50,50))
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.rect(TELA, AMARELO, (random.randint(0, LARGURA_TELA-50), random.randint(0, ALTURA_TELA-50), 50,50))

pygame.display.quit()

pygame.quit()