#recursively print "Hello, World" 5 times
def hello5(i=0):
    if i < 5:
        print("Hello, World!")
        hello5(i + 1)

hello5()

#but if you're lazy you can also do this
print("Hello, World")
print("Hello, World")
print("Hello, World")
print("Hello, World")
print("Hello, World")