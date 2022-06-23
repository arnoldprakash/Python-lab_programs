choice=int(input("Enter ur choice: \n1. perfect number \n2.armstrong number \n3.palindrome"))
if(choice==1):
    n=int(input("enter a number"))
    i=2
    sum=1
    while (i<=n/2):
        sum+=i
        i=i+1
    if(sum==n):
        print(n,"it is a perfect number")
    else:
        print("it is not a perfect number")

elif(choice==2):
    num=(input("enter a number"))
    order=len(num)
    num=int(num)
    sum=0
    temp=num
    while(temp>0):
        dig=temp%10
        sum=sum+(dig**order)
        temp=temp//10
    if(num==sum):
        print(num,"it is an armstrong number")
    else:
        print(num,"it is an armstrong number")

elif(choice==3):
    num=(input("enter a number"))
    if(num==num):
        if(num==num[::-1]):
            print(num,"it is a palindrome")
        else:
            print(num,"it is not palindrome")

else:
    print("invalid input",choice)
