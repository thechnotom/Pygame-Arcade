import pygame, os, sys, random
from pygame.locals import *
from Arcade import arcade
from colours import *

global screen_width
screen_width = 460
global screen_height
screen_height = 600

class Jumper(pygame.sprite.Sprite):

    def __init__(self, jump_velocity, g, file = None):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((20,20))
        self.image.fill(pink)
        self.rect = self.image.get_rect()
        self.rect.x = 120
        self.jump_velocity = jump_velocity
        self.g = g
        self.velocity = 0

    def jump(self):
        self.velocity = self.jump_velocity * -1

    def update(self):
        self.rect.y += round(self.velocity)
        self.velocity += self.g

class BlockPair(pygame.sprite.Sprite):

    INTERVAL = 80
    WIDTH = 40
    GAP = 200
    SPEED = 4

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.dokill = False
        r = random.randint(120,380)

        self.top = pygame.Surface((BlockPair.WIDTH, r))
        self.top.fill(maroon)
        self.top_rect = self.top.get_rect()

        self.bottom = pygame.Surface((BlockPair.WIDTH, screen_height - r - BlockPair.GAP))
        self.bottom.fill(maroon)
        self.bottom_rect = self.bottom.get_rect()


        self.image = pygame.Surface((BlockPair.WIDTH, screen_height), pygame.SRCALPHA, 32)
        self.image.blit(self.bottom, (0, r + BlockPair.GAP))
        self.image.blit(self.top, (0,0))
        self.rect = self.image.get_rect()
        self.rect.x = screen_width
        
    def update(self):
        self.rect.x -= BlockPair.SPEED

        if self.rect.x < self.rect.width * -1:
            self.dokill = True


def Game(arcade):

    clock = pygame.time.Clock()
    screen = arcade.get_screen()
    arcade.setCaption(__file__)
    arcade.setWindow(screen_width, screen_height)
    font1 = pygame.font.SysFont('Arial',24, True)

    player = Jumper(16, 0.8)
    sprites = pygame.sprite.RenderUpdates()
    sprites.add(player)

    obstacles = pygame.sprite.RenderUpdates()
    pTimer = 0

    screen_rect = screen.get_rect()
    background = arcade.getImage(__file__, 'Background.png')
    background2 = arcade.getImage(__file__, 'Background.png')
    b_scroll = 0

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                player.jump()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                player.jump()

        pTimer +=1
        if pTimer >= BlockPair.INTERVAL:
            pTimer = 0
            obstacles.add(BlockPair())

        sprites.update()
        obstacles.update()
        for i in obstacles:
            if i.dokill == True: obstacles.remove(i)
        player.rect.clamp_ip(screen_rect)
        
        screen.blit(background, (b_scroll, 0))
        screen.blit(background2, (b_scroll - screen_width, 0))
        b_scroll += 6
        if b_scroll >= screen_width: b_scroll = 0
        
        obstacles.draw(screen)
        sprites.draw(screen)
        pygame.display.flip()
##        sprites.clear(screen, background)
##        obstacles.clear(screen, background)
##        pygame.display.update(
##            [pygame.Rect(r[0]-10, r[1], r[2]+20, r[3]) for r in obstacles.draw(screen)] +
##            [pygame.Rect(r[0], r[1]-10, r[2], r[3]+20) for r in sprites.draw(screen)])
        clock.tick(60)



if __name__ == '__main__':
    pygame.init()
    pygame.mixer.init(22050,-16,2,1024)
    Game(arcade())
