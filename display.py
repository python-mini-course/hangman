# Example file showing a basic pygame "game loop"
import pygame

# pygame setup
pygame.init()
Display = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

import helper
import start

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
GREY = (200,200,200)

FONT = pygame.font.SysFont('Roboto', 80)
wrongGuessFont = pygame.font.SysFont('Roboto', 50)


center = pygame.Vector2(Display.get_width() / 2, Display.get_height() / 2)

word = start.randomWordGenerator()
correctGuesses = []
wrongGuesses = []

won = False
lost = False

while running:

    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        #For Guess
        if event.type == pygame.KEYDOWN:
            key = event.unicode
            if key.isalpha():
                guess = key.upper()
                if guess in word: # if the character is not in word
                    if guess not in correctGuesses:
                        correctGuesses.append(guess)

                        # check if player won
                        won = True
                        for letter in word:
                            if letter not in correctGuesses:
                                won = False

                else: # if the character is not in the word
                    if guess not in wrongGuesses:
                        wrongGuesses.append(guess)

                        # check if player lost
                        if len(wrongGuesses) > 6:
                            lost = True
    
    # Game Completed
    if won:
        Display.fill("white")
        wonText = FONT.render('YOU WON!!', True, BLACK)
        Display.blit(wonText, center)
        pygame.display.flip()
        continue
    if lost:
        Display.fill("white")
        lostText = FONT.render('YOU LOST!!', True, BLACK)
        Display.blit(lostText, center)
        pygame.display.flip()
        continue
                        

    # fill the Display with a color to wipe away anything from last frame
    Display.fill("white")

    # title
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

    # Make boxes for the letters
    helper.drawBoxes(Display, len(word))

    i = 0
    # Show the letter
    for letter in word:
        if letter in correctGuesses:
            helper.addLetter(Display, letter, i)
        i += 1
    
    # Show the hangman
    for x in range(len(wrongGuesses) + 1):
        helper.wrong(Display, x)

    # Show wrong guesses
    helper.showWrongGuesses(Display, wrongGuesses)
    

    # flip() the display to put your work on Display
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()