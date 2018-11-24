from graphics import *
def drawPatchWindow():
    win = GraphWin("Patch Window",100,100)
    for a in range(0,100,20):
        for b in range(0,100,20):
            
            line1 = Line(Point(a,b),Point(b,a))
            line1.draw(win)
            line2 = Line(Point(b,100-a),Point(a,100-b))
            line2.draw(win)

			
def box(win):
    for x in range(5):
        for y in range(5):
            try:
                if y%x == 0:
                    dlines(win,x,y)
                else:
                    vLines(win,x,y)
            except:
                dLines(win,x,y)
				
	
def vLines(win,oldX,oldY):
    x = oldX * 4
    y = oldY * 4
    for i in range(4):
        newX = x+i
        line = Line(Point(newX,y),Point(newX,y+4))
        line.draw(win)
    
def dLines(win,oldX,oldY):
    x = oldX * 4
    y = oldY * 4
    for i in range(4):
        newY = y+i
        line = Line(Point(x,newY),Point(x+4,newY))
        line.draw(win)


def createWin():
    win = GraphWin("Patch Window",1000,1000)
    box(win)
