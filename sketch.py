from p5 import *
import random

def setup():
  noStroke ()
  global gamestate, foodx, foody, listx, listy, score, youlose
  global snakeHead,tail,snakeSpeed, direction
  
  #snake = {"x":200, "y":150, "direction" :"left"}
  #tail = [{"x":225, "y":150}]
  snakeHead={
    'x':225,
    'y':250,
    'size':25
  }
  tail=[{'x':250,'y':250},{'x':275,'y':250},{'x':300,'y':250}]
  snakeSpeed = {
    "x": 0,
    "y": 0
  }
  createCanvas(1000,700)
  #tail.append({"x":250, "y":150})
  #tail.append({"x":275, "y":150})
  textAlign (CENTER)
  textSize (100)
  gamestate = True
  loadSound ('eat.mp3', 'eat')
  loadSound ('lose.mp3', 'lose')
  loadSound ('reflections.mp3', 'reflections')
  loadFont ('fredoka.ttf', "font")
  textFont (assets['font'])
  direction = "left"
  frameRate (15)
  listx = [0, 25, 50, 75, 100, 125, 150, 175, 200, 225, 250, 275, 300, 325, 350, 375, 400, 425, 450, 475, 500, 525, 550, 575, 600, 625, 650, 675, 700, 725, 750, 775, 800, 825, 850, 875, 900, 925, 950, 975]
  listy = [0, 25, 50, 75, 100, 125, 150, 175, 200, 225, 250, 275, 300, 325, 350, 375, 400, 425, 450, 475, 500, 525, 550, 575, 600, 625, 650, 675]
  foodx = random.choice (listx) 
  foody = random.choice (listy)
  score = 0
  youlose = False
  
  
  

def draw():
  global snake, tail, gamestate, youlose,direction

  
  
  background('black')
  fill("red")
  textSize(22)
  
  if gamestate == False:
    background ('black')
    fill ("red")
    textSize (100)
    text ("game over", width/2, height/2)
    if youlose == False:
      assets['lose'].play()
      youlose = True
      assets['reflections'].stop ()
  elif gamestate == True:
    snake()
    snakeUpdate()
    createfood ()
    collectfood ()
    edges()
    snakeEatsTail ()
    fill ("white")
    textSize (20)
    text (f"Score: {score}", 60, 650)
    text ("Song: Creo - Reflections", 890, 675)
    text ("sfx from zapslat.com", 900, 650)
    if assets['reflections'].isPlaying() == False:
      assets['reflections'].play()
      assets['reflections'].setVolume (0.15)

  '''
  #moving up
  if keyCode == 39 and gamestate == True:
    if snake["direction"] == "left":
      gamestate = False
    else:
      snake["direction"] = "right"
      movesnake ({"x":25,"y":0}, -25, 0, -50, 0, -75, 0)
  #moving left
  if keyCode == 37 and gamestate == True:
    if snake["direction"] == "right":
      gamestate = False
    else:
      snake["direction"] = "left"
      movesnake ({"x":-25,"y":0}, 25, 0, 50, 0, 75, 0)
  #moving up
  if keyCode == 38 and gamestate == True:
    if snake["direction"] == "down":
      gamestate = False
    else:
      snake["direction"] = "up"
      movesnake ({"x":0,"y":25}, 0, -25, 0, -50, 0, -75)
  #moving down
  if keyCode == 40 and gamestate == True:
    if snake["direction"] == "up":
      gamestate = False
    else:
      snake["direction"] = "down"
      movesnake ({"x":0,"y":-25}, 0, 25, 0, 50, 0, 75)
  '''


'''
def movesnake(s,t0x,t0y,t1x,t1y,t2x,t2y):
  global snake,tail
  snake["x"]+=s["x"]
  snake["y"]+=s["y"]
  
  tail[0]["x"] = snake["x"] +t0x
  tail[0]["y"] = snake["y"] + t0y

  tail[1]["x"] = snake["x"] + t1x
  tail[1]["y"] = snake["y"] + t1y
  
  tail[2]["x"] = snake["x"] + t2x
  tail[2]["y"] = snake["y"] + t2y
'''

def edges ():
  global snakeHead, gamestate
  if snakeHead["x"] < 0 or snakeHead["y"] < 0 or snakeHead["x"] > 1000 or snakeHead["y"] > 675:
    gamestate = False
  
def createfood ():
  
  fill ("red")
  global foodx, foody
 
  square (foodx, foody, 25)


def collectfood ():
  global snakeHead, foodx, foody, tail, listx, listy, score, snakeSpeed 
  if snakeHead["x"] == foodx and snakeHead["y"] == foody:
    foodx = random.choice (listx) 
    foody = random.choice (listy)
    length=len(tail)
    #tail.append({"x":tail[length-1]["x"]+50, "y":tail[length-1]["y"]+50})
    score = score + 1
    assets['eat'].play()

    size=snakeHead['size']
    lastIndex=len(tail)-1
    tail.append({
      'x':tail[lastIndex]['x']-size,
      'y':tail[lastIndex]['y']
    })


def snake():
  global snakeHead,snakeTail
  fill("grey")
  square(snakeHead['x'],snakeHead['y'],snakeHead['size'])
  for i in range( len(tail)):
    fill('white')
    square(tail[i]['x'],tail[i]['y'],25)


def snakeDirection(x, y):
  global snakeSpeed
  snakeSpeed["x"] = x
  snakeSpeed["y"] = y

def keyPressed():
  global gamestate, direction
  if gamestate:
    
    if keyCode == 37:
      # left
      if direction == "right":
        gamestate = False
      else:
        direction = "left"
        snakeDirection(-1, 0)
        
    elif keyCode == 38:
      if direction == "down":
        gamestate = False
      else:
        direction = "up"
        snakeDirection(0, 1)
        
    elif keyCode == 39:
      # right
      if direction == "left":
        gamestate = False
      else:
        direction = "right"
        snakeDirection(1, 0)
        
    elif keyCode == 40:
      # down
      if direction == "up":
        gamestate = False
      else:
        direction = "down"
        snakeDirection(0, -1)
        

def snakeUpdate ():
  global snakeHead,tail,snakeSpeed
  if snakeSpeed["x"] == 0 and snakeSpeed["y"] == 0:
    pass 
  else:
  #  snake -> head, [tail0, tail1, tail2, tail3...]

    for i in range (len(tail)-1, 0, -1):
      tail[i]['x']=tail[i-1]['x']
      tail[i]['y']=tail[i-1]['y']
    tail[0]['x']=snakeHead['x']
    tail[0]['y']=snakeHead['y']
    snakeHead["x"] += snakeSpeed["x"]*25
    snakeHead["y"] += snakeSpeed["y"]*25

def snakeEatsTail ():
  global snakeHead, tail, gamestate
  #tail=[{x:90,y:78},{},{},{}]
  #snakeHead={x:45,y:67}
  for i in range (len(tail)):
    if snakeHead["x"] == tail[i]["x"] and snakeHead["y"] == tail[i]["y"]:
      gamestate = False

  
