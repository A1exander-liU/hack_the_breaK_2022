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
sea_floor = pygame.image.load('./images/seafloor.jpg')
sea_turtle = pygame.image.load('./images/sea_turtle_2-removebg-preview.png')
underwater = pygame.image.load('./images/underwater.jpg')
garbage = pygame.image.load('./images/garbage-removebg-preview.png')

def background(img):
    scaled_img = pygame.transform.scale(img, (display_width, display_height))
    gameDisplay.blit(scaled_img, (0, 0))

def draw_image(x_location, y_location, img):
    # use this for static images
    gameDisplay.blit(img, (x_location, y_location))


def turtle(x_location, y_location):
    # for character controlled image
    sea_turtle_scaled = pygame.transform.scale(sea_turtle, (100, 100))
    gameDisplay.blit(sea_turtle_scaled, (x_location, y_location))


def garbage_img(x_location, y_location):
    garbage_scaled = pygame.transform.scale(garbage, (100, 100))
    gameDisplay.blit(garbage_scaled, (x_location, y_location))


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
    home_screen()


def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])


def game_over():
    game_over_message("Game Over!")


def display_score(score):
    font = pygame.font.Font('freesansbold.ttf', 25)
    text = font.render("Avoided: " + str(score), True, black)
    gameDisplay.blit(text, (0, 0))
    pygame.display.update()


def to_home():
    time.sleep(0.5)
    home_screen()


def make_button(x_location, y_location, button_width, button_height, not_hover_colour, hovered_colour, button_info):
    mouse = pygame.mouse.get_pos()
    mouse_clicked = pygame.mouse.get_pressed()

    if x_location + button_width > mouse[0] > x_location and y_location + button_height > mouse[1] > y_location:
        pygame.draw.rect(gameDisplay, hovered_colour, (x_location, y_location, button_width, button_height), 0, 10)
        if mouse_clicked[0] == 1 and to_home != None and button_info == "Start":
            to_home()
        if mouse_clicked[0] == 1 and to_home != None and button_info == "Exit":
            pygame.quit()
        if mouse_clicked[0] == 1 and game_intro != None and button_info == "Back":
            game_intro()
        if mouse_clicked[0] == 1 and game_loop != None and button_info == "Garbage Collector":
            game_loop()
    else:
        pygame.draw.rect(gameDisplay, not_hover_colour, (x_location, y_location, button_width, button_height),0 ,10)
    button_text = pygame.font.Font("freesansbold.ttf", 15)
    textSurf, textRect = text_objects(button_info, button_text)
    textRect.center = ((x_location + (button_width / 2)), (y_location + (button_height / 2)))
    gameDisplay.blit(textSurf, textRect)


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

        # make button
        make_button(150, 350, 100, 50, seaweed_green, neon_green, "Start")
        make_button(550, 350, 100, 50, darker_red, neon_red, "Exit")

        pygame.display.update()
        clock.tick(15)


def home_screen():
    at_home = True
    while at_home:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        background(sea_floor)

        draw_image(300, 100, sea_turtle)

        make_button(100, 450, 150, 50, seaweed_green, neon_green, "Garbage Collector")
        make_button(550, 450, 150, 50, seaweed_green, neon_green, "Ocean Quiz")
        make_button(350, 450, 100, 50, seaweed_green, neon_green, "Back")

        # updates the screen after each event
        pygame.display.update()
        # frames the game is running at
        clock.tick(60)

def game_loop():
    x = (display_width * 0.45)
    y = (display_height * 0.8)

    x_change = 0
    y_change = 0

    gameExit = False

    # parameters of the obstacles
    starting_x = random.randrange(0, display_width)
    starting_y = -600
    speed = 6
    width = 100
    height = 100

    #intializing score
    avoided = 0

    turtle_width = 70

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
        background(underwater)
        # draw the obstacle with the inputted parameters
        # things(thing_start_x, thing_start_y, thing_width, thing_height, black)
        garbage_img(starting_x, starting_y)
        # scaled_img = pygame.transform.scale(garbage, (100, 100))
        # draw_image(50, 50, scaled_img)
        turtle(x, y)
        # obstacle moves down 6 pixels every frame
        starting_y += speed
        # draw_image(x, y, carImg)
        display_score(avoided)

        if starting_y > display_height:
            starting_y = 0 - height
            starting_x = random.randrange(0, display_width)
        # checks if the obstacle passed over character
        if y < starting_y + height:
            # checks if the the x point of the obstacle crosses the character
            if x > starting_x and x < starting_x + width or x + turtle_width > starting_x and x + turtle_width < starting_x + width:
                game_over()

        if starting_y > display_height:
            starting_y = 0 - height
            starting_x = random.randrange(0, display_width)
            avoided += 1
            speed += 1
            width += (avoided * 1.2)

        # keeps character inside of the screen
        if x > display_width - turtle_width:
            x = display_width - turtle_width
            # game_over()
        if x < 0:
            x = 0
            # game_over()
        if y < 0:
            y = 0
            # game_over()
        if y > display_height - turtle_width:
            y = display_height - turtle_width
            # game_over()
        # updates the screen after each event
        pygame.display.update()
        # frames the game is running at
        clock.tick(60)

game_intro()
home_screen()
game_loop()
pygame.quit()
quit()