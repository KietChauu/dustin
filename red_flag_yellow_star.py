# Vẽ cờ nước VN

import turtle

screen = turtle.Screen()
screen.bgcolor("red")
star = turtle.Turtle()
star.speed(1)

def draw_star(size):
    star.color("yellow")
    star.begin_fill()
    for i in range (5):
        star.forward(size)
        star.right(144)
        star.forward(size)
        star.left(72)
    star.end_fill()

draw_star(100)
tuple.done()