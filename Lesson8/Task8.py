import random
a = [random.randint(0,5) for i in range(10)]
b = [random.randint(-5,0) for i in range(10)]
c = tuple(a+b)
print(c)
print(c.count(0))

