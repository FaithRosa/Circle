import turtle
import colorsys
import math

t = turtle.Turtle()
t.speed(0)
n = 70
h = 0
for i in range(360):
    c = colorsys.hsv_to_rgb(h, 1, 0.8)
    h += 1 / n
    t.color(c)
    t.left(1)
    t.fd(1)
    for j in range(2):
        t.left(2)
        t.circle(100)


def heart(i):
    return 15 * math.sin(i) ** 3


def heartAche(i):
    return 12 * math.cos(i) - 5 * math.cos(2 * i) - 2 * math.cos(3 * i) - math.cos(4 * i)


y = 'y'
turtle.speed(1000)
while y == 'y':  # Run the heart function indefinitely
    for i in range(6000):
        turtle.goto(heart(i) * 20, heartAche(i) * 20)
        for j in range(1):
            turtle.color('#f73487')
        turtle.goto(0, 0)

turtle.done()

