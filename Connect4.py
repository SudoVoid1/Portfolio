import turtle
import math

drawer=turtle.Turtle()
screen= turtle.Screen()
announcer = turtle.Turtle()
announcer.penup()
announcer.ht()
announcer.goto(-200,0)
announcer.color("red")

screen.tracer(0)
def drawBoard():
    #Horizontal Lines
    for i in range(7):
        drawer.penup()
        drawer.goto(-380,300-(100*i))
        drawer.pendown()
        drawer.forward(700)
    drawer.right(90)
    screen.update()
    #Vertical lines
    for i in range(9):
        drawer.penup()
        drawer.goto(-380+100*i,300)
        drawer.pendown()
        drawer.forward(600)


def drawME(x,y): #Users positon to draw circle
    drawer.color("red")
    drawer.penup()
    drawer.goto(x,y) # middle of a square (15,50)
    drawer.pendown()
    for i in range(180):
        drawer.forward((100* math.pi)/200)
        drawer.right(2)
    
    screen.update()

def drawBot():
    drawer.color("blue")
    drawer.penup()






#Postions of spaces
def sONE():
    drawME(-285,-250+(50*i))
def sTWO():
    drawME(-185,-250)  
def sTHREE():
    drawME(-85,-250)
def sFOUR():
    drawME(15,-250)
def sFIVE():
    drawME(115,-250)
def sSIX():
    drawME(215,-250)
def sSEVEN():
    drawME(315,-250)
functions = [sONE,sTWO,sTHREE,sFOUR,sFIVE,sSIX,sSEVEN]
#This function activates all the number inputs
def activate(functions):
    for i in range(7):
        screen.onkey(functions[i], str(i+1))
def deactivate():
    for i in range(7):
        screen.onkey(None, str(i+1))

drawBoard()
activate(functions)
screen.listen() #listens to keyboard input

board = []
for i in range(6):
    row = []
    for j in range(7):
        row.append("")
    board.append(row)





screen.exitonclick()