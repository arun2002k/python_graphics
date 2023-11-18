from turtle import *
import colorsys as cs

screen = Screen()
screen.bgcolor('black')
screen.setup(width=1.0, height=1.0)
pensize(2)
speed(10)
shape('turtle')
N = 18
color(cs.hsv_to_rgb((N-3)/20,1,1))
A = 360/N

for i in range(N):
    for j in range(N):
        fd(100-N*3)
        rt(A)
    rt(A)

done()