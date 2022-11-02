import pygame
from pygame.locals import *
from sys import exit #import de saída


pygame.init()

largura = 640
altura = 480


tela = pygame.display.set_mode((largura,altura)) #define o tamanho da janela
pygame.display.set_caption("jogo")  #para colocar o nome na janela

while True: #para o jogo ficar  rodando
    for event in pygame.event.get(): #evento, ações do usuário
        if event.type==QUIT:   #condição para sair do game
            pygame.quit()
            exit()
    pygame.draw.rect(tela,(255,0,0), (200,300,40,50)) # tela(onde desenhar), RGB, posições: x,y,largura,altura
    pygame.draw.circle(tela,(0,100,0),(300,260),40) #tela(onde desenhar), RGB, posições, raio do círculo
    pygame.draw.line(tela, (255,255,100), (390,0), (390,600),5)#tela (onde desenhar), RGB, primeiro ponto, segundo ponto, espessura da linha

    pygame.display.update() #para atualizar a tela enquanto o jogo roda
