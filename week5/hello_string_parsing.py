import turtle
cmd = "drawsquare 10,7 50 red"
print(cmd)
x = cmd.split()
print(x)
turtleTemp = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor("white")

commands = ["drawsquare", "drawcircle", "drawtriangle", "drawhexagon", "drawrectangle", "drawpolygon"]
turtleNames = ["Leo","Alpha","Charlie","Delta","Echo","Foxtrot","Golf","Hotel","India","Juliet","Kilo","Lima","Mike","November","Oscar","Papa","Quebec","Romeo","Sierra","Tango","Uniform","Victor","Whiskey","Xray","Yankee","Zulu"]

def validateCommand(command):
    return command in commands

def destroyTurtle(name):
    # it only clears the turtle object lines that he has drawn 
    # We cannot destroy a turtle ever we can only hide it.
    # hiddenTurtle.hideturtle()
    # name.clear()
    if name in turtleNames:
        turtleNames.remove(name)

def validateColor(color):
    try:
       turtleTemp.color(color)
       return True
    except:
       print("It is not a valid color")
       return True

def validateTokens(tokens):
    return len(tokens) == 3 

# def validateDesign(design):
#     return design in turtleShapes

checkDesign = validateCommand("drawcircle")
print("Command exists : ",checkDesign)
checkColor = validateColor("table")
print( "Color exists : ",checkColor)

screen.exitonclick()