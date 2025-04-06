import turtle

rocket=turtle.Turtle()
space=turtle.Screen()

spaceman=turtle.Turtle()
spaceman.penup()
spaceman.goto(-103,255)
space.addshape("space man.gif")#add to screen
spaceman.shape("space man.gif")

space.bgpic("background.gif")
space.addshape("rocket.gif")#called rocket  gif
rocket.shape("rocket.gif")#assigned to rocket
rocket.penup()
rocket.goto(180,-250)#to go to entry position
rocket.speed(10000)#to increase the speed of rocket

def up():
    rocket.setheading(90) 
    rocket.forward(10)
    rocket.setheading(0)
def down():
    rocket.setheading(270)
    rocket.forward(10)
    rocket.setheading(0)
def left():
    rocket.setheading(180)
    rocket.forward(10)
    rocket.setheading(0)
def right():
    rocket.forward(10)

turtle.listen()    




turtle.onkey(up,"Up")
turtle.onkey(down,"Down")
turtle.onkey(left,"Left")
turtle.onkey(right,"Right")

while True :
  space.update() #to update the screen everytime
  if rocket.distance(spaceman) < 10 : #to find the victory by minimal distance between spaceman and rocket
    space.bgpic("thank you.gif")
             

turtle.done()