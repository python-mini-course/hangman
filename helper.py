import pygame

BLACK = (0,0,0)
RED = (255,0,0)

FONT = pygame.font.SysFont('Roboto', 80)
wrongGuessFont = pygame.font.SysFont('Roboto', 50)

def drawHangman(Display, num):
  if(num == 0):
    return True
  elif(num == 1): #head
    pygame.draw.circle(Display, BLACK, (150,150),50,8) 
  elif(num == 2): #body
    pygame.draw.line(Display, BLACK, (150,200),(150,300),8) 
  elif(num == 3): #lefthand
    pygame.draw.line(Display, BLACK, (150,210),(100,250),9) 
  elif(num == 4): #righthand
    pygame.draw.line(Display, BLACK, (150,210),(200,250),9) 
  elif(num == 5): #leftleg
    pygame.draw.line(Display, BLACK, (150,300),(100,350),9) 
  elif(num == 6): #rightleg
    pygame.draw.line(Display, BLACK, (150,300),(200,350),9) 
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
