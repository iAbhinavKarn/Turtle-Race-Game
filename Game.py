from turtle import *        #Turtle is a Module present in Python
import time
from random import randint

sc = Screen()
sc.bgcolor("black")  # Change the background of new Window

penup()
goto(-250, 250)  # goto is a function used to go on a particular point on a Window

# Making Lanes for Race

for i in range(21):
    pencolor("white")  # Loop for making lanes
    write(i)
    right(90)
    forward(10)
    pendown()
    forward(150)
    penup()
    backward(160)
    left(90)
    forward(20)
    if i == 20:
        x, y = position()  # Posotion is a function used to find position of last lane and store it in x,y
        x = x
        penup()
        ht()  # ht is the shortform of the function hide-turtle which is used to hide the sign of turtle
pendown()

# Positioning turtles at the start line

color = ["red", "white", "blue", "yellow", "cyan"]  # List of turtle colors
turt = []  # list name turt
y = 230
for i in range(5):
    turt.append(Turtle())  # Loop for makin turtles and placing them on starting line
    turt[i].right(360)
    turt[i].color(color[i])
    turt[i].shape("turtle")
    turt[i].penup()
    turt[i].goto(-270, y)
    y = y - 30
    turt[i].pendown()

# Countdwn to start the Race

w = Turtle()  # variable w is an object of turtle
w.shape("turtle")
w.color("red")
w.penup()
w.goto(0, 10)
w.pendown()
w.write("Ready", move=False, align="center", font=("Arial", 50, "normal"))
time.sleep(1)
w.clear()
w.write("Steady", move=False, align="center", font=("Arial", 50, "normal"))
time.sleep(1)
w.clear()
w.write("Go", move=False, align="center", font=("Arial", 50, "normal"))
time.sleep(1)
penup()

# Moving turtle at a random speed

for i in range(140):
    turt[0].forward(randint(1, 5))  # Loop for moving Turtu=les at random speed
    a, b = turt[0].position()
    if x <= a:  # Condition for checking is the turtle moved crossed the finishing line if yes then rotate it 360 and print its name as winner
        turt[0].right(360)
        ht()
        penup()
        goto(0, -70)
        pendown()
        pencolor("red")
        write("Red Colour Turtle won the game", move=False, align="center", font=("Times Roman New", 25, "normal"))
        break
    turt[1].forward(randint(1, 5))
    a, b = turt[1].position()
    if x <= a:
        turt[1].right(360)
        ht()
        penup()
        goto(0, -70)
        pendown()
        pencolor("white")
        write("White Colour Turtle won the game", move=False, align="center", font=("Times Roman New", 25, "normal"))
        break
    turt[2].forward(randint(1, 5))
    a, b = turt[2].position()
    if x <= a:
        turt[2].right(360)
        ht()
        penup()
        goto(0, -70)
        pendown()
        pencolor("blue")
        write("Blue Colour Turtle won the game", move=False, align="center", font=("Times Roman New", 25, "normal"))
        break
    turt[3].forward(randint(1, 5))
    a, b = turt[3].position()
    if x <= a:
        ht()
        turt[3].right(360)
        penup()
        goto(0, -70)
        pendown()
        pencolor("Yellow")
        write("Yellow Colour Turtle won the game", move=False, align="center", font=("Times Roman New", 25, "normal"))
        break
    turt[4].forward(randint(1, 5))
    a, b = turt[4].position()
    if x <= a:
        turt[4].right(360)
        penup()
        ht()
        goto(0, -70)
        pendown()
        pencolor("Cyan")
        write("Cyan Colour Turtle won the game", move=False, align="center", font=("Times Roman New", 25, "normal"))
        break
done()

