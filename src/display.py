# Example file showing a basic pygame "game loop"
import pygame

# pygame setup
pygame.init()
Display = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

import helper

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
GREY = (200,200,200)

FONT = pygame.font.SysFont('Roboto', 80)
wrongGuessFont = pygame.font.SysFont('Roboto', 50)


player_pos = pygame.Vector2(Display.get_width() / 2, Display.get_height() / 2)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the Display with a color to wipe away anything from last frame
    Display.fill("white")

    # Title
    title = FONT.render('Hangman', True, BLACK)
    Display.blit(title, (Display.get_width() / 2, 50))

    #Draw hangman
    pygame.draw.line(Display, BLACK, (10,400),(300,400),8)#baseline
    pygame.draw.line(Display, BLACK, (50,50),(50,400),8)#stick1
    pygame.draw.line(Display, BLACK, (50,60),(250,60),8)#stick2
    pygame.draw.line(Display, BLACK, (150,60),(150,100),8)#rope

    # Wrong Guesses Box
    pygame.draw.rect(Display, BLACK, (100, 500, 1100, 200), 8)
    wrongGuessesText = wrongGuessFont.render('Wrong Guess', True, BLACK)
    Display.blit(wrongGuessesText, (125, 525))

    # CODE HERE
    # Make boxes for the letters
    helper.drawBoxes(Display, 5)

    # Add letters
    helper.addLetter(Display, "H", 0)
    helper.addLetter(Display, "A", 4)

    # Show wrong guesses
    helper.showWrongGuesses(Display, ["B","C"])

    # Draw hangman
    helper.wrong(Display, 1)
    helper.wrong(Display, 2)


    # flip() the display to put your work on Display
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()