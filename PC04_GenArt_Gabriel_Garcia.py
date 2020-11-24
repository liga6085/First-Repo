#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 10:33:16 2020

@author: lilygabriel
"""

#importing
import random
from turtle import*

bgcolor("Black")

#defining turtles
setup()
turtleCircle = Turtle()
turtleLine = Turtle()


colormode(255)

IK_Blue = color(5, 41, 158) #International Klein Blue
M_Blue = color(94, 74, 227) #Marjorelle Blue
M_Purple = color(148, 123, 211) #Medium Purple
P_Pink = color(240, 167, 160) #Pastel Pink
Cyclemen = color(242, 108, 167) #Cyclemen

turtleCircle.up() #pen up

#colors = [IK_Blue, M_Blue, M_Purple, P_Pink, Cyclemen] #color list
colors = ["darkblue", "slateblue", "mediumpurple", "lightpink", "hotpink"]

for element in range(20):
    x = random.randint(-300, 300) #x-axis
    y = random.randint(-300, 300) #y-axis
    circle_size = random.randint(1, 300) #sets radius of circle
    circle_color = random.choice(colors) #sets color
    #circle_opacity = random.randint(1, 100) #sets opacity of circle
    
    turtleCircle.goto(x,y) #sets random location
    
    turtleCircle.down() #pen down
    
    turtleCircle.color(circle_color) 
    #turtleCircle.setfillopacity(circle_opacity)
    #turtleCircle.begin_fill()
    turtleCircle.circle(circle_size)
    #turtleCircle.end_fill()

    turtleCircle.up()
    
for element in range(20):
    line_length = random.randint(50, 150)
    line_angle = random.randint(10, 90)
    line_color = random.choice(colors)
    
    turtleLine.down()
    turtleLine.right(line_angle)
    turtleLine.color(line_color)
    turtleLine.forward(line_length)
    turtleLine.up()
    turtleLine.goto(0,0)
    
    
   
   
    
    
    
    