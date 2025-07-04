#TOCANDO MUSICAS EM PYTHON
import pygame

pygame.init() #INICIAR 
pygame.mixer.music.load('kelly6.mp3')  #ESCOLHA A MUSICA 
pygame.mixer.music.play() #INICIA A MUSICA
input('Pressione ENTER para parar a música...')
pygame.mixer.music.stop() #PARA A MUSICA










































