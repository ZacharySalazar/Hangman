import pygame
import time
import random
import sys
import os
import webbrowser
from pynput.keyboard import Key, Controller
import pygame.mixer
from pygame.mixer import Sound
from pygame.mixer import music
import requests
from bs4 import BeautifulSoup
pygame.mixer.pre_init()
pygame.init()
pygame.mixer.init()
win = pygame.display.set_mode((1000,800))
surfaceCreation = pygame.font.SysFont('Comic Sans MS',50)
pygame.display.set_caption("Hangman")

#images
gallows = pygame.image.load('gallows.jpg')
gallows = pygame.transform.scale(gallows,(1000,800))
blankLine = pygame.image.load('blankLine.jpg')
blankLine = pygame.transform.scale(blankLine,(40,10))
grimReaper = pygame.image.load('grimReaper.jpg')
grimReaper = pygame.transform.scale(grimReaper,(200,200))
gallowsAlert = pygame.image.load('gallowsAlert.jpg')
gallowsAlert = pygame.transform.scale(gallowsAlert,(1000,800))
gallowsLookAt = pygame.image.load('gallowsLookAt.jpg')
gallowsLookAt = pygame.transform.scale(gallowsLookAt,(1000,800))
gameWonImage = pygame.image.load('gameWonImage.jpg')
gameWonImage = pygame.transform.scale(gameWonImage,(1000,800))

sp1 = pygame.image.load('sp1.png')
sp1 = pygame.transform.scale(sp1,(200,300))
sp2 = pygame.image.load('sp2.png')
sp2 = pygame.transform.scale(sp2,(200,300))
sp3 = pygame.image.load('sp3.png')
sp3 = pygame.transform.scale(sp3,(200,300))
sp4 = pygame.image.load('sp4.png')
sp4 = pygame.transform.scale(sp4,(200,300))

categoryChoice = pygame.image.load('categoryChoice.jpg')
categoryChoice = pygame.transform.scale(categoryChoice,(1000,800))

gameStarted = pygame.image.load('gameStarted.jpg')
gameStarted = pygame.transform.scale(gameStarted,(1000,800))
gameStarted1 = pygame.image.load('gameStarted1.jpg')
gameStarted1 = pygame.transform.scale(gameStarted1,(1000,800))
gameStarted2 = pygame.image.load('gameStarted2.jpg')
gameStarted2 = pygame.transform.scale(gameStarted2,(1000,800))
gameStarted3 = pygame.image.load('gameStarted3.jpg')
gameStarted3 = pygame.transform.scale(gameStarted3,(1000,800))
gameStarted4 = pygame.image.load('gameStarted4.jpg')
gameStarted4 = pygame.transform.scale(gameStarted4,(1000,800))
gameStarted5 = pygame.image.load('gameStarted5.jpg')
gameStarted5 = pygame.transform.scale(gameStarted5,(1000,800))
gameStarted6 = pygame.image.load('gameStarted6.jpg')
gameStarted6 = pygame.transform.scale(gameStarted6,(1000,800))

#sound Effects
rightLetter = pygame.mixer.Sound("rightLetter.wav")
wrongLetter = pygame.mixer.Sound("wrongLetter.wav")
wonderSound = pygame.mixer.Sound('wonderSound.wav')
crowsSound = pygame.mixer.Sound('crowsSound.wav')
crowdCheering = pygame.mixer.Sound('crowdCheering.wav')
#music
#pygame.mixer.music.load('epicMusic.wav')
pygame.mixer.music.load('ambientMusic.wav')

print('here')
 
def getCategories():
    f = open('wordFile.txt','r')
    category = False
    foodList = []
    InstrumentsList = []
    DisneyList = []
    FastFoodList = []
    SuperHeroesList = []
    wordList = []
    readFile = f.read()
    currentWord = ''
    for i in readFile:
        currentWord += i
        
        if currentWord == 'Food':
            foodList = wordList
            wordList = []
            currentWord = ''
  
        if currentWord == 'Instruments':
            InstrumentsList = wordList
            wordList = []
            currentWord = ''
            
        if currentWord == 'Disney-Characters':
            
            DisneyList = wordList
            wordList = []
            currentWord = ''
        if currentWord == 'FFP':
            FastFoodList = wordList
            wordList = []
            currentWord = ''
        if currentWord == 'Super-Heroes':
            SuperHeroesList = wordList
            wordList = []
            currentWord = ''
            
        elif i == ' ':
            wordList.append(currentWord[:-1])
            currentWord = ""
            
    #print(foodList)
    return foodList, InstrumentsList, DisneyList, FastFoodList, SuperHeroesList
    
    print(InstrumentsList)
    print(DisneyList)
    print(FastFoodList)
    print(SuperHeroesList)
    
getCategories()

def clicked(xPosition, yPosition):
    if xPosition > 13 and xPosition < 250 and yPosition > 100 and yPosition < 170:
        return True
    elif xPosition > 23 and xPosition < 240 and yPosition > 210 and yPosition < 275:
        return True
    elif xPosition > 22 and xPosition < 318 and yPosition > 320 and yPosition < 390:
        return True
    elif xPosition > 25 and xPosition < 350 and yPosition > 440 and yPosition < 500:
        return True
    elif xPosition > 40 and xPosition < 270 and yPosition > 560 and yPosition < 620:
        return True
        
def ask(xCoordinate, yCoordinate):
    string = ''
    stringArray =[]
    while True:
        event = pygame.event.poll()
        keys = pygame.key.get_pressed()
        
        if event.type == pygame.KEYDOWN:
            key = pygame.key.name(event.key)  # Returns string id of pressed key.
            
            if len(key) == 1:  # This covers all letters and numbers not on numpad.
                if keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]:
                    #if  # Include any other shift characters here.
                    #else:
                    string += key.upper()
                    
                else:
                    string += key
            #elif  # Include any other characters here.
            elif key == "backspace":
                string = string[:len(string) - 1]
                
            elif event.key == pygame.K_RETURN:  # Finished typing.
                return string
                break
            
            
            text = surfaceCreation.render(string, 1, (0,0,255))
            win.blit(text,(xCoordinate,yCoordinate))
            
           
            pygame.display.update()
            

    
    
def gameStart(category):
    gameRunning = True
    foodList, instrumentsList, disneyList, fastFoodList, superHeroesList = getCategories()
    categoryText = category
    categoryLongText = categoryText
    categoryText = surfaceCreation.render(categoryText,3,(255,0,0))
    
    if category == 'Food':
        randomPick = random.choice(foodList)
        print(randomPick)
    elif category == 'Instruments':
        randomPick = random.choice(instrumentsList)
        print(randomPick)
    elif category == 'Fast Food Places':
        randomPick = random.choice(fastFoodList)
        print(randomPick)
    elif category == 'Disney':
        randomPick = random.choice(disneyList)
        print(randomPick)
    elif category == 'Super Heroes':
        randomPick = random.choice(superHeroesList)
        print(randomPick)
    
    length = len(randomPick)

    correctLettersList = []
    for i in randomPick:
        correctLettersList.append(i)
        
    x = 1
    currentIndexList = []
    confirmedLettersList = []
    confirmWinList = set()
    lineIndexList = []
    usedLettersList = set()
    usedL = []
    guessed = False
    countGuessesList = []
    countGuesses = 0
    startNewMusic = False
    instanceSong = 0
    while gameRunning:
        if startNewMusic:
            pygame.mixer.music.stop()
            pygame.mixer.music.load('epicMusic.wav')
            pygame.mixer.music.set_volume(.8)
            pygame.mixer.music.play()
            startNewMusic = False
        if countGuesses >= 6:
            gameOver = True
            print('You Lose!')
            crowsSound.play()
            while gameOver:
                pygame.mixer.music.stop()
                event = pygame.event.poll()
                win.blit(gameStarted6,(0,0))
                xLocations = 350
                yLocations = 300
                wordMessage = ''.join(correctLettersList)
                wordMessage = surfaceCreation.render(wordMessage,1,(0,255,0))
                clickMessage = 'Click anywhere to restart'
                clickMessage = surfaceCreation.render(clickMessage,1,(0,255,255))
                win.blit(wordMessage,(130,340))
                win.blit(clickMessage,(90,600))
                #for i in correctLettersList:
                        #drawI = i
                        #drawI = surfaceCreation.render(drawI,1,(0,0,255))
                        #win.blit(drawI,(xLocations,yLocations))
                       # xLocations += 40
                pygame.display.update()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pygame.mixer.music.load('ambientMusic.wav')
                    pygame.mixer.music.set_volume(.8)
                    pygame.mixer.music.play()
                    instanceSong = 0
                    hangMan()
                    
        elif countGuesses < 6:
            guessState = countGuesses
            if guessState == 0:
                win.blit(gameStarted,(0,0))
            elif guessState == 1:
                win.blit(gameStarted1,(0,0))
            elif guessState == 2:
                win.blit(gameStarted2,(0,0))
            elif guessState == 3:    
                win.blit(gameStarted3,(0,0))
            elif guessState == 4:
                win.blit(gameStarted4,(0,0))
            elif guessState == 5:
                win.blit(gameStarted5,(0,0))
                
                
            
            
            
        if len(categoryLongText) > 6:
            win.blit(categoryText,(60,140))
        else:
            win.blit(categoryText,(170,140))

        lineX = 20
        for i in randomPick+'x'[:-1]:
            if i == '.':
                drawLine = False
                lineX += 80
            elif i!= '.':
                drawLine = True
            if drawLine == True:
                win.blit(blankLine,(lineX,700))
                lineIndexList.append((lineX, 635))
                #usedLetterList.append(i)
                lineX += 50
                   
    #appended user letter list then function that takes that list  goes through it and draws each letter  and matches its position to its indexCounter one all is drawn it updates anytime a matching letter is added to the list and continues from tehre
        #find duplicate letters add to a set and save them to indexes if indexes are met in for loop continue them
                    #add() userLetter to usedList
                    #if len(usedList > 0):
                        #for i in used (usedList) this is a set()
                            #for z in correct (correctList)
                                #if i == z:
                                    #draw i at lineIndexList[correctList.index(z)]
                    #if i==z
                    #draw i at lineIndexList[correctList.index(z)]

        #make a duplicate function
        #for i in string
                #if i == '.'
                #string.remove('.')

                #

        def indexall(list1, value):
            return [i for i, v in enumerate(list1) if v == value]
        
        period = '.'
        if period in correctLettersList:
            newList = correctLettersList.remove('.')
            
     
        if guessed == True:
            
            usedLettersList.add(playerGuess)
            if playerGuess not in usedL:
                
                usedL.append(playerGuess)
            for i in randomPick:
                if i == '.':
                   
                   continue
            for i in range(len(randomPick)):
                
                
                for i in usedLettersList:
                    for z in correctLettersList:
                        if i == z:
                            duplicateList = indexall(correctLettersList,i)
                            
                            
                            drawingI = i
                            drawingI = surfaceCreation.render(drawingI,1,(0,0,255))
                            for i in duplicateList:
                                win.blit(drawingI,lineIndexList[i])
            xLocation = 650
            yLocation = 10
            ySwitch = 0
            for i in usedL:
                    drawI = i
                    drawI = surfaceCreation.render(drawI,1,(0,0,255))
                    win.blit(drawI,(xLocation,yLocation))
                    xLocation += 40
                    ySwitch += 1
                    if ySwitch == 4:
                        yLocation += 60
                        xLocation = 650
                    if ySwitch == 8:
                        yLocation += 60
                        xLocation = 650
                    if ySwitch == 12:
                        yLocation += 60
                        xLocation = 650
        pygame.display.update()
        event = pygame.event.poll()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mousePosition = pygame.mouse.get_pos()
            if mousePosition[0] > 700 and mousePosition[0] < 820 and mousePosition[1] > 180 and mousePosition[1] < 300 and event.type == pygame.MOUSEBUTTONDOWN:
                
                
                playerGuess = ask(770,220)
                usedLettersList.add(playerGuess)
                guessed = True
                
                if playerGuess in correctLettersList:
                    rightLetter.play()
                    print('Guesses used so far: ',countGuesses)
                    confirmWinList.add(playerGuess)
                    print('The confirm List is: ', confirmWinList, 'the correct List is: ', correctLettersList)
                    lengthOfCorrect = len(correctLettersList)
                    if len(confirmWinList) > 0:
                        confirmCounter = 0
                        for element in confirmWinList:
                            for element1 in correctLettersList:
                                if element == element1:
                                    confirmCounter += 1
                                    print(element, ' is in the correct List! and is found')
                                    print('confirmed number of letters found is: ',confirmCounter)
                                    print('remaining total of letters to find is: ',lengthOfCorrect - confirmCounter)
                        if confirmCounter == lengthOfCorrect:
                            print('game won')
                            gameWon = True
                            correctWord = ''.join(correctLettersList)
                            correctWord = surfaceCreation.render(correctWord,1,(0,255,0))
                            while gameWon:
                                pygame.mixer.music.stop()
                                crowdCheering.play()
                                event = pygame.event.poll()
                                win.blit(gameWonImage,(0,0))
                                win.blit(correctWord,(80,150))
                                clickAnywhere = 'Click anywhere      to restart'
                                clickAnywhere = surfaceCreation.render(clickAnywhere,1,(0,0,255))
                                win.blit(clickAnywhere,(80,400))
                                pygame.display.update()
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                    crowdCheering.stop()
                                    pygame.mixer.music.load('ambientMusic.wav')
                                    pygame.mixer.music.set_volume(.8)
                                    pygame.mixer.music.play()
                                    instanceSong = 0
                                    break
                                
    
                                    
                            break
                            
                        
                    
                        
                else:
                    wrongLetter.play()
                    instanceSong += 1
                    if instanceSong == 1:
                        
                        startNewMusic = True
                    instanceSong += 1
                    
                    countGuesses += 1
                    print(countGuesses)
                    continue
                
                    
        if event.type == pygame.MOUSEMOTION:
            xStart, yStart = event.pos
                 
                           
        if event.type == pygame.MOUSEMOTION:
                xStart, yStart = event.pos
        #t = 't'
        #t = surfaceCreation.render(t,1,(0,0,255))
       # win.blit(t,(700,200))        
        pygame.display.update()
               
        
def hangMan():
    class stickMan:
        def __init__ (self,xPosition,image):
            self.xPosition = xPosition
            self.image = image
    pygame.mixer.music.set_volume(.8)
    pygame.mixer.music.play()
    clock = pygame.time.Clock()
    #img1 = stickMan(movingX,sp1)
    #img2 = stickMan(movingX,sp2)
    #img3 = stickMan(movingX,sp3)
    #img4= stickMan(movingX,sp4)
    win.blit(gallows,(0,0))
    imageID = 0
    movingX = 40
    while not movingX >= 800:
        pygame.event.get()
        pygame.display.update()
        imageID += 1
        clock.tick(15)
        win.blit(gallows,(0,0))
        if imageID == 1:
            win.blit(sp4,(movingX,500))
            #pygame.display.update()
            movingX += 10
            print(movingX)
        elif imageID == 2:
            win.blit(sp2,(movingX,500))
            #pygame.display.update()
            movingX += 10
            print(movingX)
        elif imageID == 3:
            win.blit(sp3,(movingX,500))
            #pygame.display.update()
            movingX += 10
        elif imageID == 4:
            win.blit(sp1,(movingX,500))
            #pygame.display.update()
            movingX += 10
            imageID = 0
        if movingX == 790:
            print('i ran')
            alertPhase = True
            startTimer = pygame.time.get_ticks()
            break
  
    while alertPhase == True:
        pygame.event.get()
        pygame.display.update()
        seconds = (pygame.time.get_ticks()-startTimer)/1000
        if seconds < 2:
            win.blit(gallowsAlert,(0,0))
            
        elif seconds > 2 and seconds < 5:
           win.blit(gallowsLookAt,(0,0))
            
        elif seconds > 5:
            break
        
    menuRunning = True
                
            
    
            
    while menuRunning:
        menuStart = True
        win.blit(categoryChoice,(0,0))
        pygame.display.update()



        if menuStart == True:
            
            event = pygame.event.poll()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            elif event.type == pygame.MOUSEMOTION:
                xStart, yStart = event.pos
                print(xStart,yStart)
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousePosition = pygame.mouse.get_pos()
                confirmationClick = clicked(mousePosition[0],mousePosition[1])
                if confirmationClick == True:
                    if mousePosition[1] < 170:
                        gameStart('Food')
                    elif mousePosition[1] < 275:
                        gameStart('Instruments')
                    elif mousePosition[1] < 390:
                        gameStart('Fast Food Places')
                    elif mousePosition[1] < 500:
                        gameStart('Disney')
                    elif mousePosition[1] < 620:
                        gameStart('Super Heroes')
    #class Letters:
        #def _init_(self,letter,letterX,letterY):
           # self.letter = letter
           # self.letterX = letterX
           # self.letterY = letterY
    
    
    
    
hangMan()    
