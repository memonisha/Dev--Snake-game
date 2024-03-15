from p5 import *


def setup():
  global snake, tail
  snake = {"x":200, "y":150, "direction" :"left"}
  tail = [{"x":225, "y":150}]
  createCanvas(1000,700)
  tail.append({"x":250, "y":150})
  tail.append({"x":275, "y":150})
  textAlign (CENTER)
  textSize (100)
  
  

def draw():
  global snake, tail
  background('black')
  drawTickAxes()
  fill ("white")
  square (snake["x"], snake["y"], 25)
  fill("grey")
  square (tail[0]["x"], tail[0]["y"], 25)
  square (tail[1]["x"], tail[1]["y"], 25)
  square (tail[2]["x"], tail[2]["y"], 25)
  if keyCode == 39:
    if snake["direction"] == "left":
      text ("game over", width/2, height/2)
    else:
      snake["direction"] = "right"
      snake["x"] += 10
      tail[0]["x"] = snake["x"] - 25
      tail[0]["y"] = snake["y"] 
      tail[1]["x"] = snake["x"] - 50
      tail[1]["y"] = snake["y"] 
      tail[2]["x"] = snake["x"] - 75
      tail[2]["y"] = snake["y"] 
  if keyCode == 37:
    if snake["direction"] == "right":
      text ("game over", width/2, height/2)
    else:
      snake["direction"] = "left"
      snake["x"] -= 10
      tail[0]["x"] = snake["x"] + 25
      tail[0]["y"] = snake["y"] 
      tail[1]["x"] = snake["x"] + 50
      tail[1]["y"] = snake["y"] 
      tail[2]["x"] = snake["x"] + 70
      tail[2]["y"] = snake["y"] 
  if keyCode == 38:
    if snake["direction"] == "down":
      text ("game over", width/2, height/2)
    else:
      snake["direction"] = "up"
      snake["y"] += 10
      tail[0]["y"] = snake["y"] - 25
      tail[0]["x"] = snake["x"]
      tail[1]["y"] = snake["y"] - 50
      tail[1]["x"] = snake["x"]
      tail[2]["y"] = snake["y"] - 75
      tail[2]["x"] = snake["x"]
  if keyCode == 40:
    if snake["direction"] == "up":
      text ("game over", width/2, height/2)
    else:
      snake["direction"] = "down"
      snake["y"] -= 10
      tail[0]["y"] = snake["y"] + 25
      tail[0]["x"] = snake["x"]
      tail[1]["y"] = snake["y"] + 50
      tail[1]["x"] = snake["x"]
      tail[2]["y"] = snake["y"] + 75
      tail[2]["x"] = snake["x"]
  

  