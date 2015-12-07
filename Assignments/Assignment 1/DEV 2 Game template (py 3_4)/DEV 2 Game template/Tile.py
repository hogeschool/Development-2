import pygame
import random
from Car import *
from Node import *

NotTraverseable = 0
Park = 1

class Point:
  def __init__(self, x, y):
    self.X = x
    self.Y = y

class Tile:
  def __init__(self, position, texture, offset, properties):    
    self.Properties = properties
    self.Up = None
    self.Down = None
    self.Left = None
    self.Right = None
    self.Position = position

    self.DefaultTexture = pygame.image.load(texture).convert()
    self.Visited = False
    self.Offset = offset


    self.Traverseable = True
    self.Park = False

    props = properties
    while(props.IsEmpty != True):
      if props.Value == NotTraverseable: self.Traverseable = False
      if props.Value == Park: self.Park = True
      props = props.Tail




  def Reset(self):
    if self.Visited == True:
      self.Visited = False
      if self.Up != None:
        self.Up.Reset()
      if self.Down != None:
        self.Down.Reset()
      if self.Left != None:
        self.Left.Reset()
      if self.Right != None:
        self.Right.Reset()
        
  def Update(self, dt):
    
      if self.Visited == False:
        self.Visited = True
        tmp = self.Value
        while(tmp.IsEmpty != True):
          tmp.Value.Update(dt)
          tmp = tmp.Tail

        if self.Up != None:
          self.Up.Update(dt)
        if self.Down != None:
          self.Down.Update(dt)
        if self.Left != None:
          self.Left.Update(dt)
        if self.Right != None:
          self.Right.Update(dt)
      

  def Draw(self, screen):            
    if self.Visited == False:
      self.Visited = True
      if self.Traverseable and not self.Park:       

        _width = int(self.Offset / 3)
        dim = 2
        screen.blit(pygame.transform.scale(self.DefaultTexture, (_width + dim, _width + dim)), 
                    (_width + self.Position.X * self.Offset, 
                      _width + self.Position.Y * self.Offset))
        
        if self.Up != None and self.Up.Traverseable:
          screen.blit(pygame.transform.scale(self.DefaultTexture, (_width + dim, _width  + dim)), 
                      (_width + self.Position.X * self.Offset, 
                       self.Position.Y * self.Offset))
        if self.Down != None and self.Down.Traverseable:
          screen.blit(pygame.transform.scale(self.DefaultTexture, (_width + dim, _width  + dim)), 
                      (_width + self.Position.X * self.Offset, 
                       _width * 2 + self.Position.Y * self.Offset))
        if self.Left != None and self.Left.Traverseable:
          screen.blit(pygame.transform.scale(self.DefaultTexture, (_width + dim, _width  + dim)), 
                      (self.Position.X * self.Offset, 
                       _width + self.Position.Y * self.Offset))
        if self.Right!= None and self.Right.Traverseable:
          screen.blit(pygame.transform.scale(self.DefaultTexture, (_width + dim, _width  + dim)), 
                      (_width * 2 + self.Position.X * self.Offset, 
                        _width + self.Position.Y * self.Offset))                
      else:
        screen.blit(pygame.transform.scale(self.DefaultTexture, (self.Offset - 1, self.Offset - 1)), (self.Position.X * self.Offset, self.Position.Y * self.Offset))

      if self.Up != None:
        self.Up.Draw(screen)
      if self.Down != None:
        self.Down.Draw(screen)
      if self.Left != None:
        self.Left.Draw(screen)
      if self.Right != None:
        self.Right.Draw(screen)
      


def build_square_matrix (dimension, offset):
  entry_point = None
  above_line = None
  prev_node = None
  for row in range(dimension):    
    for column in range(dimension):
      if (random.uniform(0, 1) > 0.75) and row > 0 and column > 0:
        if (random.uniform(0, 1) > 0.75):
          properties = Node(Park, Empty)
          node = Tile(Point(column, row), "Content\park.png", offset, properties)
        else:
          properties = Node(NotTraverseable, Empty)
          node = Tile(Point(column, row), "Content\house.png", offset, properties)
      else:
        node = Tile(Point(column, row), "Content\white_pixel.png", offset, Empty)
      
      if row == 0 and column == 0:
        entry_point = node
      if (column == 0):
        prev_node = node        
      else:
        prev_node.Right = node
        node.Left = prev_node
        prev_node = node
      if(row > 0):
        node.Up = above_line
        above_line.Down = node
        above_line = above_line.Right
    
    while prev_node.Left != None:
      prev_node = prev_node.Left
    above_line = prev_node
  return entry_point


