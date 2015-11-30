###########
# lists
###########
def lists():
  a = [-1, 1, 66.25, 333, 333, 1234.5]
  print(a)
  del a[0]
  print(a)
  del a[2:4]
  print(a)
  del a[:]
  print(a)
  squares = list(map(lambda x: x**2, range(10)))
  print(squares)
  squares = [x**2 for x in range(10)]
  print(squares)
  print([(x, y) for x in [1,2,3] for y in [3,1,4] if x != y])
#lists()

#list.append(x) #Add an item to the end of the list. Equivalent to a[len(a):] = [x].
#list.extend(L) #Extend the list by appending all the items in the given list. Equivalent to a[len(a):] = L.
#list.insert(i, x) #Insert an item at a given position. The first argument is the index of the element before which to insert, so a.insert(0, x) inserts at the front of the list, and a.insert(len(a), x) is equivalent to a.append(x).
#list.remove(x) #Remove the first item from the list whose value is x. It is an error if there is no such item.
#list.pop([i]) #Remove the item at the given position in the list, and return it. If no index is specified, a.pop() removes and returns the last item in the list. (The square brackets around the i in the method signature denote that the parameter is optional, not that you should type square brackets at that position. You will see this notation frequently in the Python Library Reference.)
#list.clear() #Remove all items from the list. Equivalent to del a[:].
#list.index(x) #Return the index in the list of the first item whose value is x. It is an error if there is no such item.
#list.count(x) #Return the number of times x appears in the list.
#list.sort(key=None, reverse=False) #Sort the items of the list in place (the arguments can be used for sort customization, see sorted() for their explanation).
#list.reverse() #Reverse the elements of the list in place.
#list.copy() #Return a shallow copy of the list. Equivalent to a[:].



###########
# tuples
###########
def tuples():
  t = 12345, 54321, 'hello!'
  print(t)
  print(t[0])
  x, y, z = t
  print(x)
  print(y)
  print(z)

  u = t, (1, 2, 3, 4, 5)
  print(u)
  # t[0] = 88888    not valid because tuples are immutable
  empty = ()
  print(empty)
  singleton = 'hello', # note the trailing comma!
  print(singleton)
#tuples()



###########
# sets
###########
def sets():
  basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
  print(basket)
  print('orange' in basket)
  print('crabgrass' in basket)
  a = set('abracadabra') # explicit constructor
  b = set('alacazam') # explicit constructor
  print(a - b)                              # letters in a but not in b
  print(a | b)                              # letters in either a or b
  print(a & b)                              # letters in both a and b
  print(a ^ b)                              # letters in a or b but not both
  print({x for x in 'abracadabra' if x not in 'abc'})
sets()



###########
# maps
###########
def maps():
  tel = {'jack': 4098, 'sape': 4139}
  print(tel)
  tel['guido'] = 4127
  print(tel)
  print(tel['jack'])
  del tel['sape']
  print(tel)
  tel['irv'] = 4127
  print(tel)
  print(list(tel.keys()))
  print(sorted(tel.keys()))
  print('guido' in tel)
  print('jack' not in tel)
  print(dict([('sape', 4139), ('guido', 4127), ('jack', 4098)]))
  knights = {'gallahad': 'the pure', 'robin': 'the brave'}
  for k, v in knights.items():
    print(k, v)
maps()

