import turtle

def moveXY(x,y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()


for i in range(6):
    moveXY(-300,(i-2)*100)
    turtle.forward(500)
turtle.right(90)
for i in range(6):
    moveXY((i-3)*100,300)
    turtle.forward(500)
turtle.exitonclick()
