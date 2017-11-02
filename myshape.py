import turtle
bob = turtle.Turtle()
def triangle(t,distance):
    for times in range(3):
        t.forward(25)
        t.right(120)
        
def octagon(t, distance):
 for times in range(8):
    t.forward(100)
    t.right(72)

def move (bob, x, y):
 bob.penup()
 bob.goto(x, y)
 bob.pendown()

def star(t,distance):
 t.begin_fill()
 for times in range(5):
  t.forward(distance)
  t.right(120)
  t.forward(distance)
  t.right(72 - 120)
 t.end_fill()

def wire(t,distance):
  for n in range(20):
    t.color(n*10,0,0)
    t.circle(n*5)
    t.width(n * 0.5)
    t.right(45)
    t.circle(40)
    t.forward(n*5)
    
def clover (t,distance):
    for times in range(5):
        t.begin_fill()
        octagon(t,40)
        t.forward(50)
        t.end_fill()
        t.left(50)

def border (t):
    for l in range(35):
        t.forward(30)
        triangle(t,5)

def abstract(t):
    for c in range(100):
      t.color(c*2,0,c*2)
      t.forward(250)
      t.right(98)

def ovals(t,distance):
    t.left(90)
    t.begin_fill()
    for s in range(20):
        t.forward(20)
        t.right(25)
        t.backward(20)
        t.left(25)
    t.end_fill()


