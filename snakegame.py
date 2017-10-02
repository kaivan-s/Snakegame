import pygame, sys, time
import random as r


play_surface = pygame.display.set_mode((720, 460))
pygame.display.set_caption('SnakeGame')

red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
black = pygame.Color(0, 0, 0)
brown = pygame.Color(146, 42, 42)
white = pygame.Color(255, 255, 255)

fps_control = pygame.time.Clock()

snake_pos = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]

food_pos = [[r.randrange(1, 72)*10, r.randrange(1, 46)*10]]
food_spawn = True

dir_r = 'Right'
Change_to = dir_r

def gameOver():
    myFont = pygame.font.SysFont('monaco', 72)
    GOsurf = myFont.render('Game over!', True, red)
    GOrect = GOsurf.get_rect()
    GOrect.midtop = (360, 15)
    play_surface.blit(GOsurf,GOrect)
    # showScore(0)
    pygame.display.flip()

    time.sleep(4)
    pygame.quit() #pygame exit
    sys.exit() #console exit

gameOver()
time.sleep(5)





