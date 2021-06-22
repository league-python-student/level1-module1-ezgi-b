from Ball import Ball
from Paddle import Paddle
global started
started = False

def setup():
    pass
    size(900, 600)
    global ball, paddle_one, paddle_two, score_one, score_two
    ball = Ball(450, 300)
    paddle_one = Paddle(100, 250)
    paddle_two = Paddle(800, 250)
    score_one = 0
    score_two = 0
def draw():
    global ball, paddle_one, paddle_two, score_one, score_two, started
    if not started:
        textSize(32)
        fill(0)
        text("Press 's' to start", width/3, height/2)
        return
    
    
    background(200, 120, 255)
    ball.update()
    paddle_one.update()
    paddle_two.update()
    ball.draw()
    paddle_one.draw()
    paddle_two.draw()
    ball.collision(paddle_one)
    ball.collision(paddle_two)
    if ball.x - ball.radius <= 0:
        score_two += 1
        ball = Ball(450, 300)
    if ball.x + ball.radius >= width:
        score_one += 1
        ball = Ball(450, 300)
    text("Right Player Score: " + str(score_one), 580, 50)
    text("Left Player Score: " + str(score_two), 40, 50)
    
    if score_one == 6:
        noLoop()
        text("The right player wins!", 300, 300)
    if score_two == 6:
        noLoop()
        text("The left player wins!", 300, 300)
    
    pass


def keyPressed():
    global paddle_one, paddle_two
    if key == 's':
        global started
        started = True
    elif key == 'e':
        paddle_one.y_speed = -6
    elif key == 'd':
        paddle_one.y_speed = 6
    elif key == CODED:
        if keyCode == UP:
            paddle_two.y_speed = -6
        elif keyCode == DOWN:
            paddle_two.y_speed = 6
       
        
       



def keyReleased():
    if key == CODED:
        paddle_two.y_speed = 0
    else:
       paddle_one.y_speed = 0 
