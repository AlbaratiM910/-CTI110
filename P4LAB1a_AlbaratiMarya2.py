import turtle
t=turtle.Turtle()
t.penup()
#draw straight line
t.goto(-30,50) #centering in the screen
t.pendown()
t.pensize(10)
t.pencolor("blue")

t.right(90)
t.forward(150)
 
t.goto(-30,50)
t.goto(20,-20)
t.goto(65,50)
t.goto(65,-100)


# A
t=turtle.Turtle()
t.penup()
t.goto(120,50) #centering in the screen
t.pendown()
t.pensize(10)
t.pencolor("red")

t.right(65)
t.forward(100)

t.setpos(120,50)
t.right(50)
t.forward(100)

t.penup()
t.setpos(100,-10)
t.right(65)
t.pendown()
t.backward(50)

# Hide turtle
t.hideturtle()

# Keep the window open until it is closed by the user
turtle.done()
