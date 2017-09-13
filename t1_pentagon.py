#!/usr/bin/env python 

import turtle

t = turtle.Turtle()

# Comment out for debugging.
turtle.tracer(1000, 1)
t.ht()

# What you need is a loop that makes
# a slightly open pentagon (sum of angles > 360)
# with sides whose lengths grow slowly with each iteration.

turtle.update()
input("HOLD") # This just allows use to see it.
turtle.getcanvas().postscript(file="pentagon_tunnel.ps")

