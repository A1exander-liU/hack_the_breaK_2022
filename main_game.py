import pygame

pygame.init()

# creating the game window size
screen_width = 800
screen_height = 600
game_window = pygame.display.set_mode((screen_width, screen_height))

# colours
black = (0, 0, 0)
white = (255, 255, 255)

# title that appears in the game window
pygame.display.set_caption("Placeholder for name")

clock = pygame.time.Clock()

crashed = False
# keep the window active as long as you don't press the quit button
while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
        # checking out all the events happening in the background
        print(event)
    # updates the game screen
    pygame.display.update()
    # how many frames are we running at? 60fps
    clock.tick(60)