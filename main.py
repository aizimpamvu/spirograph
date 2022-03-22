import turtle as t
from turtle import Screen
import random

tim = t.Turtle()
tim.pensize(1)
tim.speed("fastest")

"""colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray",
           "SeaGreen"]"""
# Using list
directions = [0, 90, 180, 270]

# Using turple
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


# tim.color(random.choice(colours))
def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)


draw_spirograph(5)

s = Screen()
screen = Screen()
s.exitonclick()
