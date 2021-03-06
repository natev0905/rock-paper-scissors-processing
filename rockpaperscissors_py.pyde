import random

#set variables
player_one_selection = 0
player_two_selection = 0
player_one_picked = None
player_one_score = 0
player_two_score = 0
mode = 0

#create screen
def setup():
    global player_one_selection
    global player_two_selection
    global player_one_picked
    global player_one_score
    global player_two_score
    global mode
    
    size(1200, 1200)

    #main function to run program    
def draw():
    global player_one_selection
    global player_one_picked
    global mode
    
    background(255)
    game_screen()
    player_1_score()
    player_2_score()
    player_2_selection()
    player_one_win_screen()
    player_two_win_screen()
    
    if player_one_selection == 1:
        image_one = loadImage("rock.png")
        image(image_one, 300, 300)
        
    elif player_one_selection == 2:
        image_two = loadImage("paper.png")
        image(image_two, 300, 300)
    
    elif player_one_selection == 3:
        image_three = loadImage("scissors.png")
        image(image_three, 300, 300)
        
#sets up game screen and score boxes
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

#displays if player 1 wins        
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

        
# displays if computer wins        
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

        
#function for the computer selection and where to display its selection        
def player_2_selection():
    global player_two_selection
    global player_one_picked
    
    if player_two_selection == 1:
        image_one = loadImage("rock.png")
        image(image_one, 700, 300)
    
    elif player_two_selection == 2:
        image_two = loadImage("paper.png")
        image(image_two, 700, 300)
        
    elif player_two_selection == 3:
        image_three = loadImage("scissors.png")
        image(image_three, 700, 300)

        
#function to determine winner        
def winner():
    global player_one_score
    global player_two_score
    global player_two_selection
    global player_one_picked
    global mode
    
    
    if player_one_selection == 1 and player_two_selection == 2:
        player_two_score += 1
        player_one_picked = False
    
    if player_one_selection == 3 and player_two_selection == 3:
        player_two_score += 1
        player_one_picked = False
    
    if player_one_selection == 3 and player_two_selection == 1:
        player_two_score += 1
        player_one_picked = False
        
    
    if player_one_selection == 2 and player_two_selection == 1:
        player_one_score += 1
        player_one_picked = False
    
    if player_one_selection == 3 and player_two_selection == 2:
        player_one_score += 1
        player_one_picked = False
    
    if player_one_selection == 1 and player_two_selection == 3:
        player_one_score += 1
        player_one_picked = False
        
    #marks game is over and switches to win screen
    if player_one_score >= 3:
        mode = 1
    if player_two_score >= 3:
        mode = 2

#function to keep player one score updated after each round
def player_1_score():
    fill(0)
    textSize(70)
    text(player_one_score, 130, 380)    

#function to keep computer score updated after each round
def player_2_score():
    fill(0)
    textSize(70)
    text(player_two_score, 1030, 380)
        
        
        
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
    
 
#all of the components that involve clicking are setup here - images, selections, return from win screen to restart
def mousePressed():
    print(mouseX, mouseY)
    global player_one_selection, player_two_selection, mode
    
    if mouseX > 130 and mouseY > 730 and mouseX < 330 and mouseY < 926:
        player_one_selection = 1
        player_two_selection = random.randint(1,3)
        winner()
    
    if mouseX > 447 and mouseY > 729 and mouseX < 647 and mouseY < 929:
        player_one_selection = 2
        player_two_selection = random.randint(1,3)
        winner()
    
    if mouseX > 753 and mouseY > 728 and mouseX < 952 and mouseY < 929:
        player_one_selection = 3
        player_two_selection = random.randint(1,3)
        winner()
        
        
    if mouseX > 103 and mouseY > 999 and mouseX < 502 and mouseY < 1051 and (mode == 1 or mode ==2):
        mode = 0
    

    
    
        
    


    
   
