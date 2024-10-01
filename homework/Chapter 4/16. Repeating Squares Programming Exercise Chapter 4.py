import turtle

turtle.penup()
turtle.goto(200, -200)
turtle.pendown()

animation_speed = 200
turtle.speed(animation_speed)

for i in range(5, 500, 5): 
    for _ in range(4): 
        turtle.left(90)
        turtle.forward(i)
