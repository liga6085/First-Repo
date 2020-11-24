#!/usr/bin/env python
# coding: utf-8

'''
Turtle starter code
ATLS 1300
Author: Dr. Z
Author: Lily Gabriel
May 29, 2020
'''

from turtle import * #import the library of commands that you'd like to use
import random
colormode(255)

bgcolor(0,5,1) #rich black

#Create a panel to draw on. 
panel = Screen()
w = 700 # width of panel
h = 700 # height of panel
panel.setup(width=w, height=h) #700 x 700 is a decent size to work on. 
#You can experiment by making it the size of your screen or super tiny!

#Don't change this line (puts (0,0) at upper left corner)
panel.setworldcoordinates(0, w, h, 0)

#=======Add your code here======
color(227, 215, 255) #lavender blue

penup()

goto(355, 355)

right(90)

pensize(3)

pendown()

repeats = range(18)
radius = 25
color = [20,40,80]
for element in repeats:
    circle(radius)
    forward(10)
    right(20)
    
penup()

pencolor(175, 162, 255) #maximum blue purple

goto(412, 356) 

pendown()

repeats = range(48) #it took me forever to figure out this configuration
radius = 50 #there has to be a smarter way but I couldn't figure it out, it was a lot of guess and check
color = [20,40,80]
for element in repeats:
    circle(radius)
    forward(12)
    right(8)

penup()

goto(150, 435)

pencolor(122, 137, 194) #glaucous

pendown()

circle(200)

penup()

goto(140, 435)

pencolor(114, 120, 141) #slate gray

pendown()

circle(210)




