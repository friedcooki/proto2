import pygame
from loginScreenScript import *

#make the game window
pygame.init()
#set up the screen
screenDimentions:tuple[int,int] = (1920,1080) #pygame.display expects a tuple
#make the screen:
screen = pygame.display.set_mode(screenDimentions)
#set frames per second
clock = pygame.time.Clock()

#game variables
run: bool = True #activates the game loop
textColour: tuple[int,int,int] = (255,255,255)
inputColour: tuple[int,int,int] = (0,0,0)
welcomeFont: pygame.font.Font = pygame.font.SysFont("arialblack", 40)
normalFont: pygame.font.Font = pygame.font.SysFont("arial", 20)
#Button variables
levelPressed: bool = False  #i will use these values in the event loop for the pop out menus
helpPressed: bool = False
settingsPressed: bool = False
accessPressed: bool = False
statsPressed: bool = False
#button dictionary
butDict = {
    'Level': False,
    'Help': False,
    'Stats': False,
    'Accessibility': False,
    'settings': False,
}

#rectangles
menuRect = pygame.Rect(300,10,350,1060) #serves as the rectangle where the buttons to the side menu will be

#button images
levelSelectImg = pygame.image.load("levelSelect.png").convert_alpha() #convert_alpha() to remove transparent particles.
gameHelpImg = pygame.image.load("gameHelp.png").convert_alpha()
settingsImg = pygame.image.load("settings.png").convert_alpha()
accessibilityImg = pygame.image.load("Accessibility.png").convert_alpha()
accountStatImg = pygame.image.load("accountStats.png").convert_alpha()

#making the button objects
levelSelectButton = Button(300,20,levelSelectImg,1)
gameHelpButton = Button(300,100,gameHelpImg,1)
settingsButton = Button(300,200,settingsImg,1)
accessButton = Button(300,300,accessibilityImg,1)
accountStatButton = Button(300,400,accountStatImg,1)

#function that contains a dictionary of bool values that change if one of the corresponding buttons is pressed
def ButtonPress(ButName: str):
    for button in butDict:
        butDict[button] = False #sets the entire dictionary to false when called
    butDict[ButName] = True #changes the chosen option to True
    ######## add to word


#game loop
while run:
    #check if the game is closed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()




    #sets fps and makes sure screen is updated
    pygame.display.update()
    clock.tick(60) #60 fps
    
    #colour the screen
    screen.fill((255,255,255))

    #display the rect for the menu
    pygame.draw.rect(screen,(0,0,139), menuRect) #displays the rectangle as darkblue

    #testing menu buttons
    if levelSelectButton.draw() == True: # when pressed it will print level select
        levelPressed = True  # sets one as true and the rest as false to stop multiple menus from opening at once
        helpPressed = False
        settingsPressed = False
        accessPressed = False
        statsPressed = False
    if gameHelpButton.draw() == True:
        levelPressed = False  
        settingsPressed = False
        accessPressed = False
        statsPressed = False
        helpPressed = True
    if accessButton.draw() == True:
        levelPressed = False  
        helpPressed = False
        settingsPressed = False
        accessPressed = True
        statsPressed = False
    if accountStatButton.draw() == True:
        levelPressed = False  
        helpPressed = False
        settingsPressed = False
        accessPressed = False
        statsPressed = True
    if settingsButton.draw() ==True:
        levelPressed = False 
        helpPressed = False
        settingsPressed = True
        accessPressed = False
        statsPressed = False

    

    

