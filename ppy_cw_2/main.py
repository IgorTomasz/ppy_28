a = "Python 2023"
b = a
c = a

print(a == b)
print(b == c)

print(type(a), type(b), type(c))
print(hex(id(a)),hex(id(b)),hex(id(c)))

c = "Java 11"

print(a == b)
print(b == c)

print(type(a), type(b), type(c))
print(hex(id(a)),hex(id(b)),hex(id(c)))


