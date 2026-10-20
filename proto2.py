import pygame
from loginScreenScript import textDraw #imports a function that displays text on screen when called

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
        self.rect = self.image.get_rect()
        self.action = None

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
        self.rect.topleft = (self.x, self.y)
        screen.blit(self.image,(self.x, self.y))
    
    def onClick(self):
        """
        this will be called when the button is clicked

        """

    def isClicked(self):
        """
        detects if the button is clicked

        Args:
            None
        Returns: 
            bool - True if the button is clicked, False if not

        """
        pos = pygame.mouse.get_pos()
        pressed = pygame.mouse.get_pressed()[0] #checks the mouse pos and if left click was pressed
        if self.rect.collidepoint(pos) == True:
            if pressed and not self.clicked:
                self.clicked = True #if it was self.action is set to true and self.clicked is set to true
                self.action = True
            if not pressed:
                self.clicked = False #if not then self.clicked and self.action are set to false
            return self.action #returns self.action




class Levelselect(Button):

    def __init__(self):
        levelSelectImg = pygame.image.load("levelSelect.png").convert_alpha()
        super().__init__(levelSelectImg, 1) #calls the init of button and takes it argumetns
        self.opened : bool = False
    
    def onClick(self):
        
        """
        this will open up to the secondary menu and load the buttons that go on that screen

        Args:
            None
        Returns:
            None
            
        """
        self.opened = not self.opened
        if not self.opened:
            return 
        secondaryButton = [vsButton, practiseButton]
        secMenu = SecondaryMenu(secondaryButton)
        secMenu.menuDraw()
        secMenu.buttonDraw(0,0,700,10)
        print("level select has been clicked")   ########make a seperate method for drawing the menu


class GameHelp(Button):
    def __init__(self):
        gameHelpImg = pygame.image.load("gameHelp.png").convert_alpha()
        super().__init__(gameHelpImg,1) #uses the superclass init

    def onClick(self):
        "This will open to the secondary menu and load the buttons"
        pass

class Settings(Button):
    def __init__(self):
        settingsImg = pygame.image.load("settings.png").convert_alpha()
        super().__init__(settingsImg,1) #uses the superclass init to set the image and scale

    def onClick(self):
        "This will open to the secondary menu and load the buttons"
        pass

class Accessibility(Button):
    def __init__(self):
        accessibilityImg = pygame.image.load("Accessibility.png").convert_alpha()
        super().__init__(accessibilityImg,1)
    def onClick(self):
        "This will open to the secondary menu and load the buttons"
        pass

class AccountStats(Button):
    def __init__(self):
        accountStatImg = pygame.image.load("accountStats.png").convert_alpha()
        super().__init__(accountStatImg,1)

    def onClick(self):
        "This will open to the secondary menu and load the buttons"
        pass

class Vsbutton(Button):
    def __init__(self):
        vsImg = pygame.image.load("vsButton.png").convert_alpha()
        super().__init__(vsImg,1)
    def onClick(self):
        pygame.draw.rect(screen,(255,255,255),blankRect)#displays the placeholder screens
        textDraw("taking you to a vs game", normalFont,blackText,10,10)

class Practise(Button):
    def __init__(self):
        practiseImg = pygame.image.load("practiseButton.png").convert_alpha()
        super().__init__(practiseImg,1)
    def onClick(self):
        pygame.draw.rect(screen,(255,255,255), blankRect) # this will display text and the place holder screen
        textDraw("taking you to a practise game",normalFont,blackText,10,10)









        

class StartMenu:
    """
    class for the main menu

    """

    def __init__(self,x: int, y: int, width: int, length: int,buttons):
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
        self.buttons = buttons if buttons != None else []

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
        
        self.isClicked()
            
        
    def isClicked(self):
        """
        detects if the button is clicked

        Args:
            None
        Returns: 
            bool - True if the button is clicked, False if not

        """
        for button in self.buttons:
            
            pos = pygame.mouse.get_pos()
            pressed = pygame.mouse.get_pressed()[0] #checks the mouse pos and if left click was pressed
            if button.rect.collidepoint(pos) and pressed:
                print("clicked - menu")
                button.onClick()

            print(button.rect.collidepoint(pos))


class SecondaryMenu(StartMenu):

    def __init__(self, buttons: list):
            super().__init__(700, 10, 600,600, None )
            self.buttons = buttons

    def menuDraw(self):
        """
        Draws the menu on the screen

        Args:
            None

        Returns:
            None

        """
        secondaryRect = pygame.Rect(self.x, self.y, self.width, self.length)
        pygame.draw.rect(screen, secondMenuCol,secondaryRect)




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
startButton : bool = None




#rectangles
#menuRect = pygame.Rect(300,10,350,1060) #serves as the rectangle where the buttons to the side menu will be
levelSelectRect = pygame.Rect(700,10,400, 400)
gameHelpRect = pygame.Rect(700,30,400,600)
settingsRect = pygame.Rect(700,50,400,600)
accessibilityRect = pygame.Rect(700,70,400,400)
statsRect = pygame.Rect(700, 90, 400,400)
blankRect = pygame.Rect(0,0,1920,1080)


#making the button objects
levelButton = Levelselect() #300,20
gameHelpButton = GameHelp() #300,100
settingsButton = Settings() #300,200
accessButton = Accessibility() #300,400
accountStatButton = AccountStats() #300,400
vsButton = Vsbutton() #700,10
practiseButton = Practise() #900.10

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

start = StartMenu(300,10,350,1060,buttonList) #(self, buttons: list[Button],x: int, y: int, width: int, length: int):


#game loop
while run:
    
    start.menuDraw()
    start.buttonDraw(0, 20, 300, 10) #def buttonDraw(self, xSpace :int, ySpace :int, buttonX:int, buttonY:int):
    start.isClicked()
    
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
