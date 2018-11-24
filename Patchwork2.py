from graphics import *
def createWin():
    win = GraphWin("Patch Window",500,500)
    initialGrid(win)
   # dVLines(win,0,0)



def slopeLines(win,x,y,colour):
    print()

def vLines(win,x,y,x2,y2):
    x+=x2
    y+=y2
    
    for a in range(0,2500,625):
        line = Line(Point(x+(a/100),y),Point(x+(a/100),y+25))
        line.draw(win)
        
def dLines(win,x,y,x2,y2):
    print()
    

def dVLines(win,x,y,colour):
    count = 0
    for x2 in range(0,100,25):
        count += 1
        for y2 in range(0,100,25):
            count +=1
            box = Rectangle(Point(x+x2,y+y2),Point(x+x2+25,y+y2+25))
           
            if count%2!=0:
                box.setFill(colour)
                vLines(win,x,y,x2,y2)
            else:
                dLines(win,x,y,x2,y2)
                
            box.draw(win)   
    
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
