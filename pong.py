mplementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = 0
RIGHT = 1

paddle1_pos = PAD_HEIGHT
paddle2_pos = PAD_HEIGHT
paddle1_vel =0
paddle2_vel =0
ball_pos = [ WIDTH / 2 , HEIGHT / 2 ]
ball_vel = [ 0 , 0 ]
score1 = 0
score2 = 0

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [ WIDTH /2 , HEIGHT / 2 ] # Place the ball in the centre
    if direction == 0:
        ball_vel[0] = -(random.randrange(120, 200)/60)
        ball_vel[1] = -(random.randrange(60, 180))/60
    elif direction == 1:
        ball_vel[0] = random.randrange(120, 200)/60
        ball_vel[1] = -(random.randrange(60, 180)/60)
        
   

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    direction = random.choice([1 , 0]) #chose the direction to move the ball in 
    spawn_ball(direction)
    

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel, paddle1_vel, paddle2_vel
 
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    
    # Ball collides and reflects off the walls
    if ((ball_pos[0] <= BALL_RADIUS + PAD_WIDTH) and (ball_pos[1] >= paddle1_pos - PAD_HEIGHT) and (ball_pos[1] <= paddle1_pos)):
        ball_vel[0] = -(ball_vel[0] + ( 0.1 * ball_vel[0]))
    elif (ball_pos[0] >= ((WIDTH-1) - PAD_WIDTH - BALL_RADIUS) and (ball_pos[1] >= paddle2_pos - PAD_HEIGHT) and (ball_pos[1] <= paddle2_pos)):
        ball_vel[0] = -(ball_vel[0] + ( 0.1 * ball_vel[0]))
    elif ball_pos[0] <= (BALL_RADIUS + PAD_WIDTH):
        score2 += 1
        spawn_ball(RIGHT)
        
    elif  ball_pos[0] >= ((WIDTH-1) - PAD_WIDTH - BALL_RADIUS):
        score1 += 1
        spawn_ball(LEFT)
        
    elif ball_pos[1] <= BALL_RADIUS or ball_pos[1] >= (HEIGHT-1) - BALL_RADIUS:
        ball_vel[1] = -ball_vel[1]
    
    
    # draw ball
    canvas.draw_circle( (ball_pos[0], ball_pos[1]) , BALL_RADIUS , 2 , 'White' , 'Red' )    
    
    
    # update paddle1's vertical position, keep paddle on the screen
    if paddle1_pos >= 80 and paddle1_pos <= 400:
        if paddle1_pos == 83 and paddle1_vel == -3:
            pass
        elif paddle1_pos == 398 and paddle1_vel == 3:
            pass
        else:
            paddle1_pos += paddle1_vel
            
    # update paddle2's vertical position, keep paddle on the screen
    if paddle2_pos >= 80 and paddle2_pos <= 400:
        if paddle2_pos == 83 and paddle2_vel == -3:
            pass
        elif paddle2_pos == 398 and paddle2_vel == 3:
            pass
        else:
            paddle2_pos += paddle2_vel
    
    
    
    # draw paddles
    canvas.draw_line((4,paddle1_pos - PAD_HEIGHT), (4,paddle1_pos), PAD_WIDTH, 'White') #left paddle
    canvas.draw_line(((WIDTH - PAD_WIDTH + 4), paddle2_pos - PAD_HEIGHT) ,((WIDTH - PAD_WIDTH +4), paddle2_pos), PAD_WIDTH, 'White') #right paddle
    
    # draw scores
    canvas.draw_text(str(score1) , (250, 100), 50, 'Aqua')
    canvas.draw_text(str(score2) , (320, 100), 50, 'Aqua')
    
#Keydown event handler
def keydown(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP['down']:
        paddle2_vel = 3
    elif key == simplegui.KEY_MAP['up']:
        paddle2_vel = -3
    if key == simplegui.KEY_MAP['w']:
        paddle1_vel = -3
    elif key == simplegui.KEY_MAP['s']:
        paddle1_vel = 3
        

        
#keyup event handler
def keyup(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP['down']:
        paddle2_vel = 0
    elif key == simplegui.KEY_MAP['up']:
        paddle2_vel = 0
    if key == simplegui.KEY_MAP['w']:
        paddle1_vel = 0
    elif key == simplegui.KEY_MAP['s']:
        paddle1_vel = 0

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)


# start frame
new_game()
frame.start()

