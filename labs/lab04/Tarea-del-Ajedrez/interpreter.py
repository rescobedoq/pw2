import pygame, sys
from pygame.locals import *
from colors import *

def parseLine(DISPLAY, y, s):
  x = 0
  for c in s:
    pygame.draw.line(DISPLAY, color[c], (x, y), (x, y))
    x += 1

def draw(picture):
  try:
    img = picture.img
  except:
    img = picture
  pygame.init()

  DISPLAY=pygame.display.set_mode((640, 480))
  DISPLAY.fill(BLUE)

  n = len(img)
  for i in range(0, n):
    parseLine(DISPLAY, i, img[i])

  while True:
    for event in pygame.event.get():
      if event.type==QUIT:
        pygame.quit()
        #sys.exit()
    pygame.display.update()


