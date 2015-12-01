import pygame
import random
import os

class Cons:
  def __init__(self, value, tail):
    self.Tail = tail
    self.Value = value
    self.IsEmpty = False

class Empty: 
  def __init__(self):
    self.IsEmpty = True

Empty = Empty()
NotTraverseable = 0

class Node:
  def __init__(self, position, texture, offset, properties):    
    self.Properties = properties
    self.Up = None
    self.Down = None
    self.Left = None
    self.Right = None
    self.Value = Empty
    self.Properties = Empty
    self.Position = position
    self.DefaultTexture = pygame.image.load(texture).convert()
    self.Visited = False
    self.Offset = offset
    props = properties

    traversable = True
    while(props.IsEmpty != True):
      if props.Value == NotTraverseable: traversable = False
      props = props.Tail
    
    self.Traverseable = traversable
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
        
  def Update(self):
    Exception("Not implemented yet")

  def Draw(self, screen):            
    if self.Visited == False:
      self.Visited = True
      if self.Traverseable:
        _width = int(self.Offset / 3)
        dim = 2
        screen.blit(pygame.transform.scale(self.DefaultTexture, (_width + dim, _width + dim)), 
                    (_width + self.Position[0] * self.Offset, 
                      _width + self.Position[1] * self.Offset))
        
        if self.Up != None and self.Up.Traverseable:
          screen.blit(pygame.transform.scale(self.DefaultTexture, (_width + dim, _width  + dim)), 
                      (_width + self.Position[0] * self.Offset, 
                       self.Position[1] * self.Offset))
        if self.Down != None and self.Down.Traverseable:
          screen.blit(pygame.transform.scale(self.DefaultTexture, (_width + dim, _width  + dim)), 
                      (_width + self.Position[0] * self.Offset, 
                       _width * 2 + self.Position[1] * self.Offset))
        if self.Left != None and self.Left.Traverseable:
          screen.blit(pygame.transform.scale(self.DefaultTexture, (_width + dim, _width  + dim)), 
                      (self.Position[0] * self.Offset, 
                       _width + self.Position[1] * self.Offset))
        if self.Right!= None and self.Right.Traverseable:
          screen.blit(pygame.transform.scale(self.DefaultTexture, (_width + dim, _width  + dim)), 
                      (_width * 2 + self.Position[0] * self.Offset, 
                        _width + self.Position[1] * self.Offset))        
        
      else:
        screen.blit(pygame.transform.scale(self.DefaultTexture, (self.Offset - 1, self.Offset - 1)), (self.Position[0] * self.Offset, self.Position[1] * self.Offset))

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
      if (random.uniform(0, 1) > 0.8):
        properties = Cons(NotTraverseable, Empty)
        node = Node((column, row), os.path.join("Content","house.png"), offset, properties)
      else:
        node = Node((column, row), os.path.join("Content","white_pixel.png"), offset, Empty)
      
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


