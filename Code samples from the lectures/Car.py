import math

class Vector2:
  def __init__(self, x, y):
    self.X = x
    self.Y = y
  def Length(self):
    return math.sqrt(self.X * self.X + self.Y * self.Y)
  def __neg__(self):
    return Vector2(-self.X, -self.Y)
  def __add__(self, other):
    return Vector2(self.X + other.X, self.Y + other.Y)
  def __sub__(self, other):
    return self + (-other);
  def __mul__(self, k):
    return Vector2(self.X * k, self.Y * k)
  def __str__(self):
    return "(" + str(self.X) + "," + str(self.Y) + ")"
  def Zero(): 
    return Vector2(0.0, 0.0)
  def UnitX(): 
    return Vector2(1.0, 0.0)
  def UnitY(): 
    return Vector2(0.0, 1.0)

v = Vector2.UnitX() * 10.0 - Vector2.UnitY() * 2.0
print(str(v))


class Car:
  def __init__(self, p, v, g):
    self.Position = p
    self.Velocity = v
    self.Gas = g
  def Travel(self, dt):
    if self.Gas > 0.0:
      return Car(self.Position + self.Velocity * dt, self.Velocity, self.Gas - 1.0 * dt)
    else:
      return self
  def __str__(self):
    return "A car at " + str(self.Position) + " with a tank of " + str(self.Gas) + " liters"

c = Car(Vector2.Zero(), Vector2.UnitX(), 10.0)
while(c.Gas > 0.0):
  c = c.Travel(2.0)
  print(c)




class MutableCar:
  def __init__(self, p, v, g):
    self.Position = p
    self.Velocity = v
    self.Gas = g
  def Travel(self, dt):
    if self.Gas > 0.0:
      self.Position = self.Position + self.Velocity * dt
      self.Gas = self.Gas - 1.0 * dt
  def __str__(self):
    return "A car at " + str(self.Position) + " with a tank of " + str(self.Gas) + " liters"

print("Starting the trip!")
c = MutableCar(Vector2.Zero(), Vector2.UnitX(), 10.0)
while(c.Gas > 0.0):
  c.Travel(2.0)
  print(c)
