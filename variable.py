x = int(10)
x = 'hello'

# Case sensitive
a = 'a'
A = 'A'

#Add multiple value to multiple variable
fruit,animal = "mango", "cat"
print(fruit, 'fruit')
print(animal, 'animal')

#Add single value to multiple variable

d=e=f = "same here"

print(d, 'd')
print(e, 'e')
print(f, 'f')

#unpack collection
fruits = ['amar', 'sonar', 'bangla']
g, h, i = fruits

print(g, 'g')
print(h, 'h')
print(i, 'i')

print(f"{g} {h} {i}")

print(10+5)
print("amar "+"sonar")

#don't do this
#print(10+"sonar")


#global and scope variable

aa = 'outer function'
def myfunc():
   aa = 'inner function'
   print(aa)

myfunc()
print(aa)

aa = 'outer function'
def myfunc2():
   global aa
   aa = 'inner function'
   print(aa)

myfunc2()
print(aa)