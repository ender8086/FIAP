from math import sqrt
print("Bhaskara")
a=int(input("Type A value: "))
b=int(input("Type B value: "))
c=int(input("Type C value: "))
if a==0:
    print("Simple equation: ({0})x+({1}) = 0".format(b,c))
    if b==0:
        print("Not a valid equation")
    else:
        x = -c/b
        print("x = {0:.1f}".format(x))
else:
    print("Second grade equation: ({0})x²+({1})x+({2}) = 0".format(a,b,c))
    d = (b**2)-(4*a*c)
    print("Delta value is: {0:.1f}".format(d))
    if d<0:
        print("Non real root.")
    elif d>0:
        x1 = (-b + sqrt(d))/(2*a)
        x2 = (-b - sqrt(d))/(2*a)
        print("The roots are: x1 = {0:.20f} and x2 = {1:.20f}".format(x1,x2))