import turtle

def sayHello():
    print("Hello")

screen = turtle.Screen()
screen.bgcolor("lightgreen")

mikey = turtle.Turtle()
mikey.shape("turtle")
mikey.color("orange")

sid = turtle.Turtle()
sid.shape("turtle")
sid.color("purple")

def drawSquare(turtle):
    for i in range(0,4):
        turtle.forward(100)
        turtle.right(90)

# pick a turtle and move it to specicified position
# and have it draw a square
def drawSquareAt(turtle,x=60,y =60):
    mikey.up()
    mikey.goto(x,y)
    mikey.down()
    drawSquare(turtle)


leo = turtle.Turtle()
leo.color("hotpink")
leo.shape("turtle")

# To move anywhere from start point
# leo.up()
# leo.goto(-50,-50)   # start point
# leo.down()
# leo.goto(0,0)   # start point
# leo.goto(100,0)
# leo.goto(100,100)
# leo.goto(0,100)
# leo.goto(0,0)



# draw asquare with sides 100 using
# a series of relative commands

# for i in range(0,4):
#     mikey.forward(100)
#     mikey.left(90)


# mikey.right(90)
# mikey.forward(100)
# mikey.left(90)
# mikey.forward(100)
# mikey.left(90)
# mikey.forward(100)
# mikey.left(90)
# mikey.forward(100)
# mikey.forward(100)
# mikey.right(90)
# mikey.forward(100)
# mikey.right(90)
# mikey.forward(100)
# mikey.right(90)
# mikey.forward(100)
# mikey.forward(100)
# mikey.right(90)
# mikey.forward(100)
# mikey.right(90)
# mikey.forward(100)
# mikey.right(90)
# mikey.forward(100)

# Draw me a square with sides 100 using a 
# Series of goto commands
# leo.forward(150)
# leo.left(120)
# leo.forward(150)
# leo.left(120)
# leo.forward(150)
# mikey.up()
# mikey.goto(-150,-150)
drawSquareAt(mikey,150,150)


# Write a function taht moves the turtle to a new location
# Rotate the turtle to a specified heading
# Draw a rectangle
def drawRectangle(turtle,width=150,height=75):
    for i in range(0,4):
        if i%2 == 0:
            turtle.forward(150)
        else:
            turtle.forward(75)
        turtle.right(90)
    
    for side in [width, height,width, height]:
        turtle.forward(side)
        turtle.right(90)
        # turtle.up()
        # turtle.goto(width,height)
        # turtle.down()

def drawRectangleAt(turtle,x=-60,y=60, angle=0):
    turtle.up()
    turtle.goto(x,y)
    turtle.down()
    turtle.setheading(angle)
    drawRectangle(turtle)

drawRectangleAt(sid, -100, 100)
#program done executing, wait for a click before
screen.exitonclick()

# alex = turtle.Turtle()
# alex.color("hotpink")
# alex.shape("turtle")

# alex.forward(150)
# alex.left(120)
# alex.forward(150)
# alex.left(120)
# alex.forward(150)

# screen.mainloop(
    
# )