
a = 'single line '
print(a)

b = """
   This is 
   Multi Line
   String"""
print(b)

for x in a:
   print(x)

print(len(a))
print("line" in a)

if "line" in a:
   print('Yes, Line is here')

print('line' not in a)

b = '  hello world'
print(b[:5])

print(b.upper())
print(b.strip().upper())

print(b.replace('hello', 'fantastic'))

number = 1
number2 = 2
str =  'amar sonar bangla'
str2 =  'amar sonar bangla {}  {}'
print(f'{number}: {str}' )

d = str2.format(number, number2)
print(d)

y = 200
print(isinstance(y, int))