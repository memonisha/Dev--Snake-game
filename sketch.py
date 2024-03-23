from p5 import *
import random

def setup():
  global snake, tail, gamestate, foodx, foody, listx, listy, score, youlose
  snake = {"x":200, "y":150, "direction" :"left"}
  tail = [{"x":225, "y":150}]
  createCanvas(1000,700)
  tail.append({"x":250, "y":150})
  tail.append({"x":275, "y":150})
  textAlign (CENTER)
  textSize (100)
  gamestate = True
  loadSound ('eat.mp3', 'eat')
  loadSound ('lose.mp3', 'lose')
  loadSound ('bgmusic.mp3', 'bgmusic')
  
  frameRate (15)
  listx = [0, 25, 50, 75, 100, 125, 150, 175, 200, 225, 250, 275, 300, 325, 350, 375, 400, 425, 450, 475, 500, 525, 550, 575, 600, 625, 650, 675, 700, 725, 750, 775, 800, 825, 850, 875, 900, 925, 950, 975, 1000]
  listy = [0, 25, 50, 75, 100, 125, 150, 175, 200, 225, 250, 275, 300, 325, 350, 375, 400, 425, 450, 475, 500, 525, 550, 575, 600, 625, 650, 675]
  foodx = random.choice (listx) 
  foody = random.choice (listy)
  score = 0
  youlose = False
  
  

def draw():
  global snake, tail, gamestate, youlose
  assets['bgmusic'].play()
  background('black')
  drawTickAxes()
  fill ("white")
  square (snake["x"], snake["y"], 25)
  fill("grey")
  # 3----range(3)----0,1,2
  for i in range(len(tail)):
    square (tail[i]["x"], tail[i]["y"], 25)
    
  if gamestate == False:
    background ('black')
    fill ("red")
    textSize (100)
    text ("game over", width/2, height/2)
    if youlose == False:
      assets['lose'].play()
      youlose = True
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
  edges ()
  if gamestate == True:
    createfood ()
    collectfood ()
    fill ("white")
    textSize (20)
    text (f"score: {score}", 60, 650)
      

''' #tailnew=[ {-25, 0}, {-50, 0}, {-75, 0},{?,?}]
# k=len(tail)
for n in range(k)
if snakedir=="right":
  for i in range(tailpos):
     
def movesnake(s,tailnew):
   global snake
   snake["x"]+=s["x"]
   snake["y"]+=s["y"]

   for i in range(len(tail)):
       for h in range:
         tail[i]["x"] = snake["x"] +h
         tail[i]["y"] = snake["y"] + h
   


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
def edges ():
  global snake, gamestate
  if snake["x"] < 0 or snake["y"] < 0 or snake["x"] > 1000 or snake["y"] > 675:
    gamestate = False
  
def createfood ():
  
  fill ("red")
  global foodx, foody
 
  square (foodx, foody, 25)
def collectfood ():
  global snake, foodx, foody, tail, listx, listy, score
  if snake["x"] == foodx and snake["y"] == foody:
    foodx = random.choice (listx) 
    foody = random.choice (listy)
    length=len(tail)
    #tail.append({"x":tail[length-1]["x"]+50, "y":tail[length-1]["y"]+50})
    score = score + 1
    assets['eat'].play()
    
  
  