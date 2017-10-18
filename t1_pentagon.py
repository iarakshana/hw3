#!/usr/bin/env python

import turtle as t

t = turtle.Turtle()

# Comment out for debugging.
#turtle.tracer(1000, 1)
#t.ht()

import turtle as t
p = t.Pen() #opens the turtle page with the arrow
p.down() #this draws when it is moving so we can get the angle changes for the pentagon
p.speed(22)#increases the speed of the drawing so don't have to wait as long for the picture
for i in range(100):
    p.forward(i)#it keeps going forward for every i in the range in this case 100
    p.left(2222)#.left to use angle movements for the turtle #arbitrarily increased from multiples of 108 which is thw angle
    #for a pentagon

# What you need is a loop that makes
# a slightly open pentagon (sum of angles > 360)
# with sides whose lengths grow slowly with each iteration.

turtle.update()
input("HOLD") # This just allows use to see it.
turtle.getcanvas().postscript(file="pentagon_tunnel.ps")
