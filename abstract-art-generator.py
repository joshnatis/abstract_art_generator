#Created by Josh Natis in 2017
#Refactor: 07/25/2019 (Fix bug with alpha values causing all colors to be black)
  # the culprit was the turtle.color() function, as it no longer accepted 2 parameters
  # replaced with turtle.color() and turtle.pencolor()

#!/bin/python3

import turtle
import random

turtle.hideturtle()

def moveTurtleRandomDirection(turtleDir,ranNum): #ranNum: random number corresponding to distance in pixels
  if turtleDir == 1:
    turtle.forward(ranNum)
  if turtleDir == 2:
    turtle.backward(ranNum)
  if turtleDir == 3:
    turtle.right(ranNum)
  if turtleDir == 4:
    turtle.left(ranNum)
        
        
def drawRandomLines(speed, pensize, rrange, ranNumBeg, ranNumEnd):
  turtle.speed(speed)
  turtle.pensize(pensize)
  for step in range(rrange):
    ranNum = random.randint(ranNumBeg,ranNumEnd)
    turtleDir = random.randint(1,5) #decide which direction to move in
    moveTurtleRandomDirection(turtleDir, ranNum) 
    turtle.pensize(random.randint(1,4))
    
    if abs(turtle.xcor()) >= 100 or abs(turtle.ycor()) >= 100: #return to center if moving beyond corners of screen
      turtle.goto(0,0)
      
  turtle.goto(0,0)
  
  
def createRandomWord():
  alphabet = {1:"a",2:"b",3:"c",4:"d",5:"e",6:"f",7:"g",8:"h",9:"i",10:"j",
              11:"k",12:"l",13:"m",14:"n",15:"o",16:"p",17:"q",18:"r",19:"s",
              20:"t",21:"u",22:"v",23:"w",24:"x",25:"y",26:"z"}
              
  randWordLength = random.randint(3,8)
  vowelizer = random.randint(1,1000) #attempt to add extra vowels in generated word
  
  word = ""
  for letter in range(randWordLength):
    randLetter = random.randint(1,26)
    
    # if these (extremely) random conditions are met, vowels will be inserted
    if vowelizer % 2 == 0:
      if vowelizer % 2 == 0 and vowelizer % 3 == 0 and vowelizer % 5 == 0:
        word = "lil " + word
        break
      elif vowelizer % 3 == 0 and vowelizer % 2 == 0:
        word += "a"
        letter +=1
      elif vowelizer % 4 == 0 and vowelizer % 2 != 0:
        word += "e"
        letter+=1
      elif vowelizer % 6 == 0:
        word+= "o"
        letter+=1
      elif vowelizer % 7 == 0 and  vowelizer % 2 == 0:
          word+= "ya"
          letter+=1
    
    word+= alphabet[randLetter]
  return word.capitalize()
  
  
def drawCoolShape():
  turtle.penup()
  
  randX = random.randint(-150,150)
  randY = random.randint(-150,150)
  randSize = random.randint(1,100)

  turtle.goto(randX, randY)
  turtle.pendown()
  turtle.speed(0)
  turtle.pensize(1)
  
  for step in range(100):
    turtle.forward(randSize)
    turtle.right(randSize*randSize)
    
    if abs(turtle.xcor()) >= 160 or abs(turtle.ycor()) >= 165:
      turtle.write(createRandomWord())
      turtle.goto(0,0)
      
  
def getRandomColor():
  LRed = (153, 0, 0, 0.3)
  LGreen = (0,255,0,0.3)
  LBlue = (0,0,153,0.3)
  LOrange = (255,128,0,0.3)
  LPurple = (102,0,102,0.3)
  LPink = (255,0,255,0.3)
  LYellow = (255,255,0,0.3)
  LWhite = (255,255,255,0.3)
  LBlack = (0,0,0,0.3)
  LPink2 = (255,204,229,0.3)
  LRed2 =(255,51,51,0.3)
  LSky = (0,255,255,0.3)
  DGreen = (0,102,0,0.3)
  Bpurp = (153,153,255,0.3)
  nPink = (255,9,127,0.3)
  blu3 = (51,153,255,0.3)
  shGold = (153,153,0,0.3)
  teals = (0,51,102,0.3)
  lgrey = (192,192,192,0.3)
  dddgreen = (0,51,0,0.3)
  velRed = (102,0,51,0.3)
  lavender = (230,230,250,0.3)
  slateGray = (49,79,79,0.3)
  midnightBlue = (25,25,112,0.3)
  LslateBlue = (132,112,255,0.3)
  deepSkyBlue = (0,191,255,0.3)
  LSeaGreen = (32,178,170,0.3)
  khaki = (240,230,140,0.3)	
  gold = (255,215,0,0.3)
  indianRed = (205,92,92,0.3)
  snow = (255,250,250,0.3)
  
  colors = [LRed, LGreen, LBlue, LOrange, LPurple, LPink, LYellow, LWhite, LBlack, 
            LPink2, LRed2, LSky, DGreen, Bpurp, nPink, blu3, shGold, teals, lgrey,
            dddgreen, velRed, lavender, slateGray, midnightBlue, deepSkyBlue, LSeaGreen,
            khaki, gold, indianRed, snow]

  return random.choice(colors)
  
  
def drawMultipleColoredShapes(amount):
  for i in range(amount):
    turtle.color(getRandomColor())
    turtle.pencolor(getRandomColor())
    turtle.begin_fill()
    drawCoolShape()
    turtle.end_fill()


def drawMultipleShapes(amount):
  for i in range(amount):
    drawCoolShape()


#entry point of the program

for i in range(10):
  drawMultipleShapes(5)
  drawMultipleColoredShapes(5)