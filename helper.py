import pygame

BLACK = (0,0,0)
RED = (255,0,0)

FONT = pygame.font.SysFont('Roboto', 80)
wrongGuessFont = pygame.font.SysFont('Roboto', 50)

def wrong(Display, num):
  if(num == 0):
    return True
  elif(num == 1):
    pygame.draw.circle(Display, BLACK, (150,150),50,8)#head
  elif(num == 2):
    pygame.draw.line(Display, BLACK, (150,200),(150,300),8)#body
  elif(num == 3):
    pygame.draw.line(Display, BLACK, (150,210),(100,250),9)#lefthand
  elif(num == 4):
    pygame.draw.line(Display, BLACK, (150,210),(200,250),9)#righthand
  elif(num == 5):
    pygame.draw.line(Display, BLACK, (150,300),(100,350),9)#leftleg
  elif(num == 6):
    pygame.draw.line(Display, BLACK, (150,300),(200,350),9)#rightleg
  else:
    return False
  
  return True


def drawBoxes(Display, num):
  for x in range(num):
    pygame.draw.rect(Display, BLACK, (400 + x * 100, 200, 80, 100), 2)

def addLetter(Display, letter, index):
  letter = FONT.render(letter, True, BLACK)
  Display.blit(letter, (425 + index * 100, 225))

def showWrongGuesses(Display, wrongGuesses):
  ind = 0
  for letter in wrongGuesses:
    wrongGuess = wrongGuessFont.render(letter, True, RED)
    Display.blit(wrongGuess, (125 + ind * 40, 575))
    ind += 1
