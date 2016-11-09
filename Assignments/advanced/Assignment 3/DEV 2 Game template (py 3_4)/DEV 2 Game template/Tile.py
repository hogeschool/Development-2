import pygame
import random
from Car import *
from Node import *


#TILE PROPERTIES
NotTraverseable = 0
Park   = 1
River  = 2
Bridge = 3
Harbor = 4

#VECTOR2 CLASS
class Vector2:
  def __init__(self, x, y):
    self.X = x
    self.Y = y


#TILE CLASS
class Tile:
  def __init__(self, position, texture, offset, properties):    
    self.Properties = properties
    self.Up = None
    self.Down = None
    self.Left = None
    self.Right = None
    self.Position = position

    self.IsEntryOfBridge = False
    self.DefaultTexture = pygame.image.load(texture).convert()
    self.Offset = offset
    self.UpdateProps(properties)
    

  def UpdateProps(self, properties):
    props = properties
    self.Bridge = False
    self.Traverseable = True
    self.Park = False
    self.River = False
    self.Harbor = False
    while(props.IsEmpty != True):
      if props.Value == Bridge: self.Bridge = True
      if props.Value == NotTraverseable: self.Traverseable = False
      if props.Value == Park: self.Park = True
      if props.Value == Harbor: self.Harbor = True
      if props.Value == River: self.River = True
      props = props.Tail

  def Draw(self, screen, is_drawing_bridges):            
    def draw_river():
      image = self.DefaultTexture.copy()
      # zero out RGB values
      image.fill((0, 0, 0, 255), None, pygame.BLEND_RGBA_MULT)
      # add in new RGB values
      image.fill((0,0,255,0), None, pygame.BLEND_RGBA_ADD)
      screen.blit(pygame.transform.scale(image, (self.Offset, self.Offset)), (self.Position.X * self.Offset, self.Position.Y * self.Offset))
    
    
    
    if self.River and not is_drawing_bridges:
      draw_river()    
    if not self.Harbor and self.Traverseable and not self.Park and not self.River or self.Bridge :

      _width = int(self.Offset / 3)
      dim = 2
      screen.blit(pygame.transform.scale(self.DefaultTexture, (_width + dim, _width + dim)), 
                  (_width + self.Position.X * self.Offset, 
                    _width + self.Position.Y * self.Offset))
        
      if self.Up != None and self.Up.Traverseable or (self.Bridge and (self.Down != None and self.Down.Traverseable and self.Up != None and self.Up.Traverseable)):
        screen.blit(pygame.transform.scale(self.DefaultTexture, (_width + dim, _width  + dim)), 
                    (_width + self.Position.X * self.Offset, 
                      self.Position.Y * self.Offset))
      if self.Down != None and self.Down.Traverseable or (self.Bridge and (self.Down != None and self.Down.Traverseable and self.Up != None and self.Up.Traverseable)):
        screen.blit(pygame.transform.scale(self.DefaultTexture, (_width + dim, _width  + dim)), 
                    (_width + self.Position.X * self.Offset, 
                      _width * 2 + self.Position.Y * self.Offset))
      if self.Left != None and self.Left.Traverseable or (self.Bridge and (self.Left != None and self.Left.Traverseable and self.Right != None and self.Right.Traverseable)):
        screen.blit(pygame.transform.scale(self.DefaultTexture, (_width + dim, _width  + dim)), 
                    (self.Position.X * self.Offset, 
                      _width + self.Position.Y * self.Offset))
      if self.Right!= None and self.Right.Traverseable or (self.Bridge and (self.Left != None and self.Left.Traverseable and self.Right != None and self.Right.Traverseable)):
        screen.blit(pygame.transform.scale(self.DefaultTexture, (_width + dim, _width  + dim)), 
                    (_width * 2 + self.Position.X * self.Offset, 
                      _width + self.Position.Y * self.Offset))                      
    elif self.Harbor: 
      draw_river()     
      screen.blit(pygame.transform.scale(self.DefaultTexture, (self.Offset - 1, self.Offset - 1)), (self.Position.X * self.Offset, self.Position.Y * self.Offset))
    elif not self.River:
      screen.blit(pygame.transform.scale(self.DefaultTexture, (self.Offset - 1, self.Offset - 1)), (self.Position.X * self.Offset, self.Position.Y * self.Offset))


def build_rivers(board):

  entry_point = board
  node = board
  init_node = node
  while(node != None):
    row = node.Position.Y
    column = node.Position.X

    if (column > 0):
      prev_node = node.Left  
      def UpdateNode(node):
        properties = Node(NotTraverseable, Node(River, Empty))
        node.DefaultTexture = pygame.image.load("Content\white_pixel.png").convert()
        node.UpdateProps(properties)
      if row == 0:
        if(prev_node != None and not prev_node.River):
          if random.uniform(0, 1) > 0.0:
            UpdateNode(node)
      else:          
        above_line = node.Up
        if random.uniform(0, 1) > 0.3 and above_line.Left != None and not above_line.Left.River and prev_node.River:
          UpdateNode(node)
        elif random.uniform(0, 1) > 0.3 and above_line.Left.River and prev_node.River and not above_line.River:
          UpdateNode(node)
        elif random.uniform(0, 1) > 0.3 and above_line.River and not prev_node.River:
          UpdateNode(node)
    if node.Right == None:
      node = init_node.Down
      init_node = node
    else:
      node = node.Right
  return entry_point


def build_bridge(board, dimension):

  entry_point = board
  node = board
  init_node = node
  while(node != None):
    row = node.Position.Y
    column = node.Position.X

    
    prev_node = node.Left  
    def UpdateNode(node):
      properties = Node(River, Node(Bridge, Empty))
      node.DefaultTexture = pygame.image.load("Content\white_pixel.png").convert()
      node.UpdateProps(properties)
    if node.River:
      if (column > 0 and row > 0 and column < dimension - 1 and row < dimension - 1):
        if (not node.Left.River and not node.Right.River and node.Left.Traverseable and node.Right.Traverseable) or (not node.Down.River and not node.Up.River and node.Up.Traverseable and node.Down.Traverseable):
          if (not node.Left.River and not node.Right.River and node.Left.Traverseable and node.Right.Traverseable):
            node.Left.IsEntryOfBridge = True
            node.Right.IsEntryOfBridge = True
          else:
            node.Up.IsEntryOfBridge = True
            node.Down.IsEntryOfBridge = True
          UpdateNode(node)
      elif (column > 0 and column < dimension - 1):
        if (node.Left.Traverseable and node.Right.Traverseable and not node.Left.River and not node.Right.River):
          node.Left.IsEntryOfBridge = True
          node.Right.IsEntryOfBridge = True
          UpdateNode(node)
      elif (row > 0 and row < dimension - 1):
        if (not node.Down.River and not node.Up.River and node.Up.Traverseable and node.Down.Traverseable):
          node.Up.IsEntryOfBridge = True
          node.Down.IsEntryOfBridge = True
          UpdateNode(node)
    if node.Right == None:
      node = init_node.Down
      init_node = node
    else:
      node = node.Right
  return entry_point


def build_buildings(tiles):
  if tiles.IsEmpty: return None
  else:
    node = tiles.Value
    if node.Position != (0,0):
      if (random.uniform(0, 1)) > 0.8 and node.River and not node.Bridge:
        properties = Node(Harbor, Empty)
        node.DefaultTexture = pygame.image.load("Content\harbor.png").convert()
        node.UpdateProps(properties)
      if (random.uniform(0, 1)) > 0.8 and not node.River and not node.IsEntryOfBridge:
        properties = Node(NotTraverseable, Empty)
        node.DefaultTexture = pygame.image.load("Content\house.png").convert()
        node.UpdateProps(properties)
      elif not node.IsEntryOfBridge and (random.uniform(0, 1)) > 0.85 and not node.River and ((node.Left != None and node.Left.Traverseable and not node.Left.River) or (node.Right != None and node.Right.Traverseable and not node.Right.River) or (node.Up != None and node.Up.Traverseable and not node.Up.River) or (node.Down != None and node.Down.Traverseable and not node.Down.River)):
        properties = Node(Park, Empty)
        node.DefaultTexture = pygame.image.load("Content\park.png").convert()
        node.UpdateProps(properties)
    build_buildings(tiles.Tail)


def build_scene (dimension, offset):
  def build_board():
    entry_point = None
    above_line = None
    prev_node = None
    for row in range(dimension):    
      for column in range(dimension):
        node = Tile(Vector2(column, row), "Content\white_pixel.png", offset, Empty)
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
  board = build_board()
  board_with_rivers = build_rivers(board)
  board_with_bridges = build_bridge(board_with_rivers, dimension)

  _board = board 
  __board = _board
  all_tiles = Empty
  first = Node(board, Empty)
  rest = first
  while(__board != None):
    while(_board != None):
      rest.Tail = Node(_board, Empty)
      rest = rest.Tail
      _board = _board.Right
    __board = __board.Down
    _board = __board
  
  entry_rivers = Empty
  _first = first
  while not _first.IsEmpty:
    if _first.Value.River and _first.Value.Position.Y == 0:
      entry_rivers = Node(_first.Value, entry_rivers)
    _first = _first.Tail


  bridges = Empty
  _first = first
  while not _first.IsEmpty:
    if _first.Value.Bridge:
      bridges = Node(_first.Value, bridges)
    _first = _first.Tail
  
  build_buildings(first)
  return first, entry_rivers, bridges

