import pygame
import sqlite3
from loginScreenScript import textDraw #imports a function that displays text on screen when called

userFile = sqlite3.connect("user.db")

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
        self.height = image.get_height() #gets the width and height to be used for scale
        self.width = image.get_width()
        self.scale = scale
        self.image = pygame.transform.scale(image, (int(self.width*scale),int(self.height*scale))) #scales the image's height and width based on the scale input by the user
        self.clicked = False
        self.topleft = None
        self.rect = self.image.get_rect()
        self.action = None
        self.menu = False

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
            if not pressed:
                self.clicked = False #if not then self.clicked and self.action are set to false
            return self.action #returns self.action

        
    def onClick(self):
        
        """
        this will open up to the secondary menu and load the buttons that go on that screen

        Args:
            None
        Returns:
            None
        """
        self.menu = not self.menu
    def getHeight(self):
        """
        this will return the height of the button
        
        Args:
            None
        Returns:
            int - int value of the height of the button
        """
        
        return self.height
    
    def getWidth(self):
        """
        this will return the width of the button
        Args:
            None
        Returns:
            int - int of the width of the button
        """

        return self.width

class Levelselect(Button):

    def __init__(self):
        """
        Constructor for the LevelSelect subclass of button

        Args:
            None
        Returns:
            None
        """
        levelSelectImg = pygame.image.load("levelSelect.png").convert_alpha()
        super().__init__(levelSelectImg, 1) #calls the init of button and takes it argumetns
        self.opened : bool = False
    


    def menuDraw(self):
        """
        this is what will open the secondary menu and let i stay on screen
        Args:
            None
        Returns:
            None
        """
        if self.menu == True:
            secondaryButton = [vsButton, practiseButton]
            secMenu = SecondaryMenu(secondaryButton)
            secMenu.menuDraw()
            secMenu.buttonDraw (200,0,700,10)
            secMenu.isClicked()

class GameHelp(Button):

    def __init__(self):
        """
        Constructor for the GameHelp subclass of button

        Args:
            None
        Returns:
            None
        """
        gameHelpImg = pygame.image.load("gameHelp.png").convert_alpha()
        super().__init__(gameHelpImg,1) #uses the superclass init

            
    def menuDraw(self):
        """
        this is what will open the secondary menu for the game help button
        Args:
            None
        Returns:
            None
            
        """
        if self.menu == True:
            secMenu = SecondaryMenu(gamehelpmen) # initalises
            secMenu.menuDraw()
            textDraw("1. No matter if anything is potted on break, its still an open table on the next turn,", ruleFont,blackText,700,20)
            textDraw("2. If the cue ball hits nothing or the other players colour, they get 2 shots ball in hand behind the starting line,", ruleFont,blackText,700,35)
            textDraw("3. If you pot the other players colour 2 shots ball in hand, pot white and 2 shots ball in hand to other player, pot black the game's over,", ruleFont,blackText,700,50)
            textDraw("4. If you have 2 shots, on your first shot you can pot any colour ball and it is fine. pots carry over like normal", ruleFont,blackText,700,65)
            textDraw("5. If you are in a situation where you're on black and the other player fouls (ball in hand 2 shots) you only get one shot", ruleFont,blackText,700,80)
            
class Settings(Button):
    def __init__(self):
        """
        constructor for the Settings subclass of button

        Args:
            None
        Returns:
            None
        """
        settingsImg = pygame.image.load("settings.png").convert_alpha()
        super().__init__(settingsImg,1) #uses the superclass init to set the image and scale
        

    
    def menuDraw(self):
        """
        this will open the secondary menu and display the options to pick from in settings
        Args:
            None
        Returns:
            None

        """
        if self.menu == True:
            secondaryButton = []
            secMenu = SecondaryMenu(secondaryButton)
            secMenu.menuDraw()
            textDraw("difficulty:", normalFont,blackText, 750,30 )
            easyDiff.draw()
            midDiff.draw()
            hardDiff.draw()
            textDraw("easy", normalFont, blackText, 750,90)
            textDraw("medium", normalFont, blackText, 850,90)
            textDraw("hard", normalFont, blackText, 950,90)

class Accessibility(Button):
    def __init__(self):
        """
        Constructor for the Accessibility subclass of button

        Args:
            None
        Returns:
            None
        """
        accessibilityImg = pygame.image.load("Accessibility.png").convert_alpha()
        super().__init__(accessibilityImg,1)
    def menuDraw(self):
        """
        This will be used to draw the menu and the text displayed on the page
        Args:
            None
        Return:
            None
        """
        if self.menu:
            secondaryButton = []
            secMenu = SecondaryMenu(secondaryButton)
            secMenu.menuDraw()
            HiConOn.draw()
            HiConOff.draw()
            textDraw("High contrast mode: ", normalFont,blackText,750,30)
            textDraw("On",normalFont,blackText,750,120)
            textDraw("Off",normalFont,blackText,850,120)

class AccountStats(Button):
    def __init__(self):
        """
        Constructor for the AccountStats subclass of button

        Args:
            None
        Returns:
            None
        """
        accountStatImg = pygame.image.load("accountStats.png").convert_alpha()
        super().__init__(accountStatImg,1)
        self.username = "username"

    def getData(self):
        """
        A method to find and return the data linked to to logged in username playing the game

        Args:
            None
        Returns
            userData.execute (list): Returns a list of all the data in the same row as the username being searched for
        """
        userData = userFile.cursor()
        return userData.execute("SELECT * FROM users WHERE username = ?", (self.username,),).fetchone() # takes all the data from the line where the usernames match
    def printData(self):
        """
        A method to print the Data fetched by getData method

        Args:
            None
        Returns:
            None
        """

        print(self.getData())

    def menuDraw(self):
        """
        This is a method to draw the menu, text to be displayed and the data fetched that links to the account

        Args:
            None
        Returns:
            None

        """
        if self.menu:
            secondaryButton = []
            secMenu = SecondaryMenu(secondaryButton) #initialises as an object
            secMenu.menuDraw()
            self.dataList = self.getData()
            textDraw("         Win         |        loss         |       games         ",normalFont,blackText,700,30) # what displays on screen when the menu opens
            textDraw(f"         {self.dataList[1]}                  {self.dataList[2]         }                  {self.dataList[3]}         ",normalFont,blackText,700,70)
            
class Vsbutton(Button):
    def __init__(self):
        """
        Constructor for the Vsbutton subclass of button

        Args:
            None
        Returns:
            None
        """
        vsImg = pygame.image.load("vsButton.png").convert_alpha()
        super().__init__(vsImg,1)
        self.opened = False
        self.newDisplay = False
        
    def onClick(self):
        """
        this will allow the secondary menu class to open the vs screen until either the back button on screen or escape is pressed
        
        Args:
            None
        Returns:
            None
        """
        self.opened = not self.opened
        if self.opened:
            self.newDisplay = True
            
            
    def displayDraw(self):
        """
        This will draw the vs screen on the screen. Depending on if high contrast is needed the colour palet swaps
        
        Args:
            None
        Returns:
            None 
        """
        if self.newDisplay:
            if HiConOff.action:
                pygame.draw.rect(screen,(255,255,255),blankRect)#displays the placeholder screen
                textDraw("taking you to a vs game", normalFont,blackText,10,10)
                pygame.draw.rect(screen,(0,0,139),backRect)
                textDraw("back to menu",normalFont,blackText,800,100)
            else:
                pygame.draw.rect(screen,(0,0,0),blankRect)#displays the placeholder screen but with the high contrast colours
                textDraw("taking you to a vs game", normalFont,(255,255,0),10,10)
                pygame.draw.rect(screen,(0,0,139),backRect)
                textDraw("back to menu",normalFont,blackText,800,100)

class Practise(Button):
    def __init__(self):
        """
        Constructor for the Practise subclass of button

        Args:
            None
        Returns:
            None
        """
        practiseImg = pygame.image.load("practiseButton.png").convert_alpha()
        super().__init__(practiseImg,1)
        self.opened = False
        self.newDisplay = False
    
    def onClick(self):
        """
        this will allow the secondary menu class to open the vs screen until either the back button on screen or escape is pressed
        
        Args:
            None
        Returns:
            None
        """
        self.opened = not self.opened
        if self.opened:
            self.newDisplay = True
            
    def displayDraw(self):
        """
        This will draw the vs screen on the screen. Depending on if high contrast is needed the colour palet swaps
        
        Args:
            None
        Returns:
            None 
        """
        if self.newDisplay:
            if HiConOff.action:
                pygame.draw.rect(screen,(255,255,255),blankRect)#Displays the placeholder screens
                textDraw("taking you to a practise game", normalFont,blackText,10,10)
                pygame.draw.rect(screen,(0,0,139),backRect)
                textDraw("back to menu",normalFont,blackText,800,100)
            else:
                pygame.draw.rect(screen,(0,0,0),blankRect)#displays the placeholder screen but with the high contrast colours
                textDraw("taking you to a practise game", normalFont,(255,255,0),10,10)
                pygame.draw.rect(screen,(0,0,139),backRect)
                textDraw("back to menu",normalFont,blackText,800,100)

class difficultyButton(Button):
    def __init__(self, x: int, y: int,name:str):
        """
        Constructor for the difficultyButton subclass of button

        Args:
            x - The x coordinate of the top left corner of the button
            y - The y coordinate of the top left corner of the button
            name - A string to identify what button is pressed if needed
        Returns:
            None
        """
        self.clickedImg = pygame.image.load("difficultyclicked.png").convert_alpha() # loads the images
        self.notclickedImg = pygame.image.load("difficultynot.png").convert_alpha()
        self.image = self.notclickedImg
        super().__init__(self.image,1) #uses Button Class init
        self.action = False
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.name = name

    def draw(self):
        """
        This method will draw an image on the screen where the button is and change when the button has been selected
        Args:
            None
        Return:
            None

        """
        self.rect.topleft = (self.x, self.y)
        if self.action == True: # depending if the button has been clicked it will change image
            screen.blit(self.clickedImg,self.rect.topleft)
        elif self.action == False:
            screen.blit(self.notclickedImg,self.rect.topleft)

    def select(self,event,group: list):
        """
        Makes it so the buttons are mutually exclusive of one another/when one is clicked the rest turn off
        Args:
            event: a pygame event
            group: a list of buttons that can be iterated through to change their self.action to false
        Returns:
            None
        """
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                for button in group:
                    button.action = False
                self.action = True

    def getDifficulty(self,group: list):
        """
        Finds and returns the difficulty of the button that is selected what then function is called

        Args:
            group: list of buttons that can be checked

        Returns:
            Str for the corresponding difficulty
        """

        for button in group:
            if button.action ==True:
                return self.name

class StartMenu:
    """
    class for the main menu

    """

    def __init__(self,x: int, y: int, width: int, length: int,buttons):
        """
        initialises a menu

        Args:
            x(int): an int for the x coordinate of the top left corner of the menu
            y(int): an int for the y coordinate of the top left corner of the menu
            width(int): an int for the width of the menu
            length(int): an int for the length of the menu
            buttons (list): a list of all the buttons to be displayed on the menu

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
        A method that draws the menu on the screen

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
        this will take the buttons in the list and display them on the menu adjusting their x and y for the space the user wanted inbetween
        
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
            height = button.getHeight()
            width = button.getWidth()
            if xSpace == 0:
                buttonY = buttonY + ySpace + height #if the X space is 0 the buttons are just moving verically so only the y changes
                buttonX = buttonX
            elif ySpace == 0:
                buttonY = buttonY
                buttonX = buttonX + xSpace + width
            
            else :
                buttonX = buttonX + xSpace + width # if the x space isnt 0 than the buttons aren't only veriticle so the x changes (before with this logic the x distance would always change)
                buttonY = buttonY + ySpace + height #if the X space is 0 the buttons are just moving verically so only the y changes
            
        
        self.isClicked()
            
        
    def isClicked(self):
        """
        detects if the button is clicked

        Args:
            None
        Returns: 
            None

        """
        for button in self.buttons:
            
            pos = pygame.mouse.get_pos()
            pressed = pygame.mouse.get_pressed()[0] #checks the mouse pos and if left click was pressed
            if button.rect.collidepoint(pos) and pressed:
                button.onClick()
    
    def eventHandle(self, event):
        """
        A method to handle events and activate buttons inside the event loop

        Args:
            event(pygame event): the current pygame event being processed
        Returns:
            None
        
        """
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            for button in self.buttons:
                if button.rect.collidepoint(event.pos):
                    for other in self.buttons:
                        if other is not button:
                            other.menu = False
                    button.onClick()

class SecondaryMenu(StartMenu):

    def __init__(self, buttons: list):
            """
            Constructor for the SecondaryMenu subclass of StartMenu

            Args:
                None
            Returns:
                None
            """
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
        
    def displayDraw(self):
        """
        this will draw the placeholder screens.
        Args:
            None
        Returns:
            None
        
        """
        for button in self.buttons:
            button.onClick()
            
    def isClicked(self):
        """
        detects if a button in the button list set in the constructor (inherited) is clicked

        Args:
            None
        Returns: 
            None

        """
        for button in self.buttons:
            
            pos = pygame.mouse.get_pos()
            pressed = pygame.mouse.get_pressed()[0] #checks the mouse pos and if left click was pressed
            if button.rect.collidepoint(pos) and pressed:
                button.onClick()
                button.displayDraw()
        
def resetMenu():
    """
    this function will serve as a way to get back to the main menu from the placeholder screen in the level select secondary menu

    Args:
        None
    Returns:
        None
    """
    vsButton.opened = False
    vsButton.newDisplay = False
    practiseButton.opened = False
    practiseButton.newDisplay = False
    levelButton.menu = False




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
ruleFont: pygame.font.Font = pygame.font.SysFont("arial", 10)
vsPlaceholder: bool = False
practisePlaceholder:bool = False
secondMenuCol = (173,216,230)
blackText = (0,0,0)
backgroundFill = (255,255,255)

#Button variables
levelPressed: bool = False  #i will use these values in the event loop for the pop out menus
helpPressed: bool = False
settingsPressed: bool = False
accessPressed: bool = False
statsPressed: bool = False
startButton = None





#rectangles
#menuRect = pygame.Rect(300,10,350,1060) #serves as the rectangle where the buttons to the side menu will be
levelSelectRect = pygame.Rect(700,10,400, 400)
gameHelpRect = pygame.Rect(700,30,400,600)
settingsRect = pygame.Rect(700,50,400,600)
accessibilityRect = pygame.Rect(700,70,400,400)
statsRect = pygame.Rect(700, 90, 400,400)
blankRect = pygame.Rect(0,0,1920,1080)
backRect= pygame.Rect(800,100,100,100)

#making the button objects
levelButton = Levelselect()
gameHelpButton = GameHelp()
settingsButton = Settings()
accessButton = Accessibility()
accountStatButton = AccountStats()
vsButton = Vsbutton()
practiseButton = Practise()
easyDiff = difficultyButton(750,50,"easy")
midDiff = difficultyButton(850,50,"mid")
hardDiff = difficultyButton(950,50,"hard")
HiConOn = difficultyButton(750,80,"")
HiConOff = difficultyButton(850,80,"")

#sets default for the buttons
easyDiff.action = True
HiConOff.action = True

#Button groups:
difficultyGroup = [easyDiff,midDiff,hardDiff]
highContrastGroup = [HiConOn,HiConOff]


#button list
buttonList = [levelButton, gameHelpButton, settingsButton, accessButton, accountStatButton]
gamehelpmen = []


start = StartMenu(300,10,350,1060,buttonList) #(self, buttons: list[Button],x: int, y: int, width: int, length: int):

#game loop
while run:
    #colour the screen
    screen.fill(backgroundFill)
    
    start.menuDraw()
    start.buttonDraw(0, 100, 300, 10) #def buttonDraw(self, xSpace :int, ySpace :int, buttonX:int, buttonY:int):
    start.isClicked()
    levelButton.menuDraw()
    vsButton.displayDraw() #displays the placeholder screen when the vsButton is pressed
    practiseButton.displayDraw() # displays the placeholder screnn for practise when the button is pressed
    gameHelpButton.menuDraw() # displays the gamehelp button when it is clicked
    settingsButton.menuDraw() #displays the settings menu when pressed
    accessButton.menuDraw()
    accountStatButton.menuDraw()



    #check if the game is closed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()


        if vsButton.newDisplay or practiseButton.newDisplay:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and blankRect.collidepoint(event.pos): #checks if the box was clicked
                resetMenu()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE: # checks if escape was pressed
                resetMenu()
            continue
        start.eventHandle(event)
        if settingsButton.menu:
            for button in difficultyGroup:
                button.select(event, difficultyGroup) #checks and swaps what button is activated 
        if levelButton.menu:
            SecondaryMenu([vsButton,practiseButton]).eventHandle(event)
        if accessButton.menu:
            SecondaryMenu([]).eventHandle(event)
            for button in highContrastGroup:
                button.select(event,highContrastGroup)#swaps which button is clicked
                if HiConOn.action == True:
                    backgroundFill = (0,0,0)
                if HiConOff.action == True:
                    backgroundFill = (255,255,255)
        if accountStatButton.menu:
            SecondaryMenu([]).eventHandle(event)






    #sets fps and makes sure screen is updated
    pygame.display.update()
    clock.tick(60) #60 fps
