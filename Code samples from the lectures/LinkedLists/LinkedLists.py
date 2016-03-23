class Empty:
  def __init__(self):
    self.Type = "Empty"
  def filter(self,p):
    return Empty()
  def map(self,f):
    return Empty()
  def __str__(self):
    return "nil"

class Node:
  def __init__(self,hd,tl):
    self.Type = "Node"
    self.Head = hd
    self.Tail = tl
  def filter(self,p):
    if p(self.Head):
      return Node(self.Head, self.Tail.filter(p))
    else:
      return self.Tail.filter(p)
  def map(self,f):
    return Node(f(self.Head), self.Tail.map(f))
  def __str__(self):
    return str(self.Head) + "," + str(self.Tail)

def unfold(s, p, f):
  if p(s):
    return Empty()
  else:
    (x,s1) = f(s)
    return Node(x, unfold(s1, p, f))

def fold(l,d,c):
  if l.Type == "Empty":
    return d
  else:
    return c(l.Head, fold(l.Tail,d,c))

def repeat_forever(step, termination):
  while termination() is False:
    step()

#cnt = 0
#def incrCount():
#  global cnt
#  cnt = cnt + 1
#  print(cnt)
#repeat_forever(incrCount, lambda: cnt > 100)

def length(l):
  return fold(l, 0, lambda x,y: 1 + y)

def sum(l):
  return fold(l, 0, lambda x,y: x + y)

def mul(l):
  return fold(l, 1, lambda x,y: x * y)

def printList(l):
  print(fold(l, "", lambda x,y: str(x) + ", " + str(y)))

def prettify(l):
  return map(l, lambda x: "My pretty " + x + " <3")

def uglify(l):
  return map(l, lambda x: "My ugly " + x + " :(")

def neutralify(l):
  return map(l, lambda x: "My neutral " + x + " :|")

#myList = Node("first element", Node("second element", Node("third element", Empty())))
#printList(prettify(myList))
#printList(uglify(myList))
#printList(neutralify(myList))

def interval(l, u):
  return unfold((l,u), lambda s: s[0] > s[1], lambda s: (s[0], (s[0]+1, s[1])))

def repeat(x, n):
  return unfold(n, lambda n: n <= 0, lambda n: (x, n-1))

myOtherList = repeat(interval(0,5), 5)
print(myOtherList)
#printList(myOtherList.filter(lambda x: x % 2 == 0).map(lambda x: x + 1).filter(lambda x: x > 4))
