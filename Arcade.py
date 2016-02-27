# Pygame Arcade
# ICS4U-02
# 2016
# A collection of games built using pygame by the ICS4U-02 class, all running in a virtual arcade.

# TODO: fix background, allow user to adjust window size on init, collision detect

import pygame, sys, os
from pygame.locals import *

class arcade:
    global previous_areas ; previous_areas = []
    
    def __init__(self):
        flags = HWSURFACE | DOUBLEBUF #| NOFRAME
        screen_x, screen_y = 600, 600
        self.screen = pygame.display.set_mode((screen_x,screen_y),flags)
        pygame.display.set_icon(pygame.image.load(os.getcwd() + '\\resources\window_icon.png').convert_alpha())

    def UI(self):
        arcade.setCaption(__file__)
        pass
    
    #Framework
    def getEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.event.pump()

    def getKey(self):
        return pygame.key.get_pressed()

    def getMousePos(self):
        return pygame.mouse.get_pos()

    def getMouseButton(self):
        return pygame.mouse.get_pressed()

    def getImage(self, file):
        return pygame.image.load(os.getcwd() + '\\resources\\'.join(file)) #Fix later; should fetch from __name__ folder

    def getSound(self, file):
        return pygame.mixer.Sound(os.getcwd() + '\\resources\\'.join(file)) #Fix later; should fetch from __name__ folder
    
    def isColliding(obj1,obj2):
        return pygame.Surface.get_rect(obj1).colliderect(pygame.Surface.get_rect(obj2))

    def drawBackground(self, background):
        self.screen.blit(background, (0, 0))

    def initBackground(self, background):
        self.screen.blit(background, (0, 0))
        pygame.display.update()

    def draw(self, *args): #arg is (object, x, y)
        global previous_areas
        update_areas = []
        for arg in args:
            self.screen.blit(arg[0],(arg[1],arg[2]))
            area = pygame.Surface.get_bounding_rect(arg[0])
            area[0], area[1] = arg[1], arg[2]
            update_areas.append(area)
            
        pygame.display.update(update_areas) #only update areas that requires it
        pygame.display.update(previous_areas)
        previous_areas = update_areas[:]

    def makeSurface(self, width, height, alpha = 0):
        if alpha:
            return pygame.Surface((width,height), pygame.SRCALPHA, 32).convert_alpha()
        return pygame.Surface((width,height))
    
    def setCaption(self, file):
        pygame.display.set_caption(os.path.basename(file).split('.')[0])
    
    def returnToArcade(self):
        arcade().UI()


if __name__ == '__main__':
    #If arcade.py is executed, open game selector UI
    #All games are executable as a standalone game.
    #All games are contained in a single .py file + resources (sprites, fonts, etc.)
    pygame.init()
    pygame.mixer.init(22050,-16,2,1024)
    arcade = arcade()
    last = pygame.time.get_ticks()
    cooldown = 30   

    while True:
        now = pygame.time.get_ticks()
        if now - last >= cooldown:
            last = now
            arcade.UI()
            arcade.getEvents()


