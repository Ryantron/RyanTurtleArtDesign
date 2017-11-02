import turtle
bob = turtle.Turtle()
ryan = turtle.Turtle()
gabriel = turtle.Turtle()
from random import randint
from myshape import *
turtle.colormode(255)
#Name of Art: Creature of Surprise
bob.speed(0)
ryan.speed(0)
gabriel.speed(0)
turtle.bgcolor("gray")
red = randint(0,255)
green = randint(0,255)
blue = randint(0,255)
#Random color probability for the remainder of the Project.
bob.color(red,green,blue)
ryan.color(red,green,blue)
gabriel.color(red,green,blue)
move(bob,-300,150)
move(ryan,150,150)
move(gabriel,700,0)
wire(bob, 50)
wire(ryan,50)
#The wire function are the middle swirls that are the "barbed wires".
move(gabriel,-570,-180) 
gabriel.right(20)

for n in range(10):
    clover(gabriel,20)
    gabriel.forward(30)
#The clover function acts as the ragged polygons in the bottom left and right corners.
move(gabriel,680,-220)
gabriel.right(20)
for x in range(10):
    clover(gabriel,20)
    gabriel.forward(30)

move(ryan,-350,-350)
move(bob,350,-350)
for times in range(40):
 bob.color(red,green,blue)
 ryan.color(red,green,blue)
 star(ryan,20)
 ryan.forward(10)
 ryan.right(10)
 star(bob,20)
 bob.forward(10)
 bob.right(10)
#Sprializing a star produces fancy circles, located at the bottom.
move(ryan,-220,-340)
move(bob,145,-345)
for times in range(37):
 bob.color(0,100,255)
 ryan.color(0,100,255)
 star(ryan,20)
 ryan.forward(10)
 ryan.right(10)
 star(bob,20)
 bob.forward(10)
 bob.right(10)

move(ryan,-480,-162)
ryan.right(130)
border(ryan)
for a in range(2):
 ryan.forward(10)
 triangle(ryan,5)
move(gabriel,680,250)
abstract(gabriel)
#The blue line with triangles are the border.
move(gabriel,-500,50)
abstract(gabriel)
#The abstract function is the purple stars that act as ornaments.
move(bob,0,0)
ovals(bob,50)
bob.left(-135)
move(bob,-10,0)
ovals(bob,50)
bob.left(90)
bob.begin_fill()
bob.end_fill()
#The ovals form a barrier over the border.


