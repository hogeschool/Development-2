class Empty:
  def __init__(self):
    self.Type = "Empty"

class Node:
  def __init__(self,hd,tl):
    self.Type = "Node"
    self.Head = hd
    self.Tail = tl

def length(l):
  return fold(l, 0, lambda x,y: 1 + y)

def sum(l):
  return fold(l, 0, lambda x,y: x + y)

def mul(l):
  return fold(l, 1, lambda x,y: x * y)

def fold(l,d,c):
  if l.Type == "Empty":
    return d
  else:
    return c(l.Head, fold(l.Tail,d,c))

def printList(l):
  print(fold(l, "", lambda x,y: x + ", " + y))

def prettify(l):
  if l.Type == "Empty":
    return Empty()
  else:
    return Node("My pretty " + l.Head + " <3", prettify(l.Tail))


myList = Node("first element", Node("second element", Node("third element", Empty())))

