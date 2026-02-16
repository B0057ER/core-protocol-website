import turtle

# --- Setup the screen ---
screen = turtle.Screen()
screen.title("Interactive Turtle Example")
screen.bgcolor("lightblue")
screen.setup(width=800, height=600)

# --- Create the turtle ---
player = turtle.Turtle()
player.shape("turtle")
player.color("green")
player.speed(0)  # Animation speed (0 = fastest)

# --- Movement functions ---
def move_forward():
    player.forward(20)

def move_backward():
    player.backward(20)

def turn_left():
    player.left(15)

def turn_right():
    player.right(15)

def change_color():
    """Cycle through a list of colors."""
    colors = ["green", "blue", "red", "purple", "orange"]
    current_color = player.pencolor()
    next_color = colors[(colors.index(current_color) + 1) % len(colors)]
    player.color(next_color)

# --- Keyboard bindings ---
screen.listen()  # Start listening for key presses
screen.onkeypress(move_forward, "Up")
screen.onkeypress(move_backward, "Down")
screen.onkeypress(turn_left, "Left")
screen.onkeypress(turn_right, "Right")
screen.onkeypress(change_color, "space")

# --- Keep the window open ---
screen.mainloop()
