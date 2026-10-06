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
    'Settings': False,
}

#rectangles
menuRect = pygame.Rect(300,10,350,1060) #serves as the rectangle where the buttons to the side menu will be
levelSelectRect = pygame.Rect(700,10,400, 400)

#button images
levelSelectImg = pygame.image.load("levelSelect.png").convert_alpha() #convert_alpha() to remove transparent particles.
gameHelpImg = pygame.image.load("gameHelp.png").convert_alpha()
settingsImg = pygame.image.load("settings.png").convert_alpha()
accessibilityImg = pygame.image.load("Accessibility.png").convert_alpha()
accountStatImg = pygame.image.load("accountStats.png").convert_alpha()
vsImg = pygame.image.load("vsButton.png").convert_alpha()
practiseImg = pygame.image.load("practiseButton.png").convert_alpha()

#making the button objects
levelSelectButton = Button(300,20,levelSelectImg,1)
gameHelpButton = Button(300,100,gameHelpImg,1)
settingsButton = Button(300,200,settingsImg,1)
accessButton = Button(300,300,accessibilityImg,1)
accountStatButton = Button(300,400,accountStatImg,1)
vsButton = Button(700,10,vsImg,1)
practiseButton = Button(900,10,practiseImg,1)

#procedure that contains a dictionary of bool values that change if one of the corresponding buttons is pressed
def ButtonPress(ButName: str):
    """
    A procedure to alter a dictionary, updating when a button is pressed by making the corresponding value to True and setting the rest to False

    Args:
        ButName: contains the name of the button
    Returns:
        None
    """
    for button in butDict:
        butDict[button] = False #sets the entire dictionary to false when called
    butDict[ButName] = True #changes the chosen option to True


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

    #button press logic
    if levelSelectButton.draw() == True: # when pressed it will change the value for the "level" key in the dictionary to true
        ButtonPress("Level")
    if gameHelpButton.draw() == True:
        ButtonPress("Help")
    if accessButton.draw() == True:
        ButtonPress("Accessibility")
    if accountStatButton.draw() == True:
        ButtonPress("Stats")
    if settingsButton.draw() ==True:
        ButtonPress("Settings")

    if butDict["Level"] == True:
        pygame.draw.rect(screen, (173,216,230), levelSelectRect) # displays the rectangle that will serve as the background of the level selcet menu
        if vsButton.draw() == True:
            print("vs")
        if practiseButton.draw() == True:
            print("practise")