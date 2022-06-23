import math
import cmath
a=int(input("enter the value od a"))
b=int(input("enter the value of b"))
c=int(input("enter the value of c"))
d=(b**2)-(4*a*c)
if (d<0):
    sol1=(-b+cmath.sqrt(d)/(2*a))
    sol2=(-b-cmath.sqrt(d)/(2*a))
    print("the roots are",sol1,sol2)
elif(d>0):
    sol1=(-b+math.sqrt(d)/(2*a))
    sol2=(-b-math.sqrt(d)/(2*a))
    print("the roots are{:6.2f} and {}".format(sol1,sol2))
else:
    sol1=-b/(2*a)
    sol2=sol1
    print("the root are {} amd {}".format(sol1,sol2))
