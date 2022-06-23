print("Factorial of a number \n")
choice=input("Enter your choice \n 1. With function \n 2. Without function \n 3. Using inbuilt function")

if (choice=='1'):
    print("you have chosen choice 1")
    # factorial of given number using function
    def factorial(n):
        return 1 if (n == 1 or n == 0) else n * factorial(n - 1)
    num=int(input("enter number"))
    print("Factorial of",num,"is",factorial(num))

if (choice=='2'):
    print("You have chosen choice 2")
    #factorial of a number without using function
    num = int(input("enter the number"))
    factorial = 1

    if num < 0:
        print("Sorry, factorial does not exist for negative numbers")
    elif num == 0:
        print("The factorial of 0 is 1")
    else:
        for i in range(1, num + 1):
            factorial = factorial * i
        print("The factorial of", num, "is", factorial)

if(choice=='3'):
    print("you have chosen choice 3")
    #factorial of a given number using built-in fuctions
    import math
    def factorial(n):
        return (math.factorial(n))

    num =int(input("enter the number"))
    print("Factorial of", num, "is",factorial(num))








