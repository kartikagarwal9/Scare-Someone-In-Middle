import pygame
from time import sleep
pygame.init()
window = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
pygame.mixer.init()
pygame.mixer.music.load('voice.mp3') #voice.mp3 is the melody tune
pygame.mixer.music.play()
sleep(5)
pygame.mixer.music.load('ScaryTune.mp3')  #ScaryTune.mp3 can be replaced with your scary tune
pygame.mixer.music.play()
sleep(1)
image = pygame.image.load('scr.jpg')  #scr.jpg is the scary photo which comes in between , you can replace with anything.
window.blit(image, (0,0))
pygame.display.update()
sleep(3)
