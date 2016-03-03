#Snow Whirled
#Class: ICS4U-02
#Name: Alex Taylor & Andrew Foster
#Date: March 3, 2016
#Description: 2-player snowboarding twirller

import pygame, os, sys
from pygame.locals import *
from Arcade import arcade
from colours import *

def SnowWhirled(arcade):

    arcade.setWindow(1250,900)

    player = 1
    
    while True:
        position = 1
        start = 0
        TimeRem = 5000
        while TimeRem > 0:
            
            arcade.getEvents()
            if Start = 1:
                TimeRem -= 1
            pressed = arcade.getKey()
            if pressed[K_ESCAPE]:
                pygame.quit()
                sys.exit()
            if pressed[K_SPACE]:
                start = 1
            if position == 1 and pressed[K_DOWN] and not any(pressed[K_LEFT],pressed[K_UP],pressed[K_RIGHT]):
                position = 2
                if  player == 1
                    score1 += 90
                elif player == 2
                    score2 += 90
            if position == 2 and pressed[K_LEFT] and not any(pressed[K_DOWN],pressed[K_UP],pressed[K_RIGHT]):
                position = 3
                if  player == 1
                    score1 += 90
                elif player == 2
                    score2 += 90
            if position == 3 and pressed[K_UP] and not any(pressed[K_LEFT],pressed[K_DOWN],pressed[K_RIGHT]):
                position = 4
                if  player == 1
                    score1 += 90
                elif player == 2
                    score2 += 90
            if position == 4 and pressed[K_RIGHT] and not any(pressed[K_LEFT],pressed[K_UP],pressed[K_DOWN]):
                position = 1
                if  player == 1
                    score1 += 90
                elif player == 2
                    score2 += 90

            player = 2
        
if __name__ == '__main__':
    pygame.init()
    pygame.mixer.init(22050,-16,2,1024)
    pygame.display.set_caption(os.path.basename(__file__).split('.')[0])
    SnowWhirled(arcade())
