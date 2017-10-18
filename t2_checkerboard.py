#!/usr/bin/env python

import turtle

t = turtle.Turtle()

import turtle

t = turtle.Turtle()
t.speed(0)

#let us define a function that draws and fills one square

def square(size,alternate,color):
    t.color(color)
    t.begin_fill()#to fill and set the color
    for i in range(4):

        t.forward(size)
        t.left(90)

    t.end_fill()#set and fill the color
    t.forward(size)#moves the turtle forward by the size

#defining function row to draw a row of squares

def row(size,alternate,color1,color2):

    for i in range(4):
        if(alternate==True):
            square(size,alternate,color1)
            square(size,alternate,color2)
        else:
            square(size,alternate,color2)
            square(size,alternate,color1)

#draws the whole chessboard by repeating the drawing rows function

def chessboard(size,alternate,color1,color2):
    t.pu()#moves without drawing to get the white square without drawing the outlines
    t.goto(-(size*4),(size*4))

    for i in range(8):#to draw squares over the 8 by 8 rows
        row(size,alternate,color1,color2)
        t.backward(size*8)
        t.right(90)
        t.forward(size)
        t.left(90)

        if(alternate==True):#condition to get a black square and then a white square
            alternate=False

        else:
            alternate=True

chessboard(50,True,'black','white')

turtle.update()
input("HOLD")

t.getscreen().getcanvas().postscript(file="checkerboard.ps")
