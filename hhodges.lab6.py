#Hannah Hodges
#CS151, Dr. Rajeev
#Lab 6
#10/28/2021

#main program
def main():
    speed= int(input("Enter speed:"))
    color= int(input("Enter color:"))
    width= int(input("Enter height:"))
from graphics import *
def make_window( title, width, height ):
    title= int(input("Title:"))
    width= 500
    height= 500
    win = GraphWin(title, width, height)
    return win
#inital position of circle
def make_circle( x, y, radius ):
    x> 50 and x<450
    x= int(input("X="))
    y= 20
    radius= int(input("Radius:"))
    return Circle( Point( x, y ), radius )

def color_circle(circle, color ):
    circle.setFill( color )
    circle.setOutline( color )

colors = ['red', 'green', 'blue', 'orange', 'yellow', 'cyan', 'magenta',
          'dodgerblue', 'turquoise', 'grey', 'gold', 'pink']
class Point(GraphicsObject):
    def __init__(self, x, y):
        GraphicsObject.__init__(self, ["outline", "fill"])
        self.setFill = self.setOutline
        self.x = float(x)
        self.y = float(y)
def draw_and_color_circle( window, circle, color ):
    circle.setFill( color )
    circle.setOutline( color )
    circle.draw( window )
 #moves the object x and y postion
def move(self, dx, dy):
        self._move(dx, dy)
        canvas = self.canvas
        if canvas and not canvas.isClosed():
            trans = canvas.trans
            if trans:
                x = dx / trans.xscale
                y = -dy / trans.yscale
            else:
                x = dx
                y = dy
            self.canvas.move(self.id, x, y)
            if canvas.autoflush:
                _root.update()
def move( circle, moveX, moveY ):
    circle.move( moveX, moveY  )

def change_title( window,title ):
    window.master.title( title )
def sleep(ms):
    time.sleep( ms / 1000 )