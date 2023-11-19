import turtle
Window = turtle.Screen()
t = turtle.Turtle()
t.speed(0)
t.pensize(2)
def spiral(size, angle):
    for _ in range(150):
        t.forward(size)
        t.right(angle)
        size += 5

spiral(0.01, 140)
Window.exitonclick()