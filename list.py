a = [1,2,3,4,454,5,5,45,45,4,5]
print(type(a))

b = list((1,2,3,43,4,65445))
print(type(b))

print(b[-1])
print(b[2:5])

for x in b:
   print(x, 'x in b')

b[0] = 'oops'
b[1:10] =['sonar', 'bangla']
print(b)
print(len(b))


mylist = ['a','b','c']
mylist.insert(2, 'oops')
mylist.append('hello')
print(mylist)

one = [1,2,3]
two = [4,5,6]

extended = one.extend(two)
print(extended,'extended return')
print(one)
print(two)


myList = ['a','b','c']
myTuple = (1,2,3,4,5,6)
myTuple2 = ('d','c','d')

myList.extend(myTuple2)
print(myList, 'myList')

myList.remove('d')
print(myList)

myList.pop()
print(myList)

g = [1,2,3,4,5]
del g[0]
del g[len(g)-1]

print(g)

g.clear()
print(g)


a = ['a','b','c','d']

for x in range(len(a)):
   print(x, a[x])

i=0
while i < len(a):
   print('while', i)
   i = i+1

[print(x) for x in a]

obj = {
   'name' : 'masud',
   'roll' : 11
}

[print(x, obj[x]) for x in obj]

oops = [x for x in obj]
print(oops)


arrOfObject = [
   {
      'name' : 'masud',
      'roll' : 5
   },
   {
      'name' : 'masud',
      'roll' : 7
   },
   {
      'name' : 'masud',
      'roll' : 3
   },
   {
      'name' : 'masud',
      'roll' : 15
   },
   {
      'name' : 'masud',
      'roll' : 17
   },
]

x = [x for x in arrOfObject if x['roll'] <10]
print(x)


y = [x for x in range(100)]
print(y)

odd = [x  if not x % 2 == 0 else None for x in range(1,101)]
print(odd)
even = [x if x % 10 != 0 else f"{int(x/10)} Ten" for x in range(1,101) if x % 2 == 0]
print(even)


a = [5,2,7,2,54,8,56]
b = a
b.sort(reverse=True)
print(a, 'unsorted')
print(b, 'sorted')
