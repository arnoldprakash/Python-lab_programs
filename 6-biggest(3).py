print("enter 3 numbers")
a=int(input())
b=int(input())
c=int(input())
if(a>b):
    if(a>c):
        print(a,"is greater than",b,"and ",c)
elif(b>a):
    if(b>c):
        print(b,"is greater than",a,"and",c)
    else:
        print(c,"is greater than",b,"and",a)

