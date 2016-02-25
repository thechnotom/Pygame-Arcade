# This file provides some code for you to get started with your game.
# Hopefully you understand the basics of python and pygame by now.
#
# If you have any questions, please feel free to ask Will or Kian for help.
#
# Also, please remeber to change this file to be the name of your game.

import pygame, os
from pygame.locals import *
from Arcade import arcade

# Here you can place your game's procedures and/or classes. 

'''
If you want to make a game with classes, I'll assume you don't
need an example. If you want help with this, ask.

Here is an example of a very simple game running as a procedure:

def Game(arcade):

    # For pictures files: .png; .jpg; .gif; .bmp
    picture = arcade.GetImage('picture_filename.png')

    # For sound files: .wav; .ogg; .mp3
    music = arcade.GetSound('song_filename.')

    #Assign default values for your game here
    player_x, player_y = 100, 100
    enemy_x, enemy_y = 500, 500
    alive = True

    #Play music
    music.play(-1)

    #Loops while the character variable is equal to True
    while alive:


        # Gets keyboard input using 'arcade.GetKey'
        
        pressed = arcade.GetKey()
        
        if pressed['K_w'] or pressed['K_UP']:
            player_y -= 1
            
        if pressed['K_s'] or pressed['K_DOWN']:
            player_y += 1
            
        if pressed['K_a'] or pressed['K_LEFT']:
            player_x -= 1
            
        if pressed['K_d'] or pressed['K_RIGHT']:
            player_x += 1



        # Draws the player and the enemy
        # Drawing is done by using 'arcade.Draw()', and passing (object, x ,y)

        arcade.Draw((player, player_x, player_y),(enemy, enemy_x, enemy_y))
        
    
    
'''


# This line should be the first thing your program runs if it
# has been run without the arcade program.
#
# If this file was excecuted by running it directly, __name__ will be
# equal to __main__, and your code will run. Otherwise, your code will
# be handled by the arcade file.
if __name__ == '__main__':

    #initializes pygame and mixer
    pygame.init()
    pygame.mixer.init(22050,-16,2,1024)
    #Gives your game window a caption. The file name is the caption.
    pygame.display.set_caption(os.path.basename(__file__).split('.')[0])
    

    # Run procedures and/or classes here
    # Example:
    #Game(arcade())




################################################################################
################################################################################
# Below is all the code from the game base without the comments. I recomended  #
# you build your game starting from this code. If you have any questions       #
# do not hesitate to ask Kian or Will.                                         #
################################################################################
################################################################################

import pygame, os
from pygame.locals import *
from Arcade import arcade

if __name__ == '__main__':
    pygame.init()
    pygame.mixer.init(22050,-16,2,1024)
    pygame.display.set_caption(os.path.basename(__file__).split('.')[0])


