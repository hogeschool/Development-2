# symbols agenda
# : colon

import os
import time
import random
class Empty: #define a class called Empty
  def __init__(self): #define the constructor 
                      #with empty parameters 
                      #(self is implicit)
    self.IsEmpty = True #we asstign True to an 
                        #attribute called IsEmpty
Empty = Empty() #we assign an instance of class 
                #Empty to a variable called empty
class Node:
  def __init__(self, v, t, p):
    self.Value = v
    self.Next = t
    self.Prev = p
    self.IsEmpty = False


class Car:
  def __init__(self, p):
    self.Position = p
    self.Speed = 1
    
  def Move(self):
    if not self.Position.Next.IsEmpty and self.Speed > 0:
      self.Position = self.Position.Next
    if not self.Position.Prev.IsEmpty and self.Speed < 0:
      self.Position = self.Position.Prev


  def Print(self):
    print("O"),
class Tile:
  def __init__(self, p, is_start, is_finish):
    self.Position = p
    self.Start = is_start
    self.Finish = is_finish

class Board:
  def __init__(self, amount_of_tile):
    self.Tiles = Empty
    for x in range(amount_of_tile):
      is_start = amount_of_tile - 1 == x
      is_end = x == 0
      current_node = Node(Tile(amount_of_tile - x, is_start, is_end), Empty, Empty)

      if not self.Tiles.IsEmpty:
        self.Tiles.Prev = current_node
      current_node.Next = self.Tiles

      self.Tiles = current_node

    if amount_of_tile > 0:
      self.Car = Car(self.Tiles)

  def Update(self):
    self.Car.Move()

  def Draw(self):
    tiles_iterator = self.Tiles
    while not tiles_iterator.IsEmpty:
      if tiles_iterator == self.Car.Position:
        self.Car.Print()
      else:
        print("_"),
      tiles_iterator = tiles_iterator.Next

dim = 100    
game = Board(dim)

while not game.Car.Position.Value.Finish:
  os.system('cls')
  game.Draw()
  game.Update()
  if (random.random() > 0.8):
    game.Car.Speed = game.Car.Speed * -1
  time.sleep(0.016)

print ("Finish")

