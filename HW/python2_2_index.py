import turtle
turtle.shape('turtle')
turtle.penup()
turtle.backward(300)
turtle.pendown()
turtle.speed(0.5)
def line(x1, x2, y2):
    turtle.pendown()
    turtle.goto(turtle.pos()+ (x2, y2))
    turtle.penup()
a=50
def one():
    turtle.penup(),
    turtle.goto(turtle.pos()+(0, a)),
    line(turtle.pos(), a, a),
    line(turtle.pos(), 0, -2*a),
    turtle.penup(),
    turtle.goto(turtle.pos()+(a/4, 0))
    
def zero():
         line(turtle.pos(), 0, a+a)
         line(turtle.pos(), a, 0)
         line(turtle.pos(), -0, -2*a)
         line(turtle.pos(), -a, 0)
         turtle.penup()
         turtle.goto(turtle.pos()+ (a*1.25, 0))
def two():
         turtle.penup()
         turtle.goto(turtle.pos()+ (0, 2*a))
         turtle.pendown()
         line(turtle.pos(), a, 0)
         line(turtle.pos(), -0, -a)
         line(turtle.pos(), -a, -a)
         line(turtle.pos(), a, 0)
         turtle.penup()
         turtle.goto(turtle.pos()+ (a/4, 0))
def four():
         turtle.penup()
         turtle.goto(turtle.pos()+ (0, 2*a))
         turtle.pendown()
         line(turtle.pos(), 0, -a)
         line(turtle.pos(), a, 0)
         line(turtle.pos(), 0, a)
         line(turtle.pos(), 0, -2*a)
         turtle.penup()
         turtle.goto(turtle.pos()+ (a/4, 0))
def three():
         line(turtle.pos(), a, a)
         line(turtle.pos(), -a, 0)
         line(turtle.pos(), a, a)
         line(turtle.pos(), -a, 0)
         turtle.penup()
         turtle.goto(turtle.pos()+ (a*1.25, -a-a))
def five():
         line(turtle.pos(), a, 0)
         line(turtle.pos(), 0, a)
         line(turtle.pos(), -a, 0)
         line(turtle.pos(), 0, a)
         line(turtle.pos(), a, 0)
         turtle.penup()
         turtle.goto(turtle.pos()+ (a/4, -2*a))
def six():
         turtle.penup()
         turtle.goto(turtle.pos()+ (a, 2*a))
         turtle.pendown()
         line(turtle.pos(), -a, -a)
         line(turtle.pos(), -0, -a)
         line(turtle.pos(), a, 0)
         line(turtle.pos(), 0, a)
         line(turtle.pos(), -a, 0)
         turtle.penup()
         turtle.goto(turtle.pos()+ (a*1.25, -a))
def seven():
         line(turtle.pos(), 0, a)
         line(turtle.pos(), a, a)
         line(turtle.pos(), -a, 0)
         turtle.penup()
         turtle.goto(turtle.pos()+ (a*1.25, -2*a))
def eight():
         line(turtle.pos(), 0, 2*a)
         line(turtle.pos(), a, 0)
         line(turtle.pos(), 0, -2*a)
         line(turtle.pos(), -a, 0)
         line(turtle.pos(), 0, a)
         line(turtle.pos(), a, 0)
         line(turtle.pos(), 0, -a)
         turtle.penup()
         turtle.goto(turtle.pos()+ (a/4, 0))
def nine():
         line(turtle.pos(), a, a)
         line(turtle.pos(), -0, a)
         line(turtle.pos(), -a, 0)
         line(turtle.pos(), 0, -a)
         line(turtle.pos(), a, 0)
         turtle.penup()
         turtle.goto(turtle.pos()+ (a/4, -a))
d={'1': (one()),
   "2": (two()),
   "3": (three()),
   "4": (four()),
   "5": (five()),
   "6": (six()),
   "7": (seven()),
   "8": (eight()),
   "9": (nine()),
   "0": (zero()),
  }






















