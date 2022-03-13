import random

import pygame
import time


pygame.init()

display_width = 800
display_height = 600

# colours
black = (0, 0, 0)
white = (255, 255, 255)
darker_red = (207, 47, 47)
seaweed_green = (55, 184, 111)
neon_green = (33, 255, 70)
neon_red = (255 ,38, 38)

car_width = 73

# create game screen size
gameDisplay = pygame.display.set_mode((display_width, display_height))
# set name of the game, displayed in top left corner of the 'navbar'
pygame.display.set_caption('Ocean Helper')
clock = pygame.time.Clock()

# loading images for use later
carImg = pygame.image.load('./images/racecar.png')
cityImg = pygame.image.load('./images/city2.jpg')
def background():
    scaled_img = pygame.transform.scale(cityImg, (display_width, display_height))
    gameDisplay.blit(scaled_img, (0, 0))

def car(x, y):
    gameDisplay.blit(carImg, (x, y))


def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


def game_over_message(text):
    large_text = pygame.font.Font('freesansbold.ttf', 50)
    TextSurf, TextRect = text_objects(text, large_text)
    TextRect.center = ((display_width / 2), (display_height / 2))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(2)
    game_loop()


def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])


def game_over():
    game_over_message("Game Over!")


def display_score(score):
    font = pygame.font.Font('freesansbold.ttf', 25)
    text = font.render("Avoided: " + str(score), True, black)
    gameDisplay.blit(text, (0, 0))
    pygame.display.update()


def game_intro():
    intro = True
    # intiating the game intro loop
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        # creating title screen
        gameDisplay.fill(white)
        large_text = pygame.font.Font('freesansbold.ttf', 60)
        TextSurf, TextRect = text_objects("Ocean Helper", large_text)
        TextRect.center = ((display_width / 2), (display_height / 5))
        gameDisplay.blit(TextSurf, TextRect)

        #adding some rectangles for buttons later
        pygame.draw.rect(gameDisplay, seaweed_green, (150, 350, 100, 50), 0, 10)
        pygame.draw.rect(gameDisplay, darker_red, (550, 350, 100, 50), 0, 10)

        # get coordinate of user's current cursor location, returned as a tuple (x, y)
        mouse = pygame.mouse.get_pos()

        # if cursor is inside the button, redraw a button over the button with bright colour
        if 150 + 100 > mouse[0] > 150 and 350 + 50 > mouse[1] > 350:
            pygame.draw.rect(gameDisplay, neon_green, (150, 350, 100, 50), 0, 10)
        if 550 + 100 > mouse[0] > 550 and 350 + 50 > mouse[1] > 350:
            pygame.draw.rect(gameDisplay, neon_red, (550, 350, 100, 50), 0, 10)


        pygame.display.update()
        clock.tick(15)


def game_loop():
    x = (display_width * 0.45)
    y = (display_height * 0.8)

    x_change = 0
    y_change = 0

    gameExit = False

    # parameters of the obstacles
    thing_start_x = random.randrange(0, display_width)
    thing_start_y = -600
    thing_speed = 6
    thing_width = 100
    thing_height = 100

    #intializing score
    avoided = 0

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            # when left, right, up, down key are pressed, get x/y change
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5
                if event.key == pygame.K_UP:
                    y_change = -5
                if event.key == pygame.K_DOWN:
                    y_change = 5
            # when the left, right, up, down key are not pressed anymore, stop the thing from moving
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change = 0
        # increasing and decreasing thing's y and x to mimic movement
        x += x_change
        y += y_change
        background()
        # draw the obstacle with the inputted parameters
        things(thing_start_x, thing_start_y, thing_width, thing_height, black)
        # obstacle moves down 6 pixels every frame
        thing_start_y += thing_speed
        car(x, y)
        display_score(avoided)

        if thing_start_y > display_height:
            thing_start_y = 0 - thing_height
            thing_start_x = random.randrange(0, display_width)
        # checks if the obstacle passed over character
        if y < thing_start_y + thing_height:
            # checks if the the x point of the obstacle crosses the character
            if x > thing_start_x and x < thing_start_x + thing_width or x + car_width > thing_start_x and x + car_width < thing_start_x + thing_width:
                game_over()

        if thing_start_y > display_height:
            thing_start_y = 0 - thing_height
            thing_start_x = random.randrange(0, display_width)
            avoided += 1
            thing_speed += 1
            thing_width += (avoided * 1.2)

        # keeps character inside of the screen
        if x > display_width - car_width:
            x = display_width - car_width
            # game_over()
        if x < 0:
            x = 0
            # game_over()
        if y < 0:
            y = 0
            # game_over()
        if y > display_height - car_width:
            y = display_height - car_width
            # game_over()
        # updates the screen after each event
        pygame.display.update()
        # frames the game is running at
        clock.tick(60)

game_intro()
game_loop()
pygame.quit()
quit()