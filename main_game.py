import random
import pygame
import time

pygame.init()

# setting screen size
display_width = 800
display_height = 600

# colours
black = (0, 0, 0)
white = (255, 255, 255)
darker_red = (207, 47, 47)
seaweed_green = (55, 184, 111)
neon_green = (33, 255, 70)
neon_red = (255 ,38, 38)

# create game screen
gameDisplay = pygame.display.set_mode((display_width, display_height))
# set name of the game, displayed in top left corner of the 'navbar'
pygame.display.set_caption('Ocean Helper')
clock = pygame.time.Clock()

# loading images for use later
sea_floor = pygame.image.load('./images/sea_floor_no_watermark.jpg')
sea_turtle = pygame.image.load('./images/sea_turtle_2-removebg-preview.png')
underwater = pygame.image.load('./images/underwater.jpg')
garbage = pygame.image.load('./images/garbage-removebg-preview.png')

def background(img):
    # scale image to screen size and draw it on screen
    scaled_img = pygame.transform.scale(img, (display_width, display_height))
    gameDisplay.blit(scaled_img, (0, 0))


def draw_image(x_location, y_location, img):
    # used for static images
    gameDisplay.blit(img, (x_location, y_location))


def turtle(x_location, y_location):
    # for character controlled image
    sea_turtle_scaled = pygame.transform.scale(sea_turtle, (100, 100))
    gameDisplay.blit(sea_turtle_scaled, (x_location, y_location))


def garbage_img(x_location, y_location):
    # automatically moving item to collect
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
    make_button(350, 400, 100, 50, seaweed_green, neon_green, "Return")
    pygame.display.update()



def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])


def game_finished():
    end_screen()


def display_score(score):
    font = pygame.font.Font('freesansbold.ttf', 20)
    text = font.render("Collected: " + str(score), True, black)
    gameDisplay.blit(text, (0, 0))
    pygame.display.update()


def to_home():
    time.sleep(0.5)
    home_screen()


def make_button(x_location, y_location, button_width, button_height, not_hover_colour, hovered_colour, button_info):
    mouse = pygame.mouse.get_pos()
    mouse_clicked = pygame.mouse.get_pressed()

    # checking if they clicked the right button, then run the other loop
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
        if mouse_clicked[0] == 1 and to_home != None and button_info == "Return":
            home_screen()
        if mouse_clicked[0] == 1 and game_loop != None and button_info == "Again":
            time.sleep(0.5)
            game_loop()
        if mouse_clicked[0] == 1 and quiz_game != None and button_info == "Ocean Quiz":
            quiz_game()
    else:
        pygame.draw.rect(gameDisplay, not_hover_colour, (x_location, y_location, button_width, button_height),0 ,10)
    # draw text on the button
    button_text = pygame.font.Font("freesansbold.ttf", 15)
    textSurf, textRect = text_objects(button_info, button_text)
    textRect.center = ((x_location + (button_width / 2)), (y_location + (button_height / 2)))
    gameDisplay.blit(textSurf, textRect)


def display_timer(time_left):
    font = pygame.font.Font('freesansbold.ttf', 20)
    text = font.render("Time left: " + str(time_left), True, black)
    gameDisplay.blit(text, (670, 0))
    pygame.display.update()


def game_intro():
    intro = True
    # initiating the game intro loop
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        # creating title screen
        background(sea_floor)
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

        draw_image(300, 0, sea_turtle)

        make_button(100, 450, 150, 50, seaweed_green, neon_green, "Garbage Collector")
        make_button(550, 450, 150, 50, seaweed_green, neon_green, "Ocean Quiz")
        make_button(350, 450, 100, 50, seaweed_green, neon_green, "Back")

        # updates the screen after each event
        pygame.display.update()
        # frames the game is running at
        clock.tick(60)


def game_loop():
    milliseconds = 0
    seconds = 20

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
    collected = 0

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
        # increasing and decreasing character's y and x to mimic movement
        x += x_change
        y += y_change
        # setting background
        background(underwater)
        # initializing garbage img
        garbage_img(starting_x, starting_y)
        # initializing character img
        turtle(x, y)
        # obstacle moves down 6 pixels every frame
        starting_y += speed
        # uses collected counter and display current collected garbage amount
        display_score(collected)

        if starting_y > display_height:
            starting_y = 0 - height
            starting_x = random.randrange(0, display_width)
        # checks if the obstacle passed over character
        if y < starting_y + height:
            # checks if the x point of the obstacle crosses the character
            if x > starting_x and x < starting_x + width or x + turtle_width > starting_x and x + turtle_width < starting_x + width:
                # when garbage is collected move the character back up back to top
                starting_y = 0 - height
                starting_x = random.randrange(0, display_width)
                speed += 0.3 # increases speed of the garbage everytime you collect one
                collected += 1 # when garbage touches you, add 1 to collected counter

        # keeps character inside the screen
        if x > display_width - turtle_width:
            x = display_width - turtle_width
        if x < 0:
            x = 0
        if y < 0:
            y = 0
        if y > display_height - turtle_width:
            y = display_height - turtle_width

        # 1000 milliseconds in 1 second
        if milliseconds > 1000:
            seconds -= 1
            # reset the milliseconds back to 0 to count the next second
            milliseconds -= 1000
        # if 20 seconds has passed stop the collection minigame
        # display game timer
        display_timer(seconds)
        if seconds == 0:
            game_finished()

        # updates the screen after each event
        pygame.display.update()
        # frames the game is running at

        # counts number of milliseconds passed in a 60pfs game
        milliseconds += clock.tick_busy_loop(60)


def quiz_game():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        background(underwater)
        question_text = pygame.font.Font('freesansbold.ttf', 20)
        TextSurf, TextRect = text_objects("How much plastic waste is in the oceans?", question_text)
        TextRect.center = ((display_width / 2), (display_height / 5))
        gameDisplay.blit(TextSurf, TextRect)

        make_button(150, 250, 200, 50, seaweed_green, neon_green, "5.25 trillion tonnes")
        make_button(450, 250, 200, 50, seaweed_green, neon_green, "900 billion tonnes")
        make_button(150, 400, 200, 50, seaweed_green, neon_green, "There isn't any")
        make_button(450, 400, 200, 50, seaweed_green, neon_green, "500 million tonnes")


        pygame.display.update()
        clock.tick(60)


def end_screen():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        # draw background
        background(sea_floor)

        make_button(200, 300, 100, 50, seaweed_green, neon_green, "Return")
        make_button(500, 300, 100, 50, seaweed_green, neon_green, "Again")

        # update screen
        pygame.display.update()
        # frames game is running at
        clock.tick(60)



game_intro()
home_screen()
game_loop()
pygame.quit()
quit()