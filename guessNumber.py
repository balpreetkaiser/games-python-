# Input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random

# initialize global variables used
num_range = 100
secret_number = 0
count = 0

# helper function to start and restart the game
def new_game():
    global secret_number
    global count
    print "New Game."
    print "The range is 0 to", num_range
    secret_number = random.randrange(0, num_range)
    if num_range == 100:
        count = 7
    elif num_range ==1000:
        count = 10
    print "Number of remaining guesses is:",count
    
    


# define event handlers for control panel
def range100():
    # button that changes range to range [0,100) and restarts
    global num_range
    num_range = 100
    new_game()

def range1000():
    # button that changes range to range [0,1000) and restarts
    global num_range
    num_range= 1000
    new_game()
    
def input_guess(guess):
    global secret_number
    global count
    # main game logic goes here	
    print "The guess was", guess 
    count -= 1
    print "Number of remaining guesses is:",count

    #Code for comparing the guess with the secret number
    
   
    if int(guess) < secret_number:
        print "Higher!"
    elif int(guess) > secret_number:
        print "Lower!"
    elif int(guess) == secret_number:
        print "Correct!"
        new_game()
          
    if count == 0:
        print "Game over!"
        print "Number to guess was:", secret_number
        new_game()
    
    
    # remove this when you add your code
    pass

    
# create frame
frame = simplegui.create_frame('Guess the number', 200, 200)


# register event handlers for control elements
frame.add_button('Range 1-100', range100, 100)
frame.add_button('Range 1-1000', range1000, 100)
frame.add_input("Enter the guess", input_guess, 100)

# call new_game and start frame
new_game()
frame.start()



# always remember to check your completed program against the grading rubric

