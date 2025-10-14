'''num = int("10")
print(num)

price = float("3.14")
print(price)

z = complex(2, 3)
print(z)

text = str(123)
print(text)

flag = bool(1)
print(flag)

lst = list((1, 2, 3))
print(lst)

tpl = tuple([1, 2, 3])
print(tpl)

s = set([1, 2, 2, 3])
print(s)

fs = frozenset([1, 2, 3])
print(fs)

d = dict(name="Priya", age=25)
print(d)

b = bytes("Hello", "utf-8")
print(b)
ba = bytearray("Hello", "utf-8")
print(ba)
mv = memoryview(b'abc')
print(mv)

x = abs(-5)
print(x)

p = pow(2, 3)
print(p)

r = round(3.567, 2)
print(r)

q, rem = divmod(9, 2)
print(q , rem)

total = sum([1, 2, 3])
print(total)

smallest = min([5, 3, 8])
print(smallest)

largest = max([5, 3, 8])
print(largest)

l = len("hello")
print(l)

for i in range(5):
    print(i)

for i,v in enumerate(['a','b']):
    print(i,v)

for x,y in zip([1,2],[3,4]):
    print(x,y)

result = list(map(str, [1,2,3]))
print(result)

filtered = list(filter(lambda x:x>2, [1,3,2]))
print(filtered)

sorted_list = sorted([3,1,2])
print(sorted_list)

rev = list(reversed([1,2,3]))
print(rev)
print(all([True, 1, 3]))
print(any([0, False, 5]))
print("Hello, QA Team")
name = input("Enter your name: ")
msg = "{} is {}".format("Age", 25)'''

print(type(5))

print(id("abc"))

print(isinstance(5, int))
print(issubclass(bool, int))
print("This is a backslash: \\")
print('It\'s a test')
print("He said \"Hi\"")
print("\a")
print("Hello\b!")
print("Hello\fWorld")
print("Hello\nWorld")
print("Hello\rWorld")
print("Name:\tPriya")
print("Hello\vWorld")