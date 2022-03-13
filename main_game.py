import pygame

pygame.init()

display_width = 800
display_height = 600

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

car_width = 73

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('A bit Racey')
clock = pygame.time.Clock()

carImg = pygame.image.load('./images/racecar.png')
cityImg = pygame.image.load('./images/city2.jpg')
def background():
    scaled_img = pygame.transform.scale(cityImg, (display_width, display_height))
    gameDisplay.blit(scaled_img, (0, 0))

def car(x, y):
    gameDisplay.blit(carImg, (x, y))

def game_loop():
    x = (display_width * 0.45)
    y = (display_height * 0.8)

    x_change = 0
    y_change = 0

    gameExit = False

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5
                if event.key == pygame.K_UP:
                    y_change = -5
                if event.key == pygame.K_DOWN:
                    y_change = 5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change = 0

        x += x_change
        y += y_change
        gameDisplay.fill(white)
        background()
        car(x, y)

        if x > display_width - car_width:
            x = display_width - car_width
        if x < 0:
            x = 0
        if y < 0:
            y = 0
        if y > display_height - car_width:
            y = display_height - car_width
        pygame.display.update()
        clock.tick(60)


game_loop()
pygame.quit()
quit()