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
    game_screen()
    player_one_win_screen()
    player_two_win_screen()

def game_screen():
    if mode == 0:
        fill(255)
        strokeWeight(3)
        rect(100, 300, 100, 110)
        rect(1000,300,100, 110)
        
        strokeWeight(5)
        rect(300,300,200,200)
        rect(700,300,200,200)
        
        #load images in respective positions    
        fill(0)
        textSize(50)
        text("ROCK PAPER SCISSORS", 350, 100)
        textSize(25)
        text("Pick your play",520,650)
        text("VS",575,410)
        text("points",100,460)
        text("points",1000, 460)
        image_one = loadImage("rock.png")
        image(image_one, 130, 730)
        image_two = loadImage("paper.png")
        image(image_two, 450, 730)
        image_three = loadImage("scissors.png")
        image(image_three, 750, 730)
        
def player_one_win_screen():
    if mode == 1:
        restart()
        background(255)
        textSize(75)
        fill(0)
        text("YOU HAVE WON! PLAYER ONE!", 25, 450)
        textSize(50)
        fill(255)
        rect(100, 1000, 400, 50)
        fill(0)
        text("RETURN", 200, 1045)
        
def player_two_win_screen():
    if mode == 2:
        restart()
        background(255)
        textSize(70)
        fill(0)
        text("COMPUTER HAS WON! PLAYER TWO", 0, 450)
        textSize(50)
        fill(255)
        rect(100, 1000, 400, 50)
        fill(0)
        text("RETURN", 200, 1045)
        
        
        
#restart function to set score and tracking variables to 0
def restart():
    global player_one_selection
    global player_two_selection
    global player_one_score
    global player_two_score
    
    player_one_selection = 0
    player_two_selection = 0
    player_one_score = 0
    player_two_score = 0
    
        

def mousePressed():
    print(mouseX, mouseY)
