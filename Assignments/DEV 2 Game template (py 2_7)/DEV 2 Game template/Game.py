import os, pygame
import time
from Prelude import *
pygame.init()

size = width, height = 600, 600
white = 255, 255, 255
black = 0, 0, 0
green = 50, 255, 100

screen = pygame.display.set_mode(size)


not_quit = True

start = time.time()
angle = 0
dt = 0.016

board = build_square_matrix(10, 50)

while not_quit :
  for even in pygame.event.get():
    if even.type == pygame.QUIT: not_quit = False

  screen.fill(green)  
  end = time.time()
  if end - start >= dt:    
    start = end
  board.Draw(screen)

  board.Reset()
  pygame.display.flip()
os._exit(1)
