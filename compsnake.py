import pygame, sys, random, time


playSurface = pygame.display.set_mode((720, 460))
pygame.display.set_caption('Snake game!')

red = pygame.Color(255, 0, 0) # gameover
green = pygame.Color(0, 255, 0) #snake
black = pygame.Color(0, 0, 0) #score
white = pygame.Color(255, 255, 255) #background
brown = pygame.Color(165, 42, 42) #food

fpsController = pygame.time.Clock()

snakePos = [100, 50]
snakeBody = [[100,50], [90,50], [80,50]]

foodPos = [random.randrange(1,72)*10,random.randrange(1,46)*10]
foodSpawn = True

direction = 'RIGHT'
changeto = direction

score=0

# Game over function
def gameOver():
    myFont = pygame.font.SysFont('monaco', 72)
    GOsurf = myFont.render('Game over!', True, red)
    GOrect = GOsurf.get_rect()
    GOrect.midtop = (360, 15)
    playSurface.blit(GOsurf,GOrect)
    show_score(0)
    pygame.display.flip()

    time.sleep(4)
    pygame.quit() #pygame exit
    sys.exit() #console exit

def show_score():
    Ssfont=pygame.font.SysFont('monaco',True,45)
    Sssurf=Ssfont.render("Score is {}".format(score))
    Ssrect=Sssurf.get_rect()
    Ssrect.midtop(350,14)
    playSurface.blit(Sssurf,Ssrect)
    pygame.display.flip()
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT or event.type==ord('d'):
                changeto='RIGHT'
            if event.key==pygame.K_LEFT or event.type==ord('a'):
                changeto='LEFT'
            if event.key==pygame.K_UP or event.type==ord('w'):
                changeto='UP'
            if event.key==pygame.K_DOWN or event.type==ord('s'):
                changeto='DOWN'
            if event.key==pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

    if changeto=='RIGHT' and not direction=='LEFT':
        direction='RIGHT'
    if changeto=='UP' and not direction=='DOWN':
        direction='UP'
    if changeto=='LEFT' and not direction=='RIGHT':
        direction='LEFT'
    if changeto=='DOWN' and not direction=='UP':
        direction='DOWN'

    if direction == 'RIGHT':
        snakePos[0] += 10
    if direction == 'LEFT':
        snakePos[0] -= 10
    if direction == 'UP':
        snakePos[1] -= 10
    if direction == 'DOWN':
        snakePos[1] += 10

    snakeBody.insert(0, list(snakePos))
    if snakePos[0] == foodPos[0] and snakePos[1] == foodPos[1]:
        foodSpawn = False
    else:
        snakeBody.pop()

    if foodSpawn == False:
        foodPos = [random.randrange(1, 72)*10, random.randrange(1, 46)*10]
    foodSpawn = True

    playSurface.fill(white)


    for pos in snakeBody:
        pygame.draw.rect(playSurface, green, pygame.Rect(pos[0],pos[1],10,10))

    pygame.draw.rect(playSurface, brown, pygame.Rect(foodPos[0],foodPos[1],10,10))




    if snakePos[0] > 710 or snakePos[0] < 0:
        gameOver()
    if snakePos[1] > 450 or snakePos[1] < 0:
        gameOver()

    for posi in snakeBody[1:]:
        if posi[0]==snakePos[0] or posi[1]==snakePos[1]:
            gameOver()

    pygame.display.flip()
    fpsController.tick(25)





gameOver()

