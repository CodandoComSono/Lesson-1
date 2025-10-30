import pygame
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load(r'C:\Users\thiago.agjunior\Downloads\Python\Kenny-G.mp3')
pygame.mixer.music.play()
while pygame.mixer.music.get_busy():
    pass
