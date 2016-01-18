import time
from threading import Thread
import os, pygame
import time
from Tile import *
from Node import *
from Boat import *
pygame.init()
size = width, height = 600, 600
white = 255, 255, 255
green = 50, 255, 100
screen = pygame.display.set_mode(size)
offset = 50
size = 10
entry_road, entry_rivers, bridges = build_scene(size, offset)

#faces to the right
boat_texture = pygame.image.load(os.path.join("Content","tanker.png")).convert_alpha()

#faces to the right
car_texture = pygame.image.load(os.path.join("Content","car.png")).convert_alpha()





def Main():
  start = time.time()
  while True:    
    pygame.event.pump()
    screen.fill(green)

    #here we draw the board, do not move
    _board = entry_road
    while not _board.IsEmpty:
      _board.Value.Draw(screen, False)
      _board = _board.Tail

    #here we draw the bridges, do not move
    _board = bridges
    while not _board.IsEmpty:
      _board.Value.Draw(screen, True)
      _board = _board.Tail

    



    pygame.display.flip()
    time.sleep(0.2)
    
Main()
