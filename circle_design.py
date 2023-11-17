import turtle as t
import colorsys

t.bgcolor('black')
t.tracer(10)
t.pensize(1)
h = 0.5

for i in range(400):
    t.speed(10)
    c = colorsys.hsv_to_rgb(h,1,1)
    t.fillcolor(c)
    h += 0.008
    t.begin_fill()
    t.fd(i)
    t.lt(100)
    t.circle(10)
    for j in range(2):
        t.fd(i*j)
        t.rt(105)
    t.end_fill()
t.done()