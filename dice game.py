import pygame, random,sys  #color is a module I made containing a list of variables with RGB values
pygame.init



Dice1 = pygame.image.load("Dice1.png")
Dice2 = pygame.image.load("Dice2.png")
Dice3 = pygame.image.load("Dice3.png")
Dice4 = pygame.image.load("Dice4.png")
Dice5 = pygame.image.load("Dice5.png")
Dice6 = pygame.image.load("Dice6.png")

Dice = [Dice1,Dice2,Dice3,Dice4,Dice5,Dice6]

splash = ["Bet until you're broke!","Rags to riches, and back to rags again","You aren't depending on this money, right?","Snake Eyes","MONEY!","Cause I'm a gambler","double or nothing"]

Random_Splash = random.choice(splash)

Window_Size = 600
screen = pygame.display.set_mode((Window_Size,Window_Size))
pygame.display.set_caption('Gamble: ' + Random_Splash)
screen.fill(pygame.Color.maroon)    #refrincing color module
pygame.display.update()
icon = random.choice(Dice)
pygame.display.set_icon(icon)

def main():

    def TEXT(size,Color,msg,x=0,y=0):
        if size == 1:
            Font = pygame.font.SysFont("None",15)
        elif size == 2:
            Font = pygame.font.SysFont("None",30)
        elif size == 3:
            Font = pygame.font.SysFont("None",45)
        elif size == 4:
            Font = pygame.font.SysFont("None",60)

        text = Font.render(msg,True,Color)

        screen.blit(text,(x,y))


    while True:



        TEXT(2,color.red,"Hi")    #refrincing color module

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


main()