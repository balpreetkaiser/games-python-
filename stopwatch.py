te for "Stopwatch: The Game"
import simplegui

# define global variables
time = '0:00.0'
current_time = 0
hits = 0
wins = 0
in_progress = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(current_time):
    global time
    t = current_time
    time = str(t//600)+ ':' + str((t%600)//100) + str(t%100/10) + '.' + str(t%10) 
    return time
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    global in_progress
    in_progress = 1    
    timer.start()
    
def stop():
    global hits, wins, in_progress, time
    timer.stop()
    hits = hits + in_progress
    if time[-1] == '0' and in_progress:
        wins = wins + 1
    in_progress = 0
    
def reset():
    global current_time, hits, wins
    timer.stop()
    wins = 0
    hits = 0
    current_time = 0
    timer.stop()

# define event handler for timer with 0.1 sec interval
def update_timer():
    global current_time
    current_time += 1
    format(current_time)    

# define draw handler
def draw_timer(canvas):
    global current_time, wins, hits
    canvas.draw_text(format(current_time), (90,150), 50, 'Red')
    canvas.draw_text(str(wins) + '/' + str(hits) ,(250,30) , 30, 'Blue')
    
# create frame
frame = simplegui.create_frame('Stopwatch', 300, 300)
timer = simplegui.create_timer(100, update_timer)

# register event handlers
frame.set_draw_handler(draw_timer)
frame.add_button('Start', start, 100)
frame.add_button('Stop', stop, 100)
frame.add_button('Reset', reset, 100)

# start frame
frame.start()

# Please remember to review the grading rubric

