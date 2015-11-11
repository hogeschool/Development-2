import math

class Counter:
  def __init__(self):
    self.cnt = 0
  def Tick(self, n):
    self.cnt = self.cnt + n
  def __str__(self):
    return "Ticked " + str(self.cnt) + " times."

c = Counter()
for i in range(0, 5):
  c.Tick(i)
  print(c)
  #input("Press enter to continue")
