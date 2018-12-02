import pygame, itertools, sys
from pygame import *

# Set of colours (R,G,B)
white = (255, 255, 255)
black = (0,0,0)
light_red = (230, 0, 0)
light_green = (0, 240, 0)
light_blue = (51, 153, 255)
gray = (128, 128, 128)
green = (0, 180, 0)
red = (190, 0, 0)
blue = (0, 102, 204)
fuschia = (255,0,255)
orange = (255,69,0)

# Initialize pygame
pygame.init()
pygame.display.set_caption('Jumping Jack')
window = pygame.display.set_mode((900, 700))

# Lets play some tunes
pygame.mixer.music.load('res/music.mp3')
pygame.mixer.music.play(-1)

"""
    Function to create a button with text in it and set its colour to its light
    version when mouse is hovered on it. Also returns True when clicked on it.
"""
def button(text, colorname, x, y, w, h, tx, ty):
    color = eval(colorname)

    pygame.draw.rect(window, color, [x, y, w, h])
    display_text(text, (tx, ty), "res/SansPosterBold.ttf", "black", 40)

    # Get (x,y) position and clicked button of mouse
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    # Detect mouse hover by comparing coordinates of box and mouse point
    for i, j in itertools.product(range(x, x+w+1), range(y, y+h+1)):
        if i == mouse[0] and j == mouse[1]:
            pygame.draw.rect(window, eval("light_"+colorname), [x, y, w, h])
            display_text(text, (tx, ty), "res/SansPosterBold.ttf", "black", 40)

            if click[0]:
                return True

"""
    Function to display text on any surface, provided the co-ordinates,
    font, size
"""
def display_text(text, place, font, color, size):
    color = eval(color)
    font = pygame.font.Font(font, size)
    text_ =  font.render(text, False, color)
    text_rect = text_.get_rect()
    text_rect.center = place
    window.blit(text_, text_rect)

"""
    The main menu. Options: Play, High scores, Quit
"""
def mainmenu():
    run = True
    bg = pygame.image.load("res/bg_mainwindow.png")

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False                 # Quit when the user clicks the exit button
        window.blit(bg, (0, 0))
        play = button('Play', "green", 380, 225, 165, 60, 460, 250)
        highscore = button('High Scores', "blue", 295, 325, 330, 60, 460, 350)
        quitbutton = button('Quit', "red", 380, 425, 165, 60, 460, 450)

        if quitbutton:
            pygame.quit()
            sys.exit()
        elif play:
            gameloop()
        elif highscore:
            highscores()

        pygame.display.update()

# Set of coordinates for the platforms & destination platform in (x, y) format
platform_coord = [(291, 567), (463, 504), (571, 431), (739, 443), (382, 353), (206, 328), (66, 238), (254, 143), (419, 163), (567, 122), (636, 252)]
destcoord = (758, 89)

"""
    Function to redraw background & platforms when updating stickman
"""
def redraw():
    bg = pygame.image.load("res/bg_game.png")
    dest = pygame.image.load("res/destination.png")
    window.blit(bg, (0, 0))
    window.blit(dest, (destcoord))

    for i in platform_coord:
        platform = pygame.image.load("res/platform.png")
        window.blit(platform, (i[0], i[1]))

"""
    Function to check whether stickman is on platform or is on destination platform
"""
def platformcheck(x,y):
    onplatform=False
    win=False

    for i in platform_coord:
        if (i[1] in range(y+78, y+94)) and (x in range(i[0]-50, i[0]+80)):                      # All other platforms
            onplatform=True
            break

    if (destcoord[1] in range(y+78, y+94)) and (x in range(destcoord[0]-50, destcoord[0]+80)):  # Destination platform
        win=True

    return (onplatform, win)

"""
    Function to check if stickman is colliding with platforms
    Uses the builtin function "colliderect" which is a part of "Rect" class
"""
def collisioncheck(x,y):
    collision=False
    # Initialize rect for stickman
    stickmanrect = pygame.Rect(x,y,64,94)

    for i in range(0, len(platform_coord)):
        # Initialize rects for all platforms
        exec('platformrect'+str(i)+' = pygame.Rect('+str(platform_coord[i][0])+','+str(platform_coord[i][1])+',103,18)')
        if eval('stickmanrect.colliderect(platformrect'+str(i)+')'):
            collision = True
            break

    return collision

"""
    Function to display message and score when the user won the game
"""
def win(time):
    run = True
    gscore = score(time)
    while run:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False                 # Quit when the user clicks the exit button

        bg = pygame.image.load("res/bg_game.png")
        window.blit(bg, (0, 0))

        display_text('YOU WIN !!!', (450, 320), "res/SansPosterBold.ttf", "orange", 50)
        display_text('Your score: '+str(gscore), (450, 375), "res/SansPosterBold.ttf", "fuschia", 40)

        pygame.display.flip()

"""
    Function to calculate score based on number of seconds taken to win the game
    TODO: More efficient, algorithmic way of calculating score
"""
def score(time):
    secs = time//1000

    if secs in range(0, 20):
        score = 500
    elif secs in range(20, 30):
        score = 400
    elif secs in range(30, 40):
        score = 350
    elif secs in range(40, 50):
        score = 300
    elif secs in range(50, 60):
        score = 250
    elif secs in range(60, 70):
        score = 200
    elif secs in range(70, 80):
        score = 150
    elif secs in range(80, 90):
        score = 100
    elif secs in range(90, 100):
        score = 50
    elif secs in range(100, 120):
        score = 30
    elif secs in range(120, 150):
        score = 20
    else:
        score = 10

    # Create if doesnt exist and append the score to res/scores.txt
    scores = open("res/scores.txt","a+")

    scores.write('\n'+str(score))

    return score

"""
    Display list of high scores (top 5)
"""
def highscores():
    run=True
    while run:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False                 # Quit when the user clicks the exit button

        bg = pygame.image.load("res/bg_game.png")
        window.blit(bg, (0, 0))

        scores=[]

        # Read the scores.txt file which has all scores saved in it
        try:
            scorelist = open("res/scores.txt","r+")
        except FileNotFoundError:
            scorelist = open("res/scores.txt","a+")

        for score in scorelist:
            if len(scores)<6 and score != '\n':
                scores.append(int(score))

        # Append score '0' if score doesnt exist (min 5 scores needed)
        if len(scores)<5:
            while len(scores)<6:
                scores.append(0)

        scores.sort(reverse=True)

        display_text('HIGH SCORES:', (450, 210), "res/SansPosterBold.ttf", "orange", 50)

        y=280
        num=1
        for i in scores:
            display_text(str(num)+'. '+str(i), (450, y), "res/SansPosterBold.ttf", "fuschia", 30)
            y+=35
            num+=1

        pygame.display.flip()

"""
    Main game loop
"""
def gameloop():
    # Time elapsed since the game was initialized, in msecs
    curtime = pygame.time.get_ticks()

    # Initial position of stickman
    stickman = pygame.image.load("res/stickman_left.png")
    direction = "right"
    x,y=50,530

    run=True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run=False                 # Quit when the user clicks the exit button

        # We need only the time since we started playing the game
        time = pygame.time.get_ticks() - curtime

        # Get which key is pressed rigt now
        key = pygame.key.get_pressed()

        # Draw the background & the platforms
        redraw()
        print(mouse.get_pos())

        # Prepare animation for stickman's movement
        stickman = pygame.image.load("res/stickman_"+direction+".png")
        stickman_right = (pygame.image.load("res/stickman_right.png"), pygame.image.load("res/stickman_running_right.png"), pygame.image.load("res/stickman_jumping_right.png"))
        stickman_left = (pygame.image.load("res/stickman_left.png"), pygame.image.load("res/stickman_running_left.png"), pygame.image.load("res/stickman_jumping_left.png"))

        # Draw the stickman
        window.blit(stickman, (x,y))

        # Calculate secs and mins from msecs
        secs = str((time//1000)%60).zfill(2)
        mins = str((time//1000)//60).zfill(2)

        # Display elapsed time on the game screen
        def showtime(): display_text(mins+' : '+secs, (75, 30), "res/SansPosterBold.ttf", "orange", 30)
        showtime()

        # Animated ovement of stickman to the right
        if key[K_RIGHT]:
            if x<=760:
                for i in range(0, 3):
                    if collisioncheck(x+8,y) and not ((platformcheck(x, y))[0] or (platformcheck(x, y))[1]): break      # Stop moving if the stickman is hitting a platform
                    x+=8
                    redraw()
                    showtime()
                    window.blit(stickman_right[i], (x,y))
                    pygame.display.flip()
                direction="jumping_right"

        # Animated movement of stickman to the left
        elif key[K_LEFT]:
            if x>=50:
                for i in range(0, 3):
                    if collisioncheck(x-8,y) and not ((platformcheck(x, y))[0] or (platformcheck(x, y))[1]): break      # Stop moving if the stickman is hitting a platform
                    x-=8
                    redraw()
                    showtime()
                    window.blit(stickman_left[i], (x,y))
                    pygame.display.flip()
                direction="jumping_left"

        # Jumping of stickman
        elif key[K_UP]:
            velocity=15
            iskeyright=False
            iskeyleft=False

            for i in range(0, 29):
                jumping=True
                velocity-=1
                if collisioncheck(x, y) and not ((platformcheck(x, y))[0] or (platformcheck(x, y))[1]): break          # Stop moving if the stickman is hitting a platform
                y-=velocity

                # Check if right/left key is being pressed
                for event in pygame.event.get():
                    if event.type==KEYDOWN:
                        if event.key==K_RIGHT:
                            iskeyright = True
                        elif event.key==K_LEFT:
                            iskeyleft = True

                if x<=760 and iskeyright:   # Move right while jumping
                    direction="jumping_right"
                    if collisioncheck(x+8,y) and not ((platformcheck(x, y))[0] or (platformcheck(x, y))[1]): break      # Stop moving if the stickman is hitting a platform
                    x+=8
                elif x>=50 and iskeyleft:   # Move left while jumping
                    direction="jumping_left"
                    if collisioncheck(x-8,y) and not ((platformcheck(x, y))[0] or (platformcheck(x, y))[1]): break      # Stop moving if the stickman is hitting a platform
                    x-=8

                redraw()
                showtime()
                window.blit(stickman, (x,y))
                pygame.display.flip()

                # Stop falling if stickman lands on platform
                if ((platformcheck(x, y))[0] or (platformcheck(x, y))[1]):
                    break

        # Fall down if stickman is not on a platform
        if not ((platformcheck(x, y))[0] or (platformcheck(x, y))[1]):
            downvel=12

            while y<=520:
                falling=True
                y+=downvel
                if ((platformcheck(x, y))[0] or (platformcheck(x, y))[1]): break    # Stop falling if stickman lands on platform
                redraw()
                showtime()
                window.blit(stickman, (x,y))
                pygame.display.flip()

        if (platformcheck(x, y))[1]:    # Won when the stickman lands on destination platform
            win(time)
            break

        pygame.display.flip()

mainmenu()
pygame.quit()
