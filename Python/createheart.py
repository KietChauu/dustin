# Vẽ trái tim 
import math 
import turtle

t = turtle.Turtle()
turtle.speed(2000)
turtle.bgcolor("black")

def corazon(k):
    return 15 * math.sin(k) ** 3

def corazon1(k):
    return 12 * math.cos(k) - 5 * math.cos()