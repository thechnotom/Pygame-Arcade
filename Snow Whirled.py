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
    score1 = 0
    score2 = 0

    #images
    snowpic = arcade.getImage(__file__,'snowbackground.jpg')
    p1p1 = arcade.getImage(__file__,'p1p1.png')
    p1p2 = arcade.getImage(__file__,'p1p2.png')
    p1p3 = arcade.getImage(__file__,'p1p3.png')
    p1p4 = arcade.getImage(__file__,'p1p4.png')
    p2p1 = arcade.getImage(__file__,'p2p1.png')
    p2p2 = arcade.getImage(__file__,'p2p2.png')
    p2p3 = arcade.getImage(__file__,'p2p3.png')
    p2p4 = arcade.getImage(__file__,'p2p4.png')
    Down = arcade.getImage(__file__,'Down.bmp')
    Left = arcade.getImage(__file__,'Left.bmp')
    Up = arcade.getImage(__file__,'Up.bmp')
    Right = arcade.getImage(__file__,'Right.bmp')

    
    #Text
    Font1 = pygame.font.SysFont("monospace", 36)
    Font2 = pygame.font.SysFont("monospace", 18)

    label1 = Font1.render("Player 1 Score:           Player 2 Score:", 1, (0,0,0))
    label2 = Font1.render(str(score1), 1, (0,0,0))
    label3 = Font1.render(str(score2), 1, (0,0,0))
    label5 = Font2.render('Press Esc to Quit', 1, (0,0,0))
    label6 = Font1.render('Press Space to start', 1, (0,0,0))
    label7 = Font1.render('Time Left:', 1, (0,0,0))
  
    arcade.initBackground(snowpic)
    
    while True:   
        position = 1
        Start = 0
        TimeRem = 200

       

         #Timer
        while TimeRem > 0:
            arcade.drawBackground(snowpic)
            arcade.getEvents()
                        
            if TimeRem %10 == 0:
                label4 = Font1.render(str(TimeRem/20), 1, (0,0,0))
                label2 = Font1.render(str(score1), 1, (0,0,0))
                label3 = Font1.render(str(score2), 1, (0,0,0))

           
            if Start == 1:
                TimeRem -= 1

            #Key recognition    
            pressed = arcade.getKey()
            
            if pressed[K_ESCAPE]:
                pygame.quit()
                sys.exit()
                
            if pressed[K_SPACE]:
                Start = 1
                
            if position == 1 and pressed[K_DOWN] and not any([pressed[K_LEFT],pressed[K_UP],pressed[K_RIGHT]]) and Start == 1:
                position = 2

                #Scoring for players 
                if  player == 1:
                    score1 += 90 
                elif player == 2:
                    score2 += 90
                    
            if position == 2 and pressed[K_LEFT] and not any([pressed[K_DOWN],pressed[K_UP],pressed[K_RIGHT]]) and Start == 1:
                position = 3

                #Scoring for players 
                if  player == 1:
                    score1 += 90
                elif player == 2:
                    score2 += 90                    
            if position == 3 and pressed[K_UP] and not any([pressed[K_LEFT],pressed[K_DOWN],pressed[K_RIGHT]]) and Start == 1:
                position = 4

                #Scoring for players 
                if  player == 1:
                    score1 += 90
                elif player == 2:
                    score2 += 90
                    
            if position == 4 and pressed[K_RIGHT] and not any([pressed[K_LEFT],pressed[K_UP],pressed[K_DOWN]]) and Start == 1:
                position = 1

                #Scoring for players 
                if  player == 1:
                    score1 += 90
                elif player == 2:
                    score2 += 90

            if Start == 0 and player == 1:
                arcade.draw ((p1p1, 300, 650),(Down, 700, 300),(label4, 700, 100),(label1, 100, 800),(label2, 420, 800),(label3, 1000, 800),(label5, 0, 0),(label7, 480, 100))
            elif position == 1 and Start == 1 and player == 1:
                arcade.draw ((p1p1, 300, 350),(Down, 700, 300),(label4, 700, 100),(label1, 100, 800),(label2, 420, 800),(label3, 1000, 800),(label5, 0, 0),(label7, 480, 100))
            elif position == 2 and Start == 1 and player == 1:
                arcade.draw ((p1p2, 300, 350),(Left, 700, 300),(label4, 700, 100),(label1, 100, 800),(label2, 420, 800),(label3, 1000, 800),(label5, 0, 0),(label7, 480, 100))
            elif position == 3 and Start == 1 and player == 1:
                arcade.draw ((p1p3, 300, 350),(Up, 700, 300),(label4, 700, 100),(label1, 100, 800),(label2, 420, 800),(label3, 1000, 800),(label5, 0, 0),(label7, 480, 100))
            elif position == 4 and Start == 1 and player == 1:
                arcade.draw ((p1p4, 300, 350),(Right, 700, 300),(label4, 700, 100),(label1, 100, 800),(label2, 420, 800),(label3, 1000, 800),(label5, 0, 0),(label7, 480, 100))

            if Start == 0 and player == 2:
                arcade.draw ((p2p1, 300, 650),(Down, 700, 300),(label4, 700, 100),(label1, 100, 800),(label2, 420, 800),(label3, 1000, 800),(label5, 0, 0),(label7, 500, 100))
            elif position == 1 and Start == 1 and player == 2:
                arcade.draw ((p2p1, 300, 350),(Down, 700, 300),(label4, 700, 100),(label1, 100, 800),(label2, 420, 800),(label3, 1000, 800),(label5, 0, 0),(label7, 500, 100))
            elif position == 2 and Start == 1 and player == 2:
                arcade.draw ((p2p2, 300, 350),(Left, 700, 300),(label4, 700, 100),(label1, 100, 800),(label2, 420, 800),(label3, 1000, 800),(label5, 0, 0),(label7, 500, 100))
            elif position == 3 and Start == 1 and player == 2:
                arcade.draw ((p2p3, 300, 350),(Up, 700, 300),(label4, 700, 100),(label1, 100, 800),(label2, 420, 800),(label3, 1000, 800),(label5, 0, 0),(label7, 500, 100))
            elif position == 4 and Start == 1 and player == 2:
                arcade.draw ((p2p4, 300, 350),(Right, 700, 300),(label4, 700, 100),(label1, 100, 800),(label2, 420, 800),(label3, 1000, 800),(label5, 0, 0),(label7, 500, 100))

            #arcade.draw ((label6, 400, 200))

        if player == 2:
            break
        position = 1
        player = 2

        
if __name__ == '__main__':
    pygame.init()
    pygame.mixer.init(22050,-16,2,1024)
    pygame.display.set_caption(os.path.basename(__file__).split('.')[0])
    SnowWhirled(arcade())
