from graphics import *
import time
def createWin():
    win = GraphWin("Patch Window",500,500)
    initialGrid(win)

def vLines(win,x,y,x2,y2):
    x+=x2
    y+=y2
    
    for a in range(0,2500,625):
        line = Line(Point(x+(a/100),y),Point(x+(a/100),y+25))
        line.draw(win)

def dLines(win,x,y,x2,y2):
    x+=x2
    y+=y2
    for a in range(0,2500,625):
        line = Line(Point(x,y+(a/100)),Point(x+25,y+(a/100)))
        line.draw(win)

def dVLines(win,x,y,colour):
    count = 0
    for x2 in range(0,100,25):
        count += 1
        for y2 in range(0,100,25):
            count +=1
            box = Rectangle(Point(x+x2,y+y2),Point(x+x2+25,y+y2+25))
           
            if count%2!=0:
                box.setFill(colour)
                box.draw(win)
                vLines(win,x,y,x2,y2)
            else:
                box.draw(win)
                dLines(win,x,y,x2,y2)

#----------------------------------------------------------------------------------------------------------

def slopeLines(win,x,y,colour):
    
    b = 60
    for a in range(0,120,20):
        
        x2 = x+100
        y2 = y+100
        
        #Positive Gradient
        line = Line(Point(x+a,y),Point(x,y+a))
        line.setOutline(colour)
        line.draw(win)

        line = Line(Point(x2-a,y2),Point(x2,y2-a))
        line.setOutline(colour)
        line.draw(win)

        
        #Negative Gradient
        line = Line(Point(x2-a,y2),Point(x,y+a))
        line.setOutline(colour)
        line.draw(win)
        
        line = Line(Point(x+a,y),Point(x2,y2-a))
        line.setOutline(colour)
        line.draw(win)

#----------------------------------------------------------------------------------------------------------

def initialGrid(win):
    PATCHSIZE = 500
    SQUARESIZE = 100
    patchPos = PATCHSIZE
    count = 0
    for x in range(0,PATCHSIZE,SQUARESIZE):
        patchPos -= SQUARESIZE
        for y in range(0,PATCHSIZE,SQUARESIZE):

            box = Rectangle(Point(x,y),Point(x+SQUARESIZE,y+SQUARESIZE))
            box.draw(win)
            
            if (count)%3==0:
                colour = 'red'

            if (count)%3==1:
                colour = 'blue'

            if (count)%3==2:
                colour = 'green'

                
                
            if patchPos == y:
                slopeLines(win,x,y,colour)
            else:
                dVLines(win,x,y,colour)
            count += 1
            
createWin()
