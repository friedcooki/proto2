import pygame

class Button:
    """ 
    An image based button, detects when it is clicked and only registered once per action.
    The buttons only appear when the method is called.

    """
    def __init__(self, image, scale : float):
        """
        initialises a Button

        Args:
            image: The image to be used to display the button from a local png
            scale (float): A float used to scale the png of the image, either to make it bigger or smaller

        Returns:
            None

        """
        height = image.get_height() #gets the width and height to be used for scale
        width = image.get_width()
        self.scale = scale
        self.image = pygame.transform.scale(image, (int(width*scale),int(height*scale))) #scales the image's height and width based on the scale input by the user
        self.clicked = False
        self.topleft = None

    def draw(self, x: int, y: int):
        """
        displays the button on screen

        Args:
            x (int): the x coordinate of the top left corner of the button
            y (int): the y coordinate of the top right corner of the button
        Returns:
            None

        """
        self.x = x
        self.y = y
        screen.blit(self.image,(self.x, self.y))
    
    def onClick(self):
        """
        this will be called when the button is clicked

        """




class Levelselect(Button):

    def __init__(self):
        levelSelectImg = pygame.image.load("levelSelect.png").convert_alpha()
        super().__init__(levelSelectImg, 1) #calls the init of button and takes it argumetns
    
    def onClick(self):
        
        """
        this should open up to a new menu
        """
        

        """
        their own buttons, mnake the link in the menu class
        vsButton.draw()
        practiseButton.draw()
        if vsButton.onClick() == True:
            vsPlaceholder = True #when the button is pressed this allows the placeholder screens to be shown
        if practiseButton.onClick() == True:
           practisePlaceholder = True
        """

        

class StartMenu:
    """
    class for the main menu

    """

    def __init__(self, buttons: list,x: int, y: int, width: int, length: int):
        """
        initialises a menu

        Args:
            buttons (list): a list of all the buttons to be displayed on the menu
            x(int): an int for the x coordinate of the top left corner of the menu
            y(int): an int for the y coordinate of the top left corner of the menu
            width(int): an int for the width of the menu
            length(int): an int for the length of the menu

        Returns:
            None

        """

        self.x = x
        self.y = y
        self.width = width
        self.length = length
        self.buttons = buttons

    def menuDraw(self):
        """
        Draws the menu on the screen

        Args:
            None

        Returns:
            None

        """

        menuRect = pygame.Rect(self.x,self.y,self.width,self.length)
        #display the rect for the menu
        pygame.draw.rect(screen,(0,0,139), menuRect) #displays the rectangle as darkblue
    
    def buttonDraw(self, xSpace :int, ySpace :int, buttonX:int, buttonY:int):
        """
        this will take the buttons in the list and display them on the menu
        
        Args:
            xSpace: the seperation of the buttons in the x direction in px
            ySpace: the seperations of the buttons in the y direction in px
            buttonX: The x coordinate of the top left of the first button
            buttonY: The y coordinate of the top left of the first button
        Return:
            None

        """

        for button in self.buttons:
            button.draw(buttonX,buttonY)
            buttonX = buttonX + xSpace
            buttonY = buttonY + ySpace #add the button size



#class SecondaryMenu(StartMenu):

            



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
vsPlaceholder: bool = False
practisePlaceholder:bool = False
secondMenuCol = (173,216,230)
blackText = (0,0,0)
#Button variables
levelPressed: bool = False  #i will use these values in the event loop for the pop out menus
helpPressed: bool = False
settingsPressed: bool = False
accessPressed: bool = False
statsPressed: bool = False




#rectangles
menuRect = pygame.Rect(300,10,350,1060) #serves as the rectangle where the buttons to the side menu will be
levelSelectRect = pygame.Rect(700,10,400, 400)
gameHelpRect = pygame.Rect(700,30,400,600)
settingsRect = pygame.Rect(700,50,400,600)
accessibilityRect = pygame.Rect(700,70,400,400)
statsRect = pygame.Rect(700, 90, 400,400)
blankRect = pygame.Rect(0,0,1920,1080)


#button images

gameHelpImg = pygame.image.load("gameHelp.png").convert_alpha()
settingsImg = pygame.image.load("settings.png").convert_alpha()
accessibilityImg = pygame.image.load("Accessibility.png").convert_alpha()
accountStatImg = pygame.image.load("accountStats.png").convert_alpha()
vsImg = pygame.image.load("vsButton.png").convert_alpha()
practiseImg = pygame.image.load("practiseButton.png").convert_alpha()

#making the button objects
levelButton = Levelselect() #300,20
gameHelpButton = Button(gameHelpImg,1) #300,100
settingsButton = Button(settingsImg,1) #300,200
accessButton = Button(accessibilityImg,1) #300,400
accountStatButton = Button(accountStatImg,1) #300,400
vsButton = Button(vsImg,1) #700,10
practiseButton = Button(practiseImg,1) #900.10

#button list
buttonList = [levelButton]

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

start = StartMenu(buttonList, 300,10,350,1060) #(self, buttons: list[Button],x: int, y: int, width: int, length: int):


#game loop
while run:
    #check if the game is closed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    start.menuDraw()
    start.buttonDraw(0, 20, 300, 10)



    #sets fps and makes sure screen is updated
    pygame.display.update()
    clock.tick(60) #60 fps
    
    #colour the screen
    screen.fill((255,255,255))

   
"""
    if gameHelpButton.draw() == True:
        ButtonPress("Help")
    if accessButton.draw() == True:
        ButtonPress("Accessibility")
    if accountStatButton.draw() == True:
        ButtonPress("Stats")
    if settingsButton.draw() ==True:
        ButtonPress("Settings")

    if butDict["Level"] == True:
        pygame.draw.rect(screen, secondMenuCol, levelSelectRect) # displays the rectangle that will serve as the background of the level selcet menu

            
    if vsPlaceholder == True:
        pygame.draw.rect(screen,(255,255,255),blankRect)#displays the placeholder screens
        textDraw("taking you to a vs game", normalFont,bblackText,10,10)
        
    if practisePlaceholder == True:
        pygame.draw.rect(screen,(255,255,255), blankRect)
        textDraw("taking you to a practise game",normalFont,blackText,10,10)
        
    if butDict["Help"] == True:
        pygame.draw.rect(screen,secondMenuCol,gameHelpRect) #displays the secondary menu for game help
        textDraw("Rules:",normalFont,blackText,700,50)
        
    if butDict["Settings"] == True:
        pygame.draw.rect(screen,secondMenuCol,settingsRect) #displays the menu and the texts
        textDraw("difficulty:", normalFont,blackText,700,50)
        textDraw("friction:", normalFont,blackText, 700,250)
        
    if butDict["Accessibility"] == True: #displays the accessibility screen
        pygame.draw.rect(screen,secondMenuCol,accessibilityRect)
        textDraw("high contrast mode:",normalFont,blackText,700,100) #marker for the selects for high cotnrast mode
        
    if butDict["Stats"] == True: #displays the account stats screen
        pygame.draw.rect(screen,secondMenuCol,statsRect)
        textDraw("stats: ", normalFont, blackText, 700, 100) #lets the user know what is being displayed
        """