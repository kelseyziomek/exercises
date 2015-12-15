def add(a,b):
    print "Adding %d + %d" % (a,b)
    return a+b

def subtract(a,b):
    print "Subtracting %d - %d" % (a,b)
    return a - b

def multiply(a,b):
    print "Multiplying %d * %d" % (a,b)
    return a*b

def divide(a,b):
    print "Dividing %d / %d" % (a,b)
    return a / b

print "Let's do some math with functions!"

age = add(30,5)
height = subtract(70,10)
weight = multiply(60, 2)
iq = divide(240, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)

