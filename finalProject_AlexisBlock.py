"""
Chasing the Weekend Game
ATLS 1300/5650
Author: Alexis Block (Harris)

Description: Welcome to Chasing the Weekend! Help Alexis make it to the weekend by avoiding obstacles like dogs, textbooks, footballs and professors around CU's campus!

To begin the game: Simply press the run button

Game play instructions (also in instructions splash screen): Help Alexis make it to the weekend by avoiding obstacles around CU's campus! Use the spacebars to jump
over obstacles like abandonded textbooks, dogs, and professors. Use the down arrow to duck under stray footballs thrown by other students!
Beware! Alexis only has 3 lives to make it to the weekend! Each time Alexis hits an object, she will lose a life. The longer you make it, the higher your score will be! Make it to Saturday to win!

Intended users and support for intended users: Intended users include other students who also have to take on work while being a full time student in order to support themselves financially. This game is intended to help represent how stressful that experience can be, and be an ode to all the hustlers out there. As a grad student who is taking 4 classes because my scholarship only lasts a year and working a 20 hour per week job to support myself, I know firsthand how much can be on our plates at any one time.
In addition, there are some accessibility accomodations for users who need them:
All text is rendered using pygame's text features (rather than images) which enables screen readers to read the text. This is useful for users who might need accomodations for reading, including those with dyslexia.
Further, gameplay is controlled by just two buttons and a clicking mouse/mousepad. This simplified gameplay allows users with conditions that cause motor control impairement to still interact with a game. Further, though users are meant to duck under footballs, I have made them just low enough to also jump over them. This means that users can play the game with just the spacebar if needed. This enables users with conditions that effect motor control to still interact with the game (rather than a more complicated interface that is not motor control friendly)
Finally, the visuals used are made using coolors color palettes, an online interface that creates color palettes that are friendly to color blind eyes, and high contrast colors to hopefully aid users with visual impairment in enjoying the game.

Note: This game is meant to be played on a 1300 by 750 (standard computer screen) window. If the window is smaller than that, the game components will not be sized correctly!

"""
# from FILE import * # blanket import
import pygame, random
import pygame.mixer as mixer
pygame.init()


# create a window
w = 1300
h = 750
win = pygame.display.set_mode((w,h)) # define window variable

#======================== Variables & functions ===================================================
WHITE = (255,255,255) # some handy RGB values
BLACK = (0,0,0)

#background music (music credit: https://www.playonloop.com/2010-music-loops/dark-wings/)
soundfile = "backgroundMusicLoop.wav" 

#sound that plays when user jumps (sound credit: https://www.youtube.com/watch?v=q7Ar0otY1RQ)
jumpSound = pygame.mixer.Sound("jump.wav")

#sound that plays when user hits objects (sound credit: from OOP repository-- edited to sound higher pitch by myself)
collisionSound = pygame.mixer.Sound("oof.wav")

#sound that plays when character ducks (sound credit: Pixabay https://pixabay.com/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=music&amp;utm_content=6316)
duckSound = pygame.mixer.Sound("whoosh1.wav")
 
#Sound Effect from Pixabay https://pixabay.com/sound-effects/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=music&amp;utm_content=38511
winSound = pygame.mixer.Sound("youWin.wav")

#Sound Effect from Pixabay "https://pixabay.com/sound-effects/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=music&amp;utm_content=6993
loseSound = pygame.mixer.Sound("gameOver.wav")

#font size and game font to use for all text in the game
fontSize = 40
gameFont = pygame.font.Font("Snicker.ttf", fontSize, bold = True)

#font size and instructions font to use for instructions
instructionsFontSize = 20
instructionsFont = pygame.font.Font("joystix.ttf", instructionsFontSize)

gameOverFontSize = 100
gameOverFont = pygame.font.Font("joystix.ttf", gameOverFontSize)

#backgroundImage (Built CU buildings and some other elements of background myself, partially adapted from: https://www.freepik.com/premium-vector/pixel-art-game-background-grass-sky-clouds_9047947.htm?epik=dj0yJnU9bWZOekEzY2trOEpzSndVN2FxQVNRX1BSVzdzZlFqNXQmcD0wJm49R2Y2U3FsVUExa1hvZlBtWjRQZnZ2ZyZ0PUFBQUFBR09ZLW1z)
backgroundImage = pygame.image.load("backgroundNew.png")
background = pygame.transform.scale(backgroundImage, (w,h))

#startScreen image
startScreenImage = pygame.image.load("startScreen.png")
startScreen = pygame.transform.scale(startScreenImage, (w,h))

#load all user images and scale for gameplay
userImage1 = pygame.image.load("userRun1.png")
user1 = pygame.transform.scale(userImage1, (89, 129))
userImage2 = pygame.image.load("userRun2.png")
user2 = pygame.transform.scale(userImage2, (84, 120))
userImage3 = pygame.image.load("userRun3.png")
user3 = pygame.transform.scale(userImage3, (81,126))
#add user images into a list to cycle through in drawing them to screen (repeat some to keep them on screen longer)
allUserImages = [user1, user1, user2, user2, user2, user3, user3]

#load duck image and scale to show when user presses down arrow
playerDuckImage = pygame.image.load("playerDuck.png")
playerDuck = pygame.transform.scale(playerDuckImage, (77,91))

#load all professor (variation 1) images and scale for gameplay
professorImage1 = pygame.image.load("professorRun1.png")
professor1_1 = pygame.transform.scale(professorImage1, (65, 125))
professorImage2 = pygame.image.load("professorRun2.png")
professor1_2 = pygame.transform.scale(professorImage2, (65, 116))
professorImage3 = pygame.image.load("professorRun3.png")
professor1_3 = pygame.transform.scale(professorImage3, (57, 121))
#similar to user, add images into list to cycle through in drawing them to screen
allProfessorImages = [professor1_1, professor1_1, professor1_2, professor1_3, professor1_3, professor1_2]

#repeat process with professor (variation 2) images and scale for gameplay
professor2Image1 = pygame.image.load("professor2Run1.png")
professor2_1 = pygame.transform.scale(professor2Image1, (85, 125))
professor2Image2 = pygame.image.load("professor2Run2.png")
professor2_2 = pygame.transform.scale(professor2Image2, (81, 117))
professor2Image3 = pygame.image.load("professor2Run3.png")
professor2_3 = pygame.transform.scale(professor2Image3, (73,121))
allProfessor2Images = [professor2_1, professor2_1, professor2_2, professor2_3, professor2_3, professor2_2]

#load image for winning character jumping
winningJumpImage = pygame.image.load("happyJump.png")
winningJump = pygame.transform.scale(winningJumpImage, (122,177))
#load the images into a list to be able to reuse movingCharacter class for winning animation
allWinningJumpImages = [winningJump, winningJump, winningJump, winningJump, winningJump, winningJump, winningJump]

#load heart image for lives (partially adapted from these images: https://www.pngwing.com/en/search?q=8+Bit+Heart)
heartImage = pygame.image.load("liveHeart.png")
heart = pygame.transform.scale(heartImage, (77,66))

#load book image for textbook obstacle (book image partially adapted from: https://www.shutterstock.com/image-vector/stack-books-pixel-art-old-school-1362594311)
bookImage = pygame.image.load("book.png")
bookCartoon = pygame.transform.scale(bookImage, (67,56))

#load football image for football obstacle
footballImage = pygame.image.load("football.png")
footballObject = pygame.transform.scale(footballImage, (35, 26))

#load dog image for dog obstacle (dog 8-bit drawing from: https://stock.adobe.com/images/pixel-art-dog-character-isolated-on-white-background-domesitc-animal-icon-cute-8-bit-logo-retro-vintage-80s-90s-16-bit-slot-machine-video-game-gra)
dogImage = pygame.image.load("dog.png")
dogObject = pygame.transform.scale(dogImage, (88,87))

#load hover image to change button image if user hovers over it
hoveringImage = pygame.image.load("scoreHover.png")
hovering = pygame.transform.scale(hoveringImage, (300,65))

#load score background image that will serve as background for text in game
scoreImage = pygame.image.load("score.png")
scoreBackgroundImage = pygame.transform.scale(scoreImage, (300,65))

#load arrow images for instructions pages
arrowRightImage = pygame.image.load("arrow.png")
arrowRight = pygame.transform.scale(arrowRightImage, (45,25))
arrowLeftImage = pygame.image.load("arrow2.png")
arrowLeft = pygame.transform.scale(arrowLeftImage, (45,25))

#load startScreen image for background of start screen
startScreenImage = pygame.image.load("startScreen.png")
startScreen = pygame.transform.scale(startScreenImage, (w,h))

#load instruction image for background of instructions pages
instructionsBackgroundImage = pygame.image.load("instructionsBackground.png")
instructionsBackground = pygame.transform.scale(instructionsBackgroundImage, (w,h))

#load losing background image for losing screen
loseBackgroundImage = pygame.image.load("gameOver.png")
loseBackground = pygame.transform.scale(loseBackgroundImage, (w,h))

#class for any moving characters (the user, professor variation 1 and professor variation 2)
class movingCharacter:
    '''load moving character with x + y coordinates, step size for movement, and images that will be used for cycle'''
    def __init__(self, x, y, playerCycle = allUserImages, step=12):
        self.x = x
        self.y = y
        self.playerCycle = playerCycle
        #maximum jump velocity
        self.jumpHeight = 28
        self.stepIndex = 0
        self.step = step
        #useful image width and height values for placing images on the screen
        self.imageWidth = (self.playerCycle[self.stepIndex]).get_width()
        self.imageHeight = (self.playerCycle[self.stepIndex]).get_height()
        self.box = pygame.Rect(self.x, self.y, self.imageWidth, self.imageHeight)
        #set default values for player actions of running, jumping, and ducking
        self.playerRunning = True
        self.playerJump = False
        self.playerDuck = False
        self.draw = True

    def characterAnimation(self):
        '''method that looks for if the object is drawn and running and cycles through the images one by one to create frame by frame animation'''
        if self.draw:
            if self.playerRunning:
                self.box = win.blit(self.playerCycle[self.stepIndex], (self.x,self.y))
                self.stepIndex += 1
                if self.stepIndex >= 6:
                    self.stepIndex = 0

    def keyCheck(self,event):
        '''method that passes in python pressed down events and if it is the spacebar, it plays the jump sound
        and sets playerJump to True and if it is the down arrow, it plays the duck sound
        and sets player duck to True (and reverses those actions if key is unpressed)'''
        if event.type == pygame.KEYDOWN:
            if self.playerJump == False and event.key == pygame.K_SPACE:
                pygame.mixer.Sound.play(jumpSound)
                self.playerJump = True
            if self.playerDuck == False and event.key == pygame.K_DOWN:
                pygame.mixer.Sound.play(duckSound)
                self.playerDuck = True
                self.playerRunning = False
                
        if event.type == pygame.KEYUP:
            if self.playerDuck == True and event.key == pygame.K_DOWN:
                self.playerRunning = True
                self.playerDuck = False
                self.duckIndex = 0      
    
    def jumping(self):
        '''method that runs if playerJump is set to True in the keyCheck method to make the player jump up in a parabolic pattern'''
        #if playerJump is True
        if self.playerJump:
            #subtract the velocity from the character's y coordinate, making the character move up
            self.y -= self.jumpHeight
            #subtract 2 from the velocity so it is moving up less and less (slowing down), before stopping and then reversing direction to actually add 2 each time
            self.jumpHeight -= 2
            #if the velocity is max velocity (28)
            if self.jumpHeight < -28:
                #set playerJump to false and reset original velocity
                self.playerJump = False
                self.jumpHeight = 28
    
    def duck(self, image = playerDuck): 
        '''method that blits (draws) the duck image onto the screen if playerDuck is set to true by keyCheck method'''
        if self.playerDuck == True:
            self.box = win.blit(image, (self.x,self.y+50))
    
    def move(self):
        '''Method that moves the enemy characters from right to left according to the step attribute'''
        self.x -= self.step
    
    def offscreen(self):
        '''Method that moves the player character offscreen from left to right when game is one'''
        self.step = 10
        self.x += self.step

    def startMovement(self):
        '''Method that moves the character onto the screen and stops it in the exact middle for the start screen'''
        self.x += self.step
        if self.x >= w/2-self.imageWidth/2:
            self.x = w/2-self.imageWidth/2
    
    def collision(self, obj):
        '''Method that passes in an object and if that object's box collides with the player's box, then it sets that object's draw attribute to False and plays the collision sound'''
        if self.box.colliderect(obj.box):
            obj.draw = False
            pygame.mixer.Sound.play(collisionSound)
        

#reusable class for football and books and dogs
class staticObstacles:
    def __init__(self, startPos=(w+100,h-160), step=10, image = bookCartoon):
        '''Default staticObstacle object is the text book with the following set attributes'''
        self.x,self.y=startPos
        self.image = image
        self.imageWidth = image.get_width()
        self.imageHeight = image.get_height()
        self.box=pygame.Rect(startPos[0],startPos[1],self.imageWidth, self.imageHeight)
        self.step = step 
        self.draw = True
        
    def show(self):
        '''Method that draws the object onto the screen using its passed in image attribute'''
        if self.draw == True:
            self.box = win.blit(self.image, (self.x,self.y))

    def move(self):
        ''' method that moves the object from right side of screen to left'''
        self.x -= self.step
        self.show()

#class for all stats that have an image associated with them (including button backgrounds, day backgrounds, and hearts)
class Stats:
    def __init__(self,x,y, image = heart, hoverImage=hovering):
        '''Default Stats object is the heart images with the following attributes'''
        self.x = x
        self.y = y
        self.image = image
        self.imageWidth = (self.image).get_width()
        self.imageHeight = (self.image).get_height()
        self.box=pygame.Rect(self.x,self.y,self.imageWidth, self.imageHeight)
        self.hoverImage = hoverImage
        #create variable that holds whether or not the stat is clicked for button functionality
        self.clicked = False
        self.draw = True

    def show(self):
        '''Method that draws the object onto the screen using it's passed in image attribute'''
        if self.draw == True:
            self.box = win.blit(self.image, (self.x,self.y))

    def hover(self):
        '''Method that creates hover effect for buttons.
        It takes in mouse's movement and cursor's coordinates. If the coordinates are over the Stats object box,
        then it will change the background image to the hover image'''
        x,y = pygame.mouse.get_pos()
        if self.box.collidepoint(x, y):
            self.box = win.blit(self.hoverImage, (self.x,self.y))

    def click(self, event):
        '''Method that allows for button clicking functionality. It takes in pygame events. If the mouse button is clicked,
        then it records the cursor's position. If the mouse was clicked with the cursor colliding with the object's box,
        then it sets the attribute clicked to True'''
        if event.type == pygame.MOUSEBUTTONDOWN:
            x,y = pygame.mouse.get_pos()
            if self.box.collidepoint(x,y):
                self.clicked = True

#class that actually draws and updates the score text using time (more time = higher score), borrowed from OOP Snippet repository
class Scorekeeper:
    def __init__(self, time = 0, countDir = False, text = 0, position = (53,32)):
        self.totalTime = time
        self.countDir = countDir # if False, then clock counts up
        self.setToZero(time) # resets clock based on self.countDown

        # text settings
        self.fontSize= fontSize
        self.font = gameFont
        self.text = text # string to print
        self.position = position

        self.draw = True
        self.drawBackground = True
    
    def countUp(self):
        '''calculates time passed and returns time in
        seconds (int).'''
        self.spawnTime = ((pygame.time.get_ticks()-self.start_ticks))
        seconds=(pygame.time.get_ticks()-self.start_ticks)/100
        self.currTime = int(seconds)
        return self.currTime

    def setToZero(self,time=60): 
      '''Gets computer clock time at method call,
      and resets Timer values (self.currTime).'''
      self.start_ticks=pygame.time.get_ticks()
      
      if self.countDir:
          self.currTime = time
      else:
          self.currTime = 0
        
    def showTime(self):
        '''Uses pygame font object to draw time on screen.
        Argument - Surface (pygame Surface) to add text to.'''
        self.text = str(self.currTime)
        if self.draw == True:
            self.box = win.blit(self.font.render("Score: " + self.text, True, 
                            ("#685543")), self.position)

#reusable class for all text that appears in the game
class Text:
    def __init__(self, position = (540,32), font = gameFont, text = "MONDAY", color = "#CF995F"):
        '''Default text object is the Monday day of the week display that is orange'''
        self.font = font
        self.text = text
        self.draw = True
        self.position = position
        self.color = color
        
    def show(self):
        '''Method that draws the text onto the screen and then moves it directly to the center of the screen using its box width'''
        if self.draw == True:
            self.box = win.blit(self.font.render(self.text, True, 
                                (self.color)), self.position)
            self.textWidth = self.box.w
            self.position = ((w/2 - (self.textWidth/2)), h-350)
            
    #changes day depending on current "score" (time)
    def changeDay(self, obj):
        '''Method that changes the day depending on the current "score" (based on time passed defined above in Scorekeeper class.
        It passes in the object (always Scorekeeper) uses Scorekeeper object's attribute currTime to change day of the week text accordingly'''
        if 100 <= obj.currTime < 200:
            self.text = "TUESDAY"
            
        elif 200 <= obj.currTime< 300:
            self.text = "WEDNESDAY"
            
        elif 300 <= obj.currTime< 400: 
            self.text = "THURSDAY"
            
        elif 400 <= obj.currTime< 500:
            self.text = "FRIDAY"
        
        elif 500 <= obj.currTime< 600:
            self.text = "SATURDAY"

class Manager:
    def __init__(self):
        #set a hit counter to keep track of lives lost
        self.hitCounter = 0
        
        #set clock used for animation control
        self.clock = pygame.time.Clock() 

        #reusable retry button using Stats class to reuse for win or loss screen
        self.retryButtonText = Text(text = "RETRY")
        self.retryButtonBackgroundWidth = scoreBackgroundImage.get_width()
        self.retryButtonBackground = Stats(w/2-self.retryButtonBackgroundWidth/2, y = h-425, image = scoreBackgroundImage)

    def livesSubtract(self, lifeObject1, lifeObject2, lifeObject3):
        '''Method that hides the heart images based on the hitCounter atttribute value'''
        if self.hitCounter == 1:
            lifeObject3.draw = False
        if self.hitCounter == 2:
            lifeObject2.draw = False
        if self.hitCounter == 3:
            lifeObject1.draw = False

    def start(self):
        '''Method for the start of the game that creates the start screen'''
        
        #load the music and play it forever (loop it)
        mixer.music.load(soundfile)
        mixer.music.play(-1)
        
        #instantiate button object for start
        startButtonText = Text(text = "START")
        startButtonBackgroundWidth = scoreBackgroundImage.get_width()
        startButtonBackground = Stats(w/2-startButtonBackgroundWidth/2, y = h-360, image = scoreBackgroundImage)

        #instantiate playerCharacter to move across startScreen
        startPlayer = movingCharacter(-100,h-230)

        #set while loop boolean to True
        startPage = True
        
        #while boolean is True
        while startPage:

            #draw the start screen background
            win.blit(startScreen, (0,0))

            #show the start button
            startButtonBackground.show()

            #call the hover method which changes the button background is mouse hovers over it
            startButtonBackground.hover()
            
            #show the start button text
            startButtonText.show()

            #call the characterAnimation and startMovement methods from movingCharacter class to move character across screen in animation
            startPlayer.characterAnimation()
            startPlayer.startMovement()

            #event listener for loop
            for event in pygame.event.get():
                #if user hits quit...
                if event.type == pygame.QUIT:
                    #quit pygame
                    pygame.quit()
                #call click method which checks to see if the start button is clicked
                startButtonBackground.click(event)

                #if it is clicked
                if startButtonBackground.clicked == True:
                    #set the while loop to false
                    startPage = False
                    #and call the instructions function defined below
                    self.instructions()

            #pygame animation control
            pygame.display.update()
            self.clock.tick(30) # framerate in fps

    def instructions(self):
        '''Method for the instructions of the game that includes page one and page two of instructions'''

        #top text "Welcome to Chasing the Weekend" that remains across the top on page one and page two of instructions
        instructionsTextTop = Text(text = "Welcome to Chasing the Weekend", position = (w/2, 0))

        #define boolean variable that runs while loop in this method
        instructionsPages = True

        #define boolean variables that control display of page 1 or page 2 of instructions (if True, display that page)
        instructionsPage1 = True
        instructionsPage2 = False

        #line by line instantiation of Text objects (could not find way to create line breaks in pygame unfortunately) for instruction text in white instructions font

        #this section contains the text for page 1 of instructions
        instructionsTextLine1 = Text(font = instructionsFont, text = "Help Alexis make it to the weekend by avoiding", color = "white")
        instructionsTextLine2 = Text(font = instructionsFont, text = "obstacles around CU's campus! ", color = "white")
        instructionsTextLine3 = Text (font = instructionsFont, text = "Use the spacebar to jump over obstacles like", color = "white")
        instructionsTextLine4 = Text (font = instructionsFont, text = "Abandoned textbooks      Dogs         and professors", color = "white")
        instructionsTextLine5 = Text (font = instructionsFont, text = "And use the down arrow to duck under stray", color = "white")
        instructionsTextLine6 = Text (font = instructionsFont, text = "footballs thrown by other students!", color = "white")

        #this block contains text for page 2 of instructions
        instructionsTextLine7 = Text (font = instructionsFont, text = "Beware! Alexis only has 3 lives to make it to the weekend.", color = "white")
        instructionsTextLine8 = Text (font = instructionsFont, text = "Each time Alexis hits an object, she will lose a life.", color = "white")
        instructionsTextLine9 = Text (font = instructionsFont, text = "The longer you make it, the higher your score will be.", color = "white")
        instructionsTextLine10 = Text (font = instructionsFont, text = "Make it to Saturday to win!", color = "white")
        instructionsTextLine11 = Text (font = instructionsFont, text = "Ready to play?", color = "white")

        #next button Text/Stats object for page 1 of instructions
        nextButtonText = Text(text = "NEXT")
        nextButtonBackgroundWidth = scoreBackgroundImage.get_width()
        nextButtonBackground = Stats(w/2-nextButtonBackgroundWidth/2+20, y = h-125, image = scoreBackgroundImage)

        #day example object for instructions visual on page 2
        dayExampleText = Text(text = "SATURDAY")
        dayTextBackgroundWidth = scoreBackgroundImage.get_width()
        dayBackground = Stats(x = (w/2-dayTextBackgroundWidth/2), y = h-390, image = scoreBackgroundImage)

        #start button Text/Stats object for page 2 of instructions
        startGameButtonText = Text(text = "LET'S GO!")
        startGameButtonBackgroundWidth = scoreBackgroundImage.get_width()
        startGameButtonBackground = Stats(w/2-startGameButtonBackgroundWidth/2, y = h-125, image = scoreBackgroundImage)
        
        #while instructionsPages boolean is True, display the instructions pages using the following while loop
        while instructionsPages:
            #draw the instructions background used in page 1 and page 2 of instructions
            win.blit(instructionsBackground, (0,0))

            #Section of code that displays all of page 1 instructions and next button
            if instructionsPage1:
                
                #creates visuals for page 1 of instructions (example user image and example obstacle images so user know what everything looks like beforehand)
                nonMovingPlayer = pygame.transform.scale(userImage1, (61, 88))
                win.blit(nonMovingPlayer, (200, 100))
                nonMovingBook = pygame.transform.scale(bookImage,(67,56))
                win.blit(nonMovingBook, (320,h-400))
                nonMovingDog = pygame.transform.scale(dogImage, (88,87))
                win.blit(nonMovingDog, (w/2-(nonMovingDog.get_width()/2)+20,h-425))
                nonMovingProfessor1 = pygame.transform.scale(professorImage1, (44,85))
                win.blit(nonMovingProfessor1, (w-375,h-425))
                nonMovingProfessor2 = pygame.transform.scale(professor2Image1, (55,81))
                win.blit(nonMovingProfessor2, (w-275,h-425))
                nonMovingFootball = pygame.transform.scale(footballImage, (69,52))
                win.blit(nonMovingFootball, (w/2-nonMovingFootball.get_width()/2+20,h-200))

                #displays all of the text for page 1 in the assigned positions
                instructionsTextTop.show()
                instructionsTextTop.position = ((w/2 - (instructionsTextTop.textWidth/2)), 50)
                instructionsTextLine1.show()
                instructionsTextLine1.position = ((w-1000), h-625)
                instructionsTextLine2.show()
                instructionsTextLine2.position = ((w-1000), h-580)

                pygame.draw.line(win, "white", (150,h-540), (w-150, h-540), width = 3)

                instructionsTextLine3.show()
                instructionsTextLine3.position = ((w/2 - (instructionsTextLine3.textWidth/2)), h-470)

                instructionsTextLine4.show()
                instructionsTextLine4.position = ((w/2 - (instructionsTextLine4.textWidth/2)), h-330)

                instructionsTextLine5.show()
                instructionsTextLine5.position = ((w/2 - (instructionsTextLine5.textWidth/2)), h-250)

                instructionsTextLine6.show()
                instructionsTextLine6.position = ((w/2 - (instructionsTextLine6.textWidth/2)), h-225)

                #calls show method to display button background
                nextButtonBackground.show()
                
                #calls hover method to change background image if user hovers over next button
                nextButtonBackground.hover()
                
                #displays next button text in assigned position in middle bottom of screen
                nextButtonText.show()
                nextButtonText.position = ((w/2 - (nextButtonText.textWidth/2)+20), h-120)

                #pygame event listener for loop
                for event in pygame.event.get():
                    #if user hits quit...
                    if event.type == pygame.QUIT:
                        #quit pygame
                        pygame.quit()
                    #call click method that looks for if next button is clicked
                    nextButtonBackground.click(event)
                
                #if next button is clicked...
                if nextButtonBackground.clicked == True:
                    #turn off the instructions for page 1 and turn on the instructions for page 2
                    instructionsPage1 = False
                    instructionsPage2 = True
            
            if instructionsPage2:
                #display reused "Welcome to Chasing the Weekend" text from previous page
                instructionsTextTop.show()
                instructionsTextTop.position = ((w/2 - (instructionsTextTop.textWidth/2)), 50)

                #displays all of the text for page 1 in the assigned positions
                instructionsTextLine7.show()
                instructionsTextLine7.position = ((w/2 - (instructionsTextLine7.textWidth/2)), h-625)
                
                #draws heart visuals for user to know what lives look like
                win.blit(heart, (w/2-(heart.get_width()/2),h-580))
                win.blit(heart, (w/2-(heart.get_width()/2)-80,h-580))
                win.blit(heart, (w/2-(heart.get_width()/2)+80,h-580))

                #more instructions text after hearts
                instructionsTextLine8.show()
                instructionsTextLine8.position = ((w/2 - (instructionsTextLine8.textWidth/2)), h-510)

                instructionsTextLine9.show()
                instructionsTextLine9.position = ((w/2 - (instructionsTextLine9.textWidth/2)), h-480)

                pygame.draw.line(win, "white", (150,h-430), (w-150, h-430), width = 3)

                #displays example of what day text looks like for user
                dayBackground.show()
                dayExampleText.show()
                dayExampleText.position = ((w/2 - (dayExampleText.textWidth/2)), h-380)

                #draws arrows pointing to day example
                win.blit(arrowLeft,(w/2-240, h-370))
                win.blit(arrowRight,(w/2+200, h-370))

                #more instructions text after day example
                instructionsTextLine10.show()
                instructionsTextLine10.position = ((w/2 - (instructionsTextLine10.textWidth/2)), h-300)

                instructionsTextLine11.show()
                instructionsTextLine11.position = ((w/2 - (instructionsTextLine11.textWidth/2)), h-170)
            
                #call show method to display start button background
                startGameButtonBackground.show()

                #call hover method to change start button background if user hovers over button
                startGameButtonBackground.hover()
                
                #show the start button text
                startGameButtonText.show()
                startGameButtonText.position = ((w/2 - (startGameButtonText.textWidth/2)), h-120)

                #pygame event listener for loop
                for event in pygame.event.get():
                    #if user hits quit...
                    if event.type == pygame.QUIT:
                        #quit pygame
                        pygame.quit()
                    
                    #call click method to check if start button is clicked
                    startGameButtonBackground.click(event)
                
                #if start button is clicked...
                if startGameButtonBackground.clicked == True:
                    #turn off the 2nd page of instructions
                    instructionsPage2 = False
                    #and start the game play method defined below
                    self.gameplay()
            
            #pygame animation controls
            pygame.display.update()
            self.clock.tick(30) # framerate in fps (30-60 is typical)       

    def gameplay(self):
        '''Method that actually starts game play where user can begin avoiding obstacles, lives start subtracting and the score starts counting'''
        #while loop boolean variable
        play = True

        #boolean variable that controls if obstacles are being populated or not (True = being populated)
        addingObstacles = True

        #boolean variable that controls if collisions are being counted or not (True = being counted)
        countingCollisions = True

        #set background image
        backgroundStep = 0
        backgroundWidth = w

        #instantiate player object
        player = movingCharacter(50,h-230)

        #instantiate score object and score background
        scoreBackground = Stats(x = 40, y = 25, image = scoreBackgroundImage)
        score = Scorekeeper()

        #instantiate day object and day background
        dayBackground = Stats(x = (w/2-(scoreBackground.imageWidth/2)), y = 25, image = scoreBackgroundImage)
        #instantiate text object for day text
        day = Text()

        #instantiate 3 life object heart images
        life1 = Stats(w-325,25)
        life2 = Stats(w-225,25)
        life3 = Stats(w-125,25)

        #Starting speed of moving screen (sets the screen to move -8 steps in the x direction in the while loop)
        gameSpeed = 10

        #create an empty list for all objects to be appended to. This will be the placeholder list to draw populated objects from
        allObjects = []

        #append one of each object (book, football, dog, professor variation 1, and professor variation 2) into the allObjects list
        for i in range (1):
            allObjects.append(staticObstacles(startPos = ((w+100),(h-160))))
            allObjects.append(staticObstacles(startPos=(w+100,h-250), image = footballObject))
            allObjects.append(staticObstacles(startPos = (w+200, h-190), image = dogObject ))
            allObjects.append(movingCharacter(w+200, h-230, playerCycle = allProfessorImages))
            allObjects.append(movingCharacter(w+200, h-230, playerCycle = allProfessor2Images))

        #create an empty list which will hold all objects that are moving on the game screen
        movingObjects = []

        #variable that will hold time passed to eventually populate objects into movingObjects list
        loop = 0

        #variable that controls the space between objects in movingObjects list
        populationSpace = 70
            
        #while play boolean is set to True...
        while play:

            #add one to the loop variable to serve as a time passed holder
            loop +=1

            #fill in the background with black just in case background image doesn't draw right away
            win.fill(BLACK)

            #draw background
            win.blit(background, (0+backgroundStep, 0))

            #draw second background image to move with original (on the right side of the original)
            win.blit(background, (backgroundWidth+backgroundStep, 0))

            #move the background according to the game speed
            backgroundStep -= gameSpeed

            #if the first background has moved completely off screen
            if backgroundStep <= -w:
                #draw a new one at the right side of the screen
                win.blit(background, (w+backgroundStep,0))
                #set the backgroundStep back to zero to restart process
                backgroundStep = 0

            #show the three hearts
            life1.show()
            life2.show()
            life3.show()

            #start increasing score
            score.countUp()
        
            #cycle through the player images
            player.characterAnimation()

            #show the score and day
            scoreBackground.show()
            dayBackground.show()
            day.show()
            day.position = ((w/2 - (day.textWidth/2)), 32)
            day.changeDay(score)
            score.showTime()
            
            #pygame event listener for loop
            for event in pygame.event.get():
                #if user hits quit...
                if event.type == pygame.QUIT:
                    #quit pygame
                    pygame.quit()
                #call movingCharacter keyCheck method to check if user is pressing the spacebar (jump) or down arrow (duck)
                player.keyCheck(event)
                    
            #run jump and duck methods for the player character
            player.jumping()
            player.duck()             

            #if addingObstacles boolean is set to True...
            if addingObstacles:
                #if the loop number is divisible by the populationSpace number (set originally to 70) with zero remainder -- in other words, every 70 "loops"
                if loop%populationSpace == 0:
                    #create variable newObject that pulls a random choice object from allObjects list
                    newObject = random.choice(allObjects)
                    #add that new object to the movingObjects list to animate/display/move
                    movingObjects.append(newObject)
                    #remove it from the allObjects list so it does not repeat the next time we add an obstacle
                    allObjects.remove(newObject)

            #for all the objects in the movingObjects list...
            for object in movingObjects:
                #call the move method (note that both movingCharacter and staticObstacles objects have the move method so that it doesn't matter what type of object it is)
                object.move()
                #if the object is an object instantiated from the movingCharacter class however...
                if type(object) == movingCharacter:
                    #call the character animation method and increase the step index to create frame by frame running animations for professors
                    object.characterAnimation()
                    if object.stepIndex >= 5:
                        object.stepIndex = 0

                #if countingCollisions boolean is set to True...
                if countingCollisions:
                    #call the movingCharacter collision method to check if player collides with object (if it does, object.draw = False)
                    player.collision(object)
                    if not object.draw: # if draw is False
                        #add one to the hitCounter
                        self.hitCounter += 1

                        #re-add that object back to the original allObjects list to be reused/repopulated again by turning its drawing back on and moving it to the right side of the screen
                        allObjects.append(object)
                        object.draw = True
                        object.x = w+200

                        #then remove that object from the movingObjects list so it's not sitting there invisible and still moving
                        movingObjects.remove(object)
                    
                    #if the object is not collided with, but does go off of the right side of the screen...
                    if object.x<0-object.imageWidth:
                        #re-add that object back to the original allObjects list to be reused/repopulated again, and move it to the right side of the screen
                        allObjects.append(object)
                        object.x = w+200
                        
                        #then remove that object from movingObjects list
                        movingObjects.remove(object)
                
                #GAMEPLAY DIFFICULTY CONDITIONAL STATEMENTS THAT INCREASE CHALLENGE EACH DAY

                #if day is Tuesday
                if day.text == "TUESDAY":
                    #increase the speed of the movement
                    gameSpeed= 13
                    #decrease the space between the populated objects in movingObjects list
                    populationSpace = 50
                    #set step for obstacles so they also move the speed of the game
                    if type(object)==staticObstacles:
                        object.step = gameSpeed
                    else:
                        object.step = gameSpeed+2
                
                #repeat for each day, gradually increasing gameSpeed and decreasing space between populated objects in movingObjects list
                if day.text == "WEDNESDAY":
                    gameSpeed= 16
                    populationSpace = 45
                    if type(object)==staticObstacles:
                        object.step = gameSpeed
                    else:
                        object.step = gameSpeed+2
                
                if day.text == "THURSDAY":
                    gameSpeed= 19
                    populationSpace = 40
                    if type(object)==staticObstacles:
                        object.step = gameSpeed
                    else:
                        object.step = gameSpeed+2

                if day.text == "FRIDAY":
                    gameSpeed= 22
                    populationSpace = 35
                    if type(object)==staticObstacles:
                        object.step = gameSpeed
                    else:
                        object.step = gameSpeed+2

                #if the user reaches Saturday (the weekend! The win!)...
                if day.text == "SATURDAY":
                    #stop counting collisions and adding obstacles
                    countingCollisions = False
                    addingObstacles = False

                    #wait until all the last populated object has moved off the screeen
                    if movingObjects[-1].x <= 0-movingObjects[-1].imageWidth:
                        #call the movingCharacter offscreen method to move the user from left to right until they disappear off screen at a step speed of 8
                        player.step = 8
                        player.offscreen()
                        #gradually fade out the music
                        mixer.music.fadeout(3500)

                        #if the player has moved fully off screen
                        if player.x >= w+player.imageWidth:
                            #turn off play
                            play = False
                            #and start the win method defined below!
                            self.playerWin()

            #remove the heart images if there is a collision
            self.livesSubtract(life1, life2, life3)

            #if the player hits 3 objects and loses all three of their lives (the hitCounter = 3)...
            if self.hitCounter == 3:
                #stop the music
                mixer.music.stop()
                #turn off play
                play = False
                #and start the lose method defined below :(
                self.playerLose()
                
            #pygame animation control
            pygame.display.update()
            self.clock.tick(30) # framerate in fps

    def playerLose(self):
        '''Method that creates the losing screen if the player loses according to outcome from method above'''

        #while loop boolean
        loser = True
        
        #set retry button clicked to False (just in case user has retried multiple times)
        self.retryButtonBackground.clicked = False

        #play the lose sound
        pygame.mixer.Sound.play(loseSound)
        
        #instantiate game over text
        gameOverText = Text(font = gameOverFont, text = "GAME OVER", color = "white")
        gameOverTextSecondLine = Text(font = instructionsFont, text = "Alexis fell behind in her school work", color = "white")
        gameOverTextThirdLine = Text(font = instructionsFont, text = "and will not be able to party this weekend. Sad.", color = "white")
        
        #while boolean loser is True...
        while loser:
            #draw the loser background
            win.blit(loseBackground, (0,0))

            #show display the game over text
            gameOverText.show()
            gameOverText.position = ((w/2 - (gameOverText.textWidth/2)), 50)

            gameOverTextSecondLine.show()
            gameOverTextSecondLine.position = ((w/2 - (gameOverTextSecondLine.textWidth/2)), 190)

            gameOverTextThirdLine.show()
            gameOverTextThirdLine.position = ((w/2 - (gameOverTextThirdLine.textWidth/2)), 230)

            #display the retry button background
            self.retryButtonBackground.show()
            #call the hover method to change retry button background if user hovers over it
            self.retryButtonBackground.hover()
                
            #display retry button text
            self.retryButtonText.show()
            self.retryButtonText.position = ((w/2 - (self.retryButtonText.textWidth/2)), h-420)

            #pygame event listener for loop
            for event in pygame.event.get():
                #if user hits quit...
                if event.type == pygame.QUIT:
                    #quit pygame
                    pygame.quit()

                #call click method which checks if retry button was clicked
                self.retryButtonBackground.click(event)

            #if it was clicked, reset the hit counter, turn off the loser page and restart by re-calling the start method
            if self.retryButtonBackground.clicked == True:
                    self.hitCounter = 0
                    loser = False
                    self.start()

            #pygame animation control
            pygame.display.update()
            self.clock.tick(30) # framerate in fps
                    
    
    def playerWin(self):
        '''Method that creates the winning screen if the player wins according to outcome from gameplay method above'''

        #while loop boolean
        winner = True
        self.retryButtonBackground.clicked = False
        
        winningText = Text(font = gameOverFont, text = "YOU WIN!", color = "white")
        winningSecondLine = Text(font = instructionsFont, text = "Congratulations! You helped Alexis make it across campus and", color = "white")
        winningThirdLine = Text(font = instructionsFont, text = "safely to the weekend! It's time to party.", color = "white")

        pygame.mixer.Sound.play(winSound)
        #add screen with "You won!" and button that has option to replay
        winningCharacter = movingCharacter(w/2, h-150, playerCycle=allWinningJumpImages)
        winningCharacterJumpHeight = 28
        winningCharacter.x = (w/2-winningCharacter.imageWidth/2)

        self.retryButtonText.text = "REPLAY"

        while winner:
            win.fill("black")
            winningText.show()
            winningText.position = ((w/2 - (winningText.textWidth/2)), 50)

            winningSecondLine.show()
            winningSecondLine.position = ((w/2 - (winningSecondLine.textWidth/2)), 190)

            winningThirdLine.show()
            winningThirdLine.position = ((w/2 - (winningThirdLine.textWidth/2)), 230)


            self.retryButtonBackground.show()
            self.retryButtonBackground.hover()

            self.retryButtonText.show()
            self.retryButtonText.position = ((w/2 - (self.retryButtonText.textWidth/2)), h-420)
            
            winningCharacter.characterAnimation()
            
            winningCharacter.y -= winningCharacterJumpHeight
            winningCharacterJumpHeight -= 2
            if winningCharacterJumpHeight < -28:
                winningCharacterJumpHeight = 28

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                self.retryButtonBackground.click(event)
            if self.retryButtonBackground.clicked == True:
                    self.hitCounter = 0
                    winner = False
                    self.start()

            pygame.display.update()
            self.clock.tick(30) # framerate in fps (30-60 is typical)

    def main(self):
        self.start()

if __name__ == '__main__':
    Manager().main()       