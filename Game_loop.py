# importing modules

import pygame
import math
import random
from Exit_screen import game_over
from pygame import mixer

# initialise pygame
pygame.init()

#adding background music



#adding screen and background image
screen = pygame.display.set_mode((800, 600))
background = pygame.image.load('back.png')


# Adding caption to screen
pygame.display.set_caption("space invaders")
icon = pygame.image.load(r'spaceship.png')
pygame.display.set_icon(icon)

# initial score
score = 0


# player constants and image

playerimg = pygame.image.load(r'playerimg.png')
playerx = 370
playery = 480
player_hzt = 0
player_vert = 0


# enemiy empty lists and constants

q=1
x = " "
enemyimg = []
alienx = []
alieny = []
vel_x = []
vel_y = []
x_speed = 0.9
y_speed = 5


# bullets image and constants

bulletimg = pygame.image.load(r'bullet1.png')
bulletx = 0
bullety = 480
bulletx_change = 0
bullety_change = 10 # speed at which bullets y coordinate changes i.e speed of bullet
bullet_state = "ready"

# bringing player to screen
def player(x, y):
    screen.blit(playerimg, (playerx, playery))  # blit function used to draw on screen

# bringing player to screen
def enemy(x, y, i):
    screen.blit(enemyimg[i] ,(x, y) )

# bringing bullets to screen
def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletimg, (x + 16, y + 10))


# collision logic
def is_collision(bulletx, bullety, alienx, alieny):
    distance = math.sqrt((math.pow(bulletx - alienx, 2)) + (math.pow(bullety - alieny, 2)))
    if distance < 28:
        return True
    else:
        return False


# enemy collision image
v = 1
m = 0
n = 0

# GAME LOOP : every in game related action should be in the game loop
running = True

while running:

    screen.fill((0, 0, 0))

    screen.blit(background, (0, 0))
    # screen.blit(text, text_rect)



    # CREATING ENEMIES
    num_of_enemies = q
    colm = 5

    for i in range(num_of_enemies):
        for j in range(colm):
            if j == 0:
                enemyimg.append(pygame.image.load('enemyimg.png'))
            if j == 1:
                enemyimg.append(pygame.image.load('en1_2.png'))
            if j == 2:
                enemyimg.append(pygame.image.load('en2_2.png'))
            else:
                enemyimg.append(pygame.image.load('en3_2.png'))
            alienx.append(140 + j * 90)
            alieny.append(100 + i * 70)
            vel_x.append(2)
            vel_y.append(40)



    # CODE FOR EXITTING WINDOW

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

            # Making buttons for player movement

        if event.type == pygame.KEYDOWN  :
            if event.key == pygame.K_UP or event.key == pygame.K_w :
                player_vert = -3
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                player_vert = 3
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                player_hzt = -3
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                player_hzt = 3
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bulletx = playerx
                    bullety = playery
                    fire_bullet(bulletx, bullety)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_a or event.key == pygame.K_d:
                player_hzt = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN  or event.key == pygame.K_w  or event.key == pygame.K_s:
                player_vert = 0


    # Ensuring enemy inside screen

    playerx = playerx + player_hzt
    if playerx <= 0:
        playerx = 0
    elif playerx >= 736:
        playerx = 736
    playery = playery + player_vert
    if playery <= 0:
        playery = 0
    elif playery >= 536:
        playery = 536

    # enemy movements

    for i in range(num_of_enemies):
        alienx[i] = alienx[i] + vel_x[i]
        if alienx[i] <= 0:
            vel_x[i] = x_speed
            alieny[i] = vel_y[i] + alieny[i]
        elif alienx[i] >= 736:
            vel_x[i] = -x_speed
            alieny[i] = vel_y[i] + alieny[i]


        # Collision of enemy and bullet

        collision = is_collision(bulletx, bullety, alienx[i], alieny[i])
        if collision:
            bullety = 480
            bullet_state = "ready"

            v = 3
            m = alienx[i]
            n = alieny[i]

            # sound for collision
            mixer.init()
            mixer.music.load("coll.wav")
            mixer.music.play(1)

            # score calculation
            score = score + 1
            x = str(int(score))


            print(x)
            # global y
            y = int(x)
            alienx[i] = random.randint(0, 730)
            alieny[i] = random.randint(50, 150)
        if alieny == 0:
            running = False
        enemy(alienx[i], alieny[i], i)

    # enemy image collision

    if v > 2 and v < 20:
        colli_image = pygame.image.load("explosionpurple.png")
        screen.blit(colli_image, (m, n))
        v += 1



    # bullet movement

    if bullety <= 0:
        bullety = 480
        bullet_state = "ready"
    if bullet_state == "fire":
        fire_bullet(bulletx, bullety)
        bullety = bullety - bullety_change


    # SCORE AND ENEMY level DEFINING

    if score > 1:
        x_speed = 1
        q =2
        if score > 3:
            q = 4
            if score > 9:
                x_speed = 1.5
                q = 6
                if score > 12:
                    q =10
                    if score > 15:
                        x_speed = 1.7
                        if score > 18:
                            x_speed = 3

    # game over window

    if score == 20:
        game_over()
        
        

    font = pygame.font.SysFont("Arial", 30)
    text = font.render("score:" + x, True, (240,240,240) )  # add parameteres  , requires at least 3 parameters
    text_rect = text.get_rect()
    text_rect.center = (60, 30)
    screen.blit(text, text_rect )


    # updating screen

    player(playerx, playery)
    pygame.display.update()



