a = 23
b = 45
c = a + b
d = a / b
print("Sum is",c)
print("Sum of", a, "and", b, "is", c)

print("Sum is %d"%c)
print("Sum of %d and %d is %d"%(a,b,c))

print("Sum is {}".format(c))
print("Sum of {} and {} is {}".format(a,b,c))
print("Sum of {1} and {2} is {0}".format(c,a,b))

print("Div is {:.2f}".format(d))

#f-strings - format strings
print(f"Sum of {a} and {b} is {c}")











