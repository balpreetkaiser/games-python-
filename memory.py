mplementation of card game - Memory

import simplegui
import random
# implementation of card game - Memory

import simplegui
import random

list1 = [0, 1, 2, 3, 4, 5, 6, 7]
list1.extend(list1)
#print list1
random.shuffle(list1)
#print list1
CARD_WIDTH = 50
exposed = [False] * 16
#print exposed
mouse_pos = [0, 0]
card_num = 0
state = 0
open1 =0
open2 = 0
turns = 0

# helper function to initialize globals
def new_game():
    global exposed, list1, turns 
    turns = 0
    label.set_text("Moves = " + str(turns))
    random.shuffle(list1)
    exposed = [False] * 16
    state = 0
    
        
# define event handlers
def mouseclick(pos):
    global mouse_pos, card_number, state, open1, open2, turns,list1
    # add game state logic here
    #print list(pos)
    mouse_pos = list(pos)
    #print mouse_position[0]
    card_num = mouse_pos[0] / 50
    #print card_number
    if exposed[card_num] == True:
        pass
    else:
        if state == 0:
            exposed[card_num] = True
            open1 = card_num
            state = 1
            turns += 1
            label.set_text("Moves = " + str(turns))
        elif state == 1:
            exposed[card_num] = True
            open2 = card_num 
            state = 2
        elif state == 2:
            if list1[open1] == list1[open2]:
                pass
            else:
                exposed[open1] = False
                exposed[open2] = False
            exposed[card_num] = True
            open1 = card_num
            open2 = 0
            state = 1
            turns += 1
    label.set_text("Moves = " + str(turns))            
        
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    i = 0
    global card_num 
    j = card_num
    while i <= 15:
        canvas.draw_polygon([[(i * 50), 0], [((i + 1) * 50), 0], [((i + 1) * 50), 100], [(i * 50), 100]], 1, 'White')
        i += 1
        
    for s in list1:
        if exposed[j] == False:
            canvas.draw_polygon([[(j * 50), 0], [((j + 1) * 50), 0], [((j + 1) * 50), 100], [(j * 50), 100]], 1, 'White', 'Green')
        else:
            canvas.draw_text(str(s), (( (CARD_WIDTH/10) + (j * CARD_WIDTH)) , 80), 80, 'Red')
        j += 1


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric
