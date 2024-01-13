import turtle as t

# Score variables
playerAscore = 0
playerBscore = 0

# Create a window
window = t.Screen()
window.title("The Pong Game")
window.bgcolor("white")
window.setup(width=800, height=600)
window.tracer(0)

# Creating the left paddle
leftpaddle = t.Turtle()
leftpaddle.speed(0)
leftpaddle.shape("square")
leftpaddle.color("black")
leftpaddle.shapesize(stretch_wid=5, stretch_len=1)
leftpaddle.penup()
leftpaddle.goto(-350, 0)

# Creating the right paddle
rightpaddle = t.Turtle()
rightpaddle.speed(0)
rightpaddle.shape("square")
rightpaddle.color("black")
rightpaddle.shapesize(stretch_wid=5, stretch_len=1)
rightpaddle.penup()
rightpaddle.goto(350, 0)

# Code for creating the ball
ball = t.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("black")
ball.penup()
ball.goto(0, 0)
ballxdirection = 0.2
ballydirection = 0.2

# Code for creating pen for scorecard update
pen = t.Turtle()
pen.speed(0)
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=('Arial', 24, 'normal'))

# Functions for moving the left paddle
def leftpaddleup():
    y = leftpaddle.ycor()
    y += 90
    if y > 250:
        y = 250
    leftpaddle.sety(y)

def leftpaddledown():
    y = leftpaddle.ycor()
    y -= 90
    if y < -250:
        y = -250
    leftpaddle.sety(y)

# Functions for moving the right paddle
def rightpaddleup():
    y = rightpaddle.ycor()
    y += 90
    if y > 250:
        y = 250
    rightpaddle.sety(y)

def rightpaddledown():
    y = rightpaddle.ycor()
    y -= 90
    if y < -250:
        y = -250
    rightpaddle.sety(y)

# Assign keys to play
window.listen()
window.onkeypress(leftpaddleup, 'w')
window.onkeypress(leftpaddledown, 's')
window.onkeypress(rightpaddleup, 'Up')
window.onkeypress(rightpaddledown, 'Down')

# Function to check the score and declare a winner
def check_score():
    global ballxdirection, ballydirection
    if playerAscore == 3:
        pen.goto(0, 0)
        pen.write("Player A wins!", align="center", font=('Arial', 24, 'normal'))
        ballxdirection, ballydirection = 0, 0
        return True
    elif playerBscore == 3:
        pen.goto(0, 0)
        pen.write("Player B wins!", align="center", font=('Arial', 24, 'normal'))
        ballxdirection, ballydirection = 0, 0
        return True
    return False

# Main game loop
while True:
    window.update()

    # Moving the ball
    ball.setx(ball.xcor() + ballxdirection)
    ball.sety(ball.ycor() + ballydirection)

    # Border setup
    if ball.ycor() > 290:
        ball.sety(290)
        ballydirection *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ballydirection *= -1

    # Ball crosses the right paddle
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ballxdirection *= -1
        playerAscore += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {} ".format(playerAscore, playerBscore), align="center", font=('Arial', 24, "normal"))
        if check_score():
            break

    # Ball crosses the left paddle
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ballxdirection *= -1
        playerBscore += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {} ".format(playerAscore, playerBscore), align="center", font=('Arial', 24, "normal"))
        if check_score():
            break

    # Handling the collisions with paddles
    if (340 < ball.xcor() < 350) and (rightpaddle.ycor() + 50 > ball.ycor() > rightpaddle.ycor() - 50):
        ball.setx(340)
        ballxdirection *= -1

    if (-350 < ball.xcor() < -340) and (leftpaddle.ycor() + 50 > ball.ycor() > leftpaddle.ycor() - 50):
        ball.setx(-340)
        ballxdirection *= -1

# Keep the window open
window.mainloop()
