'''

04/12/2021

Review

1. import turtle library
import turtle  # Top of page

2. declare turtle
variable1 = turtle.Turtle()

3. declare screen (option)
variable2 = turtle.Screen()

4. movements
  a. forward
  variable1.forward(DISTANCE)
  variable1.fd(DISTANCE)

  b. backward
  variable1.backward(DISTANCE)
  variable1.bk(DISTANCE)

  c. turn right
  variable1.right(ANGLE)

  d. turn left
  variable1.left(ANGLE)

5. pen features
  penup
  variable1.penup()

  pendown
  variable1.pendown()

  move to a point
  variable1.goto(X,Y)

  move to the origin
  variable1.home()

  color
  variable1.color(COLOR)

  shape (arrow, turtle, circle, square)
  variable1.shape(SHAPE)

  speed (0,10)
  variable1.speed()

  write 
  variable1.write(TEXT,MOVE,ALIGN,FONT)
  FONT = (FONTTYPE,FONTSIZE,FONTSTYLE)

  width (1,10)
  variable1.width()

  circle
  variable1.circle(RADIUS)
  variable1.circle(RADIUS, ANGLE)
  variable1.circle(RADIUS, ANGLE, SIDE)

  fill color
  variable1.fill("COLOR")

  variable1.begin_fill()
  # SHAPE
  variable1.end_fill()
'''


import turtle

pen = turtle.Turtle()

'''
# Exercise 1 - Drawing a star
def drawStar(l):
  for x in range(5):
    pen.forward(l)
    pen.right(144)

drawStar(int(input("LENGTH :")))
'''

'''
# Exercise 2 - Drawing shapes with circle()

def drawShape(r,s):
  pen.circle(r,360,s)

drawShape(float(input("Radius: ")), int(input("Number of side: ")))
'''

# Exercise 3 - Draw a Spiral

# List with colors
colors = ['orange','red','blue','green','cyan','yellow']

# for Loop
for x in range(50):
  pen.color(colors[x % 6])
  pen.width(x / 5 + 1)
  pen.forward(x)
  pen.left(20)