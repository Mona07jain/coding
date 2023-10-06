import turtle
import random

# List of shapes the user can draw
shapes = ["square", "circle", "triangle"]

# Randomly select a shape for the user
selected_shape = random.choice(shapes)

# Function to draw a square
def draw_square():
    for _ in range(4):
        turtle.forward(100)
        turtle.right(90)

# Function to draw a circle
def draw_rectangle():
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(50)

# Function to draw a triangle
def draw_triangle():
    for _ in range(3):
        turtle.forward(100)
        turtle.left(120)

# Initialize the turtle screen
turtle.speed(1)
turtle.penup()
turtle.goto(0, 0)
turtle.pendown()

# Tell the user what to draw
print(f"Please draw a {selected_shape}:")

# Draw the selected shape
if selected_shape == "square":
    draw_square()
elif selected_shape == "rectangle":
    draw_rectangle()
elif selected_shape == "triangle":
    draw_triangle()

# Close the turtle graphics window on click
turtle.exitonclick()

    
