import turtle

def create_square(square):
    square.shape("turtle")
    square.color("red")
    for i in range(4):
        square.fd(100)
        square.left(90)

square = turtle.Turtle()
angle = 0
for i in range(30):
    square.left(12)
    create_square(square)
