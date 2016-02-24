# Pygame Arcade
# ICS4U-02
# 2016
# A collection of games built using pygame by the ICS4U-02 class, all running in a virtual arcade.

import pygame, sys, os
from pygame.locals import *

class arcade:

    def __init__(self):
        flags = HWSURFACE | DOUBLEBUF #| NOFRAME
        screen_x, screen_y = 600, 600
        self.screen = pygame.display.set_mode((screen_x,screen_y),flags)
        pygame.display.set_icon(pygame.image.load(os.getcwd() + '\\resources\window_icon.png').convert_alpha())
        print('init ran')
        
    def InputEvents():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        pygame.event.pump()

    def UI():
        pass

    #Framework
    def GetEvent(): 
        return pygame.events.get()
    def GetKey():
        return pygame.key.get_pressed()
    def GetMousePos():
        return pygame.mouse.get_pos()
    def GetMouseButton():
        return pygame.mouse.get_pressed()
    def isColliding(obj1,obj2):
        return obj1.colliderect(obj2)


    def Draw(self, *args): #arg is (object, x, y)
        for arg in args:
            print(arg)
            self.screen.blit(arg[0],(arg[1],arg[2]))
        update_areas = [pygame.Surface.get_rect(x[0]) for x in args]
        print(update_areas)
        pygame.display.update(update_areas) #only update areas that requires it

        '''
        events = pygame.events.get()
        for event in events:
            # deal with events
        pygame.event.pump()
        my_sprites.do_stuff_every_loop()
        rects = my_sprites.draw()
        activerects = rects + oldrects
        activerects = filter(bool, activerects)
        pygame.display.update(activerects)
        oldrects = rects[:]
        for rect in rects:
            screen.blit(bgimg, rect, rect)
        '''    
        

if __name__ == '__main__':
    #If arcade.py is executed, open game selector UI
    #All games are executable as a standalone game.
    #All games are contained in a single .py file + resources (sprites, fonts, etc.)
    pygame.init()
    pygame.display.set_caption("Arcade")
    arcade = arcade()
    news = pygame.Surface((600,600))
    news.fill((255,255,255),(10,10,10,10))
    while True:
        arcade.Draw((news, 0, 0))
        arcade.InputEvents
    
    
