import math
import turtle

########### Your Code here ##############
# You should only have functions here
# If you have anything outside of a function, 
# then you do not fully understand functions
# and should review how they work or ask for help

def drawSineCurve(dart):
  dart.color("Purple")
  for i in range(-360,361):
    y = math.sin(math.radians(i))
    dart.goto(i,y)


def setupWindow(wn): 
  wn.setworldcoordinates(-360,-1,360,1)
  wn.bgcolor("lightblue")
def setupAxis(dart):
  dart.color("black")
  dart.goto(-360,0)
  dart.goto(360,0)
  dart.goto(0,0)
  dart.goto(0,1)
  dart.goto(0,-1)

def drawCosineCurve(dart):
  dart.color("pink")
  dart.goto(-360,0)
  dart.goto(-360,1)
  for i in range (-360,361):
    x = math.cos(math.radians(i))
    dart.goto(i,x)
  
def drawTangentCurve(dart):
  dart.color("green")
  dart.goto(360,0)
  dart.goto(-360,0)
  for i in range (-360,361):
    z= math.tan(math.radians(i))
    dart.goto(i,z)   


##########  Do Not Alter Any Code Past Here ########
def main():
#Part A
    wn = turtle.Screen()
    wn.tracer(5)
    dart = turtle.Turtle()
    dart.speed(0)
    drawSineCurve(dart)

    #Part B
    setupWindow(wn)
    setupAxis(dart)
    dart.speed(0)
    drawSineCurve(dart)
    drawCosineCurve(dart)
    drawTangentCurve(dart)
    wn.exitonclick()
main()

  #Part A
wn = turtle.Screen()
wn.tracer(5)
dart = turtle.Turtle()
dart.speed(0)
drawSineCurve(dart)

    #Part B
setupWindow(wn)
setupAxis(dart)
dart.speed(0)
drawSineCurve(dart)
drawCosineCurve(dart)
drawTangentCurve(dart)
wn.exitonclick()
main()