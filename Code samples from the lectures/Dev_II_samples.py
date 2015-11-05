########################
# lecture two - solution
########################

class Empty:
  def __init__(self):
      self.IsEmpty = True
Empty = Empty()

class Node:
  def __init__(self, value, tail):
      self.IsEmpty = False
      self.Value   = value
      self.Tail    = tail

#l = Empty
#for i in range(0, int(input("How many elements in the list?"))):
#  l = Node(int(input("Insert the next element")), l)

#x = l
#while not(x.IsEmpty):
#  print(x.Value)
#  x = x.Tail

########################
# lecture four - list hof's
########################

def printValues(l):
  if l.IsEmpty:
    return
  else:
    print(l.Value)
    printValues(l.Tail)

def map(f, l):
  if l.IsEmpty:
    return Empty
  else:
    return Node(f(l.Value), map(f,l.Tail))
printValues(map(lambda x: x + 10, Node(1, Node(2, Node(3, Empty)))))

def filter(p, l):
  if l.IsEmpty:
    return Empty
  else:
    tl = filter(p,l.Tail)
    if p(l.Value):
      return Node(l.Value, tl)
    else:
      return tl
printValues(filter(lambda x: x % 2 == 1, Node(1, Node(2, Node(3, Empty)))))

quit()

########################
# lecture four - length
########################

cnt = 0
x = l
while not(x.IsEmpty):
  cnt = cnt + 1
  x = x.Tail
print("List contains " + str(cnt) + " elements.")

def length_loop(l):
  cnt = 0
  x = l
  while not(x.IsEmpty):
    cnt = cnt + 1
    x = x.Tail
  return cnt  

def length(l):
  if l.IsEmpty:
    return 0
  else:
    return length(l.Tail) + 1
print("List contains " + str(length(l)) + " elements.")

quit()

########################
# lecture four - simple HOF's
########################
def plus(x,y): return x + y
def times(x,y): return x * y
def minus(x,y): return x - y

def combine(op,x,y):
  return op(x,y)

print(combine(plus, "10", "20"))
print(combine(times, 10, 20))
print(combine(minus, 10, 20))

print(combine((lambda x,y: x+y), 10, 20))
print(combine((lambda x,y: x*y), 10, 20))
print(combine((lambda x,y: x-y), 10, 20))

def choose_operation():
  i = input("Choose an operation between +, -, or *")
  if i == "+":
    return lambda x,y: x+y
  elif i == "-":
    return lambda x,y: x-y
  else:
    return lambda x,y: x*y
print(combine(choose_operation(), 10, 20))

quit()

########################
# lecture one - problem
########################
playerOneName = "P1"
playerOnePositionX = 0.0
playerOnePositionY = 0.0

playerTwoName = "P2"
playerTwoPositionX = 5.0
playerTwoPositionY = 0.0

playerThreeName = "P3"
playerThreePositionX = 10.0
playerThreePositionY = 0.0

########################
# lecture one - solution
########################
class Player:
  def __init__(self, name, posX, posY):
    self.Name = name
    self.PositionX = posX
    self.PositionY = posY

playerOne   = Player("P1", 0.0, 0.0)
playerTwo   = Player("P2", 5.0, 0.0)
playerThree = Player("P3", 10.0, 0.0)

print(playerOne.Name + " is at " + str(playerOne.PositionX) + "," + str(playerOne.PositionY))
print(playerTwo.Name + " is at " + str(playerTwo.PositionX) + "," + str(playerTwo.PositionY))
print(playerThree.Name + " is at " + str(playerThree.PositionX) + "," + str(playerThree.PositionY))

########################
# lecture one - refined
########################
class Vector2:
  def __init__(self, x, y):
    self.X = x
    self.Y = y

class PlayerRefined:
  def __init__(self, name, posX, posY):
    self.Name = name
    self.Position = Vector2(posX,posY)

playerOne   = PlayerRefined("P1", 0.0, 0.0)
playerTwo   = PlayerRefined("P2", 5.0, 0.0)
playerThree = PlayerRefined("P3", 10.0, 0.0)

print(playerOne.Name + " is at " + str(playerOne.Position.X) + "," + str(playerOne.Position.Y))
print(playerTwo.Name + " is at " + str(playerTwo.Position.X) + "," + str(playerTwo.Position.Y))
print(playerThree.Name + " is at " + str(playerThree.Position.X) + "," + str(playerThree.Position.Y))

################################################
# lecture four - local and global mutation
################################################
def f(x):
  cnt = cnt + 1
  x = x + 1
  return x * 2

print(f(10))
print(f(20))
print(cnt)

quit()

########################
# lecture four - shadowing
########################
x = 10

def f(x):
  return x * 2

print(f(10))
print(f(20))

quit()

########################
# lecture four - scope
########################
def f(z):
  z = z + 1
  return z * 2

print(f(10))
print(f(30))

quit()

########################
# lecture two - scope
########################
x = 1

def f(z):
  return x * z

print(f(10))
print(f(30))
x = 2
print(f(10))
print(z)

quit()