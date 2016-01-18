import random
class Node:
  def __init__(self, value, tail):
    self.Tail = tail
    self.Value = value
    self.IsEmpty = False

class Empty: 
  def __init__(self):
    self.IsEmpty = True

Empty = Empty()

def AUX_length(l, acc):
  if l.IsEmpty: return acc
  else: return AUX_length(l.Tail, acc + 1)

def length(l):
  return AUX_length(l, 0)

def select_one_random(l):
  _length = length(l)
  rnd_num = int(random.uniform(0, _length ))
  while(rnd_num > 0):
    l = l.Tail
    rnd_num -= 1
  return l.Value
  

