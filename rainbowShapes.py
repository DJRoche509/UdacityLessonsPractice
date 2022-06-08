from turtle import Turtle

rainbow = ["red", "orange", "yellow", "green", "blue", "purple", "turquoise", 'skyblue', 'grey', 'black']

# Write whatever code you want here!
djr = Turtle()
djr.shape('turtle')
djr.width(8)
djr.penup()
djr.back(50)
djr.setpos((-40,140))
djr.up()
djr.up()
djr.pendown()
for side in rainbow:
    djr.color(side)
    djr.forward(100)
    djr.right(36)
djr.hideturtle()

draw = Turtle()
rainbow = ['blue', 'purple', 'green', 'yellow', 'orange', 'red', 'turquoise', 'pink']
draw.speed(4)
draw.width(5)
draw.penup()
draw.setpos((60,-5))
draw.pendown()
for side in rainbow:
    draw.color(side)
    draw.right(135)
    draw.forward(100)
draw.hideturtle()