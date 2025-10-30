import pygame

# initialize pygame and the mixer
pygame.init()
pygame.mixer.init()

# load and play the music
pygame.mixer.music.load(r'C:\Users\thiago.agjunior\Downloads\Python\Kenny-G.mp3')
pygame.mixer.music.play()

# wait until the music finishes playing
while pygame.mixer.music.get_busy():
    pass
