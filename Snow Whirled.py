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

    snowpic = arcade.getImage(__file__,'snowbackground.jpg')
    p1p1 = arcade.getImage(__file__,'p1p1.bmp')
    p1p2 = arcade.getImage(__file__,'p1p2.bmp')
    p1p3 = arcade.getImage(__file__,'p1p3.bmp')
    p1p4 = arcade.getImage(__file__,'p1p4.bmp')
    p2p1 = arcade.getImage(__file__,'p2p1.bmp')
    p2p2 = arcade.getImage(__file__,'p2p2.bmp')
    p2p3 = arcade.getImage(__file__,'p2p3.bmp')
    p2p1 = arcade.getImage(__file__,'p2p4.bmp')    

    Font1 = pygame.font.SysFont("monospace", 36)

    label1 = Font1.render("Player 1 Score           Player 2 Score", 1, (0,0,0))
    label2 = Font2.render(str(score1), 1, (0,0,0))
    label3 = Font2.render(str(score2), 1, (0,0,0))
    
    while True:
        #Declaration of Variables        
        position = 1
        start = 0
        TimeRem = 5000
        
        while TimeRem > 0:
            arcade.drawBackground(snowpic)
            arcade.getEvents()

            #Timer
            if Start == 1:
                TimeRem -= 1

            #Key recognition    
            pressed = arcade.getKey()
            
            if pressed[K_ESCAPE]:
                pygame.quit()
                sys.exit()
                
            if pressed[K_SPACE]:
                start = 1
                
            if position == 1 and pressed[K_DOWN] and not any(pressed[K_LEFT],pressed[K_UP],pressed[K_RIGHT]):
                position = 2

                #Scoring for players 
                if  player == 1:
                    score1 += 90 
                elif player == 2:
                    score2 += 90
                    
            if position == 2 and pressed[K_LEFT] and not any(pressed[K_DOWN],pressed[K_UP],pressed[K_RIGHT]):
                position = 3

                #Scoring for players 
                if  player == 1:
                    score1 += 90
                elif player == 2:
                    score2 += 90
                    
            if position == 3 and pressed[K_UP] and not any(pressed[K_LEFT],pressed[K_DOWN],pressed[K_RIGHT]):
                position = 4

                #Scoring for players 
                if  player == 1:
                    score1 += 90
                elif player == 2:
                    score2 += 90
                    
            if position == 4 and pressed[K_RIGHT] and not any(pressed[K_LEFT],pressed[K_UP],pressed[K_DOWN]):
                position = 1

                #Scoring for players 
                if  player == 1:
                    score1 += 90
                elif player == 2:
                    score2 += 90

            if Start == 0 and player == 1:
                arcade.draw ((p1p1, 600, 200))
            if position == 1 and Start == 1 and player == 1:
                arcade.draw ((p1p1, 600, 500))
            if position == 2 and Start == 1 and player == 1:
                arcade.draw ((p1p2, 600, 500))
            if position == 3 and Start == 1 and player == 1:
                arcade.draw ((p1p3, 600, 500))
            if position == 4 and Start == 1 and player == 1:
                arcade.draw ((p1p4, 600, 500))

            if Start == 0 and player == 2:
                arcade.draw ((p2p1, 600, 200))
            if position == 1 and Start == 1 and player == 2:
                arcade.draw ((p2p1, 600, 500))
            if position == 2 and Start == 1 and player == 2:
                arcade.draw ((p2p2, 600, 500))
            if position == 3 and Start == 1 and player == 2:
                arcade.draw ((p2p3, 600, 500))
            if position == 4 and Start == 1 and player == 2:
                arcade.draw ((p2p4, 600, 500))

        if player == 2:
            break
        player = 2

        
if __name__ == '__main__':
    pygame.init()
    pygame.mixer.init(22050,-16,2,1024)
    pygame.display.set_caption(os.path.basename(__file__).split('.')[0])
    SnowWhirled(arcade())
