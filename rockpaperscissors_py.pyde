import random
player_one_selection = 0
player_two_selection = 0
player_one_picked = None
player_one_score = 0
player_two_score = 0
mode = 0

def setup():
    global player_one_selection
    global player_two_selection
    global player_one_picked
    global player_one_score
    global player_two_score
    global mode
    
    size(1200, 1200)
    
def draw():
    global player_one_selection
    global player_one_picked
    global mode
    
    background(255)
    

def game_screen():
    if mode == 0:
        fill(255)
        strokeWeight(5)
        rect(100, 100, 100, 110)
