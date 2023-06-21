import random

def randomWordGenerator():
  listOfWords = []
  f = open("words.txt")
  for word in f:
    listOfWords.append(word.strip().upper())


  randomInd = random.randint(0, len(listOfWords) - 1)
  randomWord = listOfWords[randomInd]
  return randomWord