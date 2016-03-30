import pygame, os, sys
from pygame.locals import *
from Arcade import arcade
from colours import *

class Jumper(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((60,60))
        self.image.fill(pink)
        self.rect = self.image.get_rect()
        

def Game(arcade):
    arcade.setCaption(__file__)
    arcade.setWindow(600, 600)
    font1 = pygame.font.SysFont('Arial',24, True)

    player = Jumper()
    

    while True:
        arcade.getEvents()
        pressed = arcade.getKey()
        if pressed[K_SPACE]:

        arcade.draw((player.image, player.rect.x, player.rect.y))
        arcade.update()
    
    

if __name__ == '__main__':
    pygame.init()
    pygame.mixer.init(22050,-16,2,1024)
    Game(arcade())
