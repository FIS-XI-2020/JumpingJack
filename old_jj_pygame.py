"""
    JUMPING JACK GAME
    USING PYGAME
"""

import pygame, random, sys, itertools, time, threading
from pygame import *

# Colours (R,G,B)
white = (255, 255, 255)
black = (0,0,0)
light_red = (230, 0, 0)
light_green = (0, 240, 0)
light_blue = (51, 153, 255)
gray = (128, 128, 128)
green = (0, 180, 0)
red = (190, 0, 0)
blue = (0, 102, 204)

class Stickman(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        self.images = ["stickman_right", "stickman_running_right", "stickman_jumping_right"]

        self.index = 0

        self.image = pygame.image.load("res/%s.png" % self.images[self.index])

       # self.image = pygame.image.load("res/stickman_right.png")

        self.rect = self.image.get_rect()

    def update(self):
        self.index += 1
        if self.index >= len(self.images):
            self.index = 0
        self.image = pygame.image.load("res/%s.png" % self.images[self.index])

    def move_right(self):
        self.rect.x += 10
        self.update()
            
class Platforms(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        self.image = pygame.image.load("res/platform.png")

        self.rect = self.image.get_rect()

class Obstacles(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        self.image = pygame.image.load("res/obstacle.png")

        self.rect = self.image.get_rect()

# Lets roll
pygame.init()
screen_width = 900
screen_height = 700
screen = pygame.display.set_mode([screen_width, screen_height])

# Sprite groups
stickman_group = pygame.sprite.Group()
platforms_list = pygame.sprite.Group()
obstacles_list = pygame.sprite.Group()
all_sprites_list = pygame.sprite.Group()

# Draw the platforms
platform_coords = []

while len(platform_coords)<2:
    #platform = Platforms()
    
    px = random.randint(20, 800)
    py = random.randint(30, 550)

    print(platform_coords)

    if len(platform_coords)>=1:
        for i in platform_coords:
            if abs(i[0]-px) in range(40, 90) and (abs(i[1]-py) in range(30, 80)):
                valid = True
            else:
                valid = False
                #break
        if valid:
            platform_coords.append((px,py))
    else:
        platform_coords.append((px,py))


for i in platform_coords:
    platform = Platforms()
    platform.rect.x = i[0]
    platform.rect.y = i[1]

    platforms_list.add(platform)
    all_sprites_list.add(platform)

stickman = Stickman()
stickman.rect.x = 50
stickman.rect.y = 530
stickman_group.add(stickman)
all_sprites_list.add(stickman)

clock = pygame.time.Clock()

"""
    Function to create a button with text in it and set its colour to its light
    version when mouse is hovered on it. Also returns True when clicked on it.
"""
def button(text, colorname, x, y, w, h, tx, ty):
    color = eval(colorname)
    
    pygame.draw.rect(screen, color, [x, y, w, h])
    display_text(text, (tx, ty), "res/SansPosterBold.ttf", 40)

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    # Detect mouse hover by comparing coordinates of box and mouse point
    for i, j in itertools.product(range(x, x+w+1), range(y, y+h+1)):
        if i == mouse[0] and j == mouse[1]:
            pygame.draw.rect(screen, eval("light_"+colorname), [x, y, w, h])
            display_text(text, (tx, ty), "res/SansPosterBold.ttf", 40)

            if click[0]:
                return True
        
"""
    Function to display text on any surface, provided the co-ordinates,
    font, size etc
"""
def display_text(text, place, font, size):
    font = pygame.font.Font(font, size)
    text_ =  font.render(text, True, black)
    text_rect = text_.get_rect()
    text_rect.center = place
    screen.blit(text_, text_rect)

"""
    The main menu. Options: Play, High scores, Quit
    TODO: Playing instructions
"""
def mainmenu():
    run = True
    bg = pygame.image.load("res/bg_mainwindow.png")
    
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        screen.blit(bg, (0, 0))
        play = button('Play', "green", 380, 225, 165, 60, 460, 250)
        highscores = button('High Scores', "blue", 295, 325, 330, 60, 460, 350)
        quitbutton = button('Quit', "red", 380, 425, 165, 60, 460, 450)

        if quitbutton:
            pygame.quit()
            sys.exit()
        elif play:
            gameloop()

        pygame.display.update()
        clock.tick(15)

"""
    MAIN LOOP
"""
def gameloop():
    run = True

    while run:
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                run = False

        bg = pygame.image.load("res/bg_game.png")
        screen.blit(bg, (0, 0))

        all_sprites_list.draw(screen)

        pygame.display.flip()

        key = pygame.key.get_pressed()
        
        if key[K_RIGHT]:
            stickman.move_right()

        all_sprites_list.update()
        
        clock.tick(60)

mainmenu()
pygame.quit()
