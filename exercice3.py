animals = ['cat', 'dog', 'monkey']

animals.append('fish')
print(animals)

animals.remove('fish')
print(animals)

animals.insert(1, 'fish')
print(animals)

animals.pop(1)
print(animals)

for i in enumerate(animals):
    print(i)

squares = [x*2 for x in animals]
print(squares)

list1 = [12, 45, 32, 55]
list1.sort()
print(list1)

list1.reverse()
print(list1)