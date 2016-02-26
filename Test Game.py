import pygame, os
from pygame.locals import *
from Arcade import arcade


def Game(arcade):
    
    
    ball_x, ball_y = 290, 290
    ball = pygame.Surface((20,20))
    pygame.draw.circle(ball, arcade.colour('blue'), (10,10), 10)
    speed_x, speed_y = 3, 3

    player_x, player_y = 300, 550
    player = pygame.Surface((100, 25))
    player.fill((255,255,255),(0,0,100,25))

    background = pygame.Surface((600,600))
    background.fill(arcade.colour('red'),(0,0,600,600))
    arcade.InitBackground(background)

    last = pygame.time.get_ticks()
    cooldown = 5
    alive = True
    
    while alive:
        arcade.GetEvents()
        now = pygame.time.get_ticks()
        if now - last >= cooldown:
            last = now

            pressed = arcade.GetKey()
            if pressed[K_a] or pressed[K_LEFT]:
                player_x -= 5
            if pressed[K_d] or pressed[K_RIGHT]:
                player_x += 5

            
            arcade.DrawBackground(background)
            arcade.Draw((player, player_x, player_y),
                        (ball, ball_x, ball_y))

if __name__ == '__main__':
    pygame.init()
    pygame.mixer.init(22050,-16,2,1024)
    pygame.display.set_caption(os.path.basename(__file__).split('.')[0])
    Game(arcade())
