from graphics import *
win = GraphWin("Hey", 500, 500)

def BlueCircle100 (the_center):
 the_circle = Circle(the_center, 100)
 the_circle.setFill("blue")
 return the_circle

pnt= Point (200, 200)
pnt2= Point (350,350)

first_circle= BlueCircle100(pnt)
first_circle.draw(win)

second_circle= BlueCircle100(pnt2)
second_circle.draw(win)


win2 = GraphWin("win2", 500, 500)

def ColoredCircle100 (the_center, color):
 the_circle = Circle(the_center, 100)
 the_circle.setFill(color)
 return the_circle

third_circle= ColoredCircle100(pnt, "red")
third_circle.draw(win2)

fourth_circle= ColoredCircle100(pnt2, "blue")
fourth_circle.draw(win2)

win3 = GraphWin("win3", 500, 500)

def ClickCircle100 (color):
 new_point = win3.getMouse()
 x = new_point.getX()
 y = new_point.getY()
 pnt3= Point (x,y)
 the_circle = Circle(pnt3,100)
 the_circle.setFill(color)
 return the_circle

fifth_circle=ClickCircle100("blue")
fifth_circle.draw(win3)

sixth_circle=ClickCircle100("red")
sixth_circle.draw(win3)

win4 = GraphWin("win4", 500, 500)

def Square(a,b,length):
 point= Point(a,b)
 point2= Point(a+length,b+length )
 rect= Rectangle(Point(a,b),point2)
 return rect

sqr=Square(100,200, 100)
sqr.draw(win4)

sqr2=Square(250,250,50)
sqr2.draw(win4)

win5 = GraphWin("win5", 500, 500)

def House(a,b):
 p1= Point(a,b)
 p2= Point(a, b+50)
 p3= Point(a+50, b+50)
 p4= Point(a+50,b)
 p5= Point(a+25, b-25)
 house= Polygon(p1,p2,p3,p4,p5)
 return house

h1=House(200,200)
h1.draw(win5)

h2=House(400,400)
h2.draw(win5)
 



input("press a key to continue")
