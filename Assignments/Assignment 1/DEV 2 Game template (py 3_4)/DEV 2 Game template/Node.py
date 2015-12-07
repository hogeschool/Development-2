class Node:
  def __init__(self, value, tail):
    self.Tail = tail
    self.Value = value
    self.IsEmpty = False

class Empty: 
  def __init__(self):
    self.IsEmpty = True

Empty = Empty()