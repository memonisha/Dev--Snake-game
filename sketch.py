from p5 import *
import random

def setup():
  global snake, tail, gamestate, foodx, foody
  snake = {"x":200, "y":150, "direction" :"left"}
  tail = [{"x":225, "y":150}]
  createCanvas(1000,700)
  tail.append({"x":250, "y":150})
  tail.append({"x":275, "y":150})
  textAlign (CENTER)
  textSize (100)
  gamestate = True
  frameRate (15)
  listx = [0, 25, 50, 75, 100, 125, 150, 175, 200, 225, 250, 275, 300, 325, 350, 375, 400, 425, 450, 475, 500, 525, 550, 575, 600, 625, 650, 675, 700, 725, 750, 775, 800, 825, 850, 875, 900, 925, 950, 975, 1000]
  listy = [0, 25, 50, 75, 100, 125, 150, 175, 200, 225, 250, 275, 300, 325, 350, 375, 400, 425, 450, 475, 500, 525, 550, 575, 600, 625, 650, 675]
  foodx = random.choice (listx) 
  foody = random.choice (listy)
  
  

def draw():
  global snake, tail, gamestate
  background('black')
  drawTickAxes()
  fill ("white")
  square (snake["x"], snake["y"], 25)
  fill("grey")
  square (tail[0]["x"], tail[0]["y"], 25)
  square (tail[1]["x"], tail[1]["y"], 25)
  square (tail[2]["x"], tail[2]["y"], 25)
  if gamestate == False:
    background ('black')
    fill ("red")
    text ("game over", width/2, height/2)
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
  createfood ()
  
  

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
  
  
  