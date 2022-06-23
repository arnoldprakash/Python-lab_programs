choice=input("Enter your choice \n 1. tuples operatoins \n 2. list operations \n 3. Dictionary\n 4.exit")

if(choice=='1'):
    #tuples operations demo
    choice1=input("You have chosen tuple operations\n1.Creation of tuples\n2.Acessing tuples element\n3.Assigning multiple variables\n4.To exchange values in one tuples\n5.Conversion of list to tuples")
    if(choice1=='1'):
        #Creation of tuples
        print("\nCreation of tuples")
        marx_tuples=1,2,3
        print("marx_tuples: ",marx_tuples)
    if(choice1=='2'):
        #Acessing a tuples elemet
        print("\nAcessing tuples element")
        tuple1=1,2,3
        print("tuple1: ",tuple1)
        print("tuple1[0]: ",tuple1[0])
        print("tuple1[-1] :",tuple1[-1])
        print("tuple1[2] :",tuple1[2])
    if(choice1=='3'):
        #assinging multiple variables
        print("\nassigning multiple variables")
        marx_tuples = ('grouncho', 'chico', 'harpo')
        print("marx_tuple: ",marx_tuples)
        a,b,c=marx_tuples
        print("a:",a,"b:",b,"c:",c)
    if(choice1=='4'):
        #to exchange values in one
        print("\nexchange values in one tuples")
        password='swordfish'
        icecream='tuti fruti'
        password,icecream=icecream,password
        print("password: ",password,"icecream: ",icecream)
    if(choice1=='5'):
        #Conversion of list to tuples
        print("\nconversion of list to tuples")
        marx_list=['Grouncho','chico','hanpo']
        tuple(marx_list)
        print("type of marx_list", type(marx_list))

if(choice=='2'):
    #list operations
    choice2=input("\nYou have chosen list operations \nchoose what you want to demonstrate \n1. creation of list \n2.list of list \n3.add item \n4.combining lists \n5.swapping of list")
    if(choice2=='1'):
        # creation of list
        print('creating a list')
        weekdays=['monday', 'tuesday', 'wednesday']
        print(weekdays)
    if(choice2=='2'):
        #list of list
        print("list of list")
        small_birds=['humming birds','finch']
        extict_birds=['dodo','passenger pegion']
        all_birds=[small_birds,extict_birds,'macao']
        print("small birds =",small_birds)
        print("extinct birds = ",extict_birds)
        print("all birds = ",all_birds)
        print("all_birds[0]",all_birds[0])
        print("all_birds[0][0]",all_birds[0][0])
        print("all_birds[0][0][0]",all_birds[0][0][0])
    if(choice2=='3'):
        #add item
        print("adding item")
        marxes=["'Grouncho","chico","harpo"]
        others=["grouncho",'karl']
        print("marxes:",marxes)
        print('others :',others)
        print("marxes.append('zeppo'): ")
        print(marxes.append("zeppo"))
        print("marxes.append('others): ")
        print(marxes.append("others"))
    if(choice2=='4'):
        #combining lists
        marxes = ["'Grouncho", "chico", "harpo"]
        others = ["grouncho", 'karl']
        print("combining lists")
        print("marxes.append(others) :")
        print(marxes.extend(others))
        print("marxes=marxes+others: ")
        marxes+=others
        print(marxes)
    if(choice2=='5'):
        #swap 2 list
        a=[1,2,3]
        b=a
        a[0]='surprise'
        print("a after swap: ",a)
        print("b after swap: ",b)
if(choice=='3'):
    #creating dictionary
     choice3=input("\nYou have chosen dictionary operations\n choose which dictionary operation to be done\n 1.creating of dictionary\n 2.adding and changing an item in dictionary\n 3.combining dictionary with update\n 4.convert tuple/list into a dictionary\n 5.deletion of an element in the dictionary/n")
     if(choice3=='1'):
         print("creating a dictionary")
         key_value={1:"one","day":"24-hours",3.14:"pi value"}
         print(key_value)
     if(choice3=='2'):
            print("adding and changing an item in dictionary")
            weekdays={1:"sunday",2:"monday"}
            weekdays[4]="thrusday"
            weekdays[4]="wednesday"
            print(weekdays)
     if(choice3=='3'):
            print("combining dictionary with update")
            weekdays={1:"sunday",2:"monday",3:"tuesday"}
            holidays={7:"saturday",3:"thrusday"}
            weekdays.update(holidays)
            print(weekdays)
     if(choice3=='4'):
            print("convert tuple/list into a dictionary")
            lol=[['a','b'],['c','d'],['e','f']]
            print(dict(lol))
            lot=[('a','b'),('c','d'),('e','f')]
            print(dict(lot))
            tos=('ab','cd','ef')
            print(dict(tos))
     if(choice3=='5'):
            print("deleting an element in the dictionary")
            weekdays={1:"sunday",2:"monday",3:"tuesday"}
            del weekdays[1]
            print(weekdays)
else:
    print("exiting program")
