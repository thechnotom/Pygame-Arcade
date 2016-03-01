import pygame, os, sys
from pygame.locals import *
from Arcade import arcade
from colours import *

def Game(arcade):

    arcade.setCaption(__file__)
    
    ball_x, ball_y = 290, 290
    ball = arcade.makeSurface(20,20,1)
    pygame.draw.circle(ball, gold, (10,10), 10)

    player_x, player_y = 250, 550
    player = arcade.makeSurface(100, 25)
    player.fill(navy,(0,0,100,25))

    background = pygame.Surface((600,600))
    background.fill(green,(0,0,600,600))
    arcade.initBackground(background)

    last = pygame.time.get_ticks()
    cooldown = 8
    alive = True

    dy = 3
    dx = 2

    
    while alive:
        arcade.getEvents()
        now = pygame.time.get_ticks()
        while now - last >= cooldown:
            last = now

            pressed = arcade.getKey()
            if pressed[K_a] or pressed[K_LEFT]:
                player_x -= 5
            if pressed[K_d] or pressed[K_RIGHT]:
                player_x += 5
            if pressed[K_ESCAPE]:
                pygame.quit()
                sys.exit()

            ball_y -= dy
            ball_x -= dx
    
            if ball_y <= 0:
                dy *= -1
            if ball_y >= 600:
                #you lose
                dy *= -1
            if ball_x <= 0:
                dx *= -1
            if ball_x >= 600:
                dx *= -1  
            
        arcade.drawBackground(background)
        arcade.draw((player, player_x, player_y),
                    (ball, ball_x, ball_y))

if __name__ == '__main__':
    pygame.init()
    pygame.mixer.init(22050,-16,2,1024)
    Game(arcade())
