import turtle
import math

def drawBoard():
    
    #Draw both of the horizontal lines
    for i in range(2):
        drawer.penup()
        drawer.goto(-300,100-200*i)
        drawer.pendown()
        drawer.forward(600)

    drawer.right(90)

    #Update the screen with new changes
    screen.update()
    for i in range(2):
        drawer.penup()
        drawer.goto(-100+200*i,300)
        drawer.pendown()
        drawer.forward(600)
    
    #Add numbers to the top corner of each square
    num =1
    for i in range(3):
        for j in range(3):
            drawer.penup()
            drawer.goto(-290+ j*200, 280 - i * 200)
            drawer.pendown()

            drawer.write(num,font = ("Arial",12))
            num+=1
    
def drawX(x,y):
    drawer.penup()
    drawer.goto(x,y)
    drawer.pendown()

    drawer.setheading(60)
    for i in range(2):
        drawer.forward(75)
        drawer.backward(150)
        drawer.forward(75)
        drawer.left(60)
    screen.update()


def drawO(x,y):
    drawer.penup()
    drawer.goto(x,y+75)
    drawer.pendown()

    drawer.setheading(0)

    #Draw a circle with the correct size
    for i in range(180):
        drawer.forward((150* math.pi)/180)
        drawer.right(2)

    screen.update()

# Checks if x or o wins
def checkWon(letter):
    for i in range(3):
        #Horizontal
        if board[i][0] == board[i][1] and board[i][1] == board[i][2] and board[i][0] ==letter:
            return True
            #Vertical
        if board[0][i] == board[1][i] and board[1][i] == board[2][i] and board[0][i] == letter:
            return True
            #Diagonally down
    if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] == letter:
        return True
        #diagonally up
    if board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[0][2] == letter:
        return True
    return False

def checkDraw():
    count = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == "x":
                count+= 1
    if count > 3:
        return True
    else:
        return False
        

def addO():
    for i in range(3):
        for j in range(3):
            if board[i][j] == "":
                board[i][j] = "o"
                if checkWon("o"):
                    drawO(-200+200*j, 200-200*i)
                    return
                board[i][j]= ""
    for i in range(3):
        for j in range(3):
            if board[i][j] == "":
                board[i][j] = "x"
                if checkWon("x"):
                    board[i][j] = "o"
                    drawO(-200+200*j,200-200*i)
                    return
                board[i][j] = ""
    for i in range(0,3,2):
        for j in range(0,3,2):
            if board[i][j] == "":
                board[i][j] = "o"
                drawO(-200+200*j, 200-200*i)
                return
        
            
#This function activates all the event listeners
def activate(functions):
    for i in range(9):
        screen.onkey(functions[i], str(i+1))
def deactivate():
    for i in range(9):
        screen.onkey(None, str(i+1))
    

def addX(row,column):
    #Clear announcer
    announcer.clear()
    #check position on board
    if board[row][column] == "x" or board[row][column] == "o":
        announcer.write("That spot is taken", font = ("Arial",36))
        screen.update()
    else:
        #draw an x in the correct spot
        drawX(-200+200* column, 200-200 * row)
        #Add an x to the computers board
        board[row][column] = "x"

        if checkWon("x"):
            announcer.goto(-97,0)
            announcer.write("You won!", font = ("Arial",36))

            screen.update()
            deactivate()
        else:
            addO()
            if checkWon('o'):
                announcer.goto(-90,0)
                announcer.write("You lost", font = ("Arial", 36))
                screen.update
                deactivate()
            elif checkDraw():
                announcer.goto(-90,0)
                announcer.write("Draw", font = ("Arial", 36))
                screen.update()
                deactivate()
    

def sONE():
    addX(0,0)
def sTWO():
    addX(0,1)  
def sTHREE():
    addX(0,2)
def sFOUR():
    addX(1,0)
def sFIVE():
    addX(1,1)
def sSIX():
    addX(1,2)
def sSEVEN():
    addX(2,0)
def sEIGHT():
    addX(2,1)
def sNINE():
    addX(2,2)

functions = [sONE,sTWO,sTHREE,sFOUR,sFIVE,sSIX,sSEVEN,sEIGHT,sNINE]



#Create Turtle
drawer=turtle.Turtle()
announcer = turtle.Turtle()

drawer.pensize(10)
drawer.ht()

announcer.penup()
announcer.ht()
announcer.goto(-200,0)
announcer.color("red")

#Create screen
screen= turtle.Screen()
screen.tracer(0)
drawBoard()

#Create the board
board = []
for i in range(3):
    row = []
    for j in range(3):
        row.append("")
    board.append(row)



activate(functions)
screen.listen()



screen.exitonclick()



