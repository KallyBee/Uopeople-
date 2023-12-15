
def print_circum(radius):
       x = 2 * 3.14 * radius
       return x
   print(print_circum(2)

 


   def print_circum(radius):
        x = 2 * 3.14 * radius
       return x
   print(print_circum(3))

 


   def print_circum(radius):
        x = 2 * 3.14 * radius
        return x
   print(print_circum(4))


 

                                 Part 2
A)	
Item1 = 200
Item2 = 400
Item3 = 600

Def individual(value1):
    
    Return (value1)

Def combo(value1, value2):
    
    If value1 == “it1”:
        
        firstChoice = item1
        
    elif value1 == “it2”:
        
        firstChoice = item2
        
    else:
        
        firstChoice = item3
        
    if value2 == “it1”:
        
        secondChoice = item1
        
    elif value2 == “it2”:
        
        secondChoice = item2
       
    elif value2 == “it3”:
        
        secondChoice = item3
        
    total = firstChoice + secondChoice
    percent = (10/100)*total
    discountPrice = total – percent
    
    return (discountPrice)
    
def gift():
    
    total = item1 + item2 + item3
    percent = (25/100)*total
    discountPrice = total – percent
    
    return (discountPrice)
    
    
noOfProduct = int(input(“Availbale items are (3), how many items do you want to buy: “))

if noOfProduct == 1:
    
    choice = input(“pick your item:\nitem 1 (worth 200) = it1\nitem 2 (worth 400) = it2\nitem 3 worth (600) = it3\nAwaiting input: “)
    
    if choice == “it1”:
        
        print (“\n item 1 = “, individual(item1))
 

        
    elif choice == “it2”:
        
        print(“\n item 2 = “, individual(item2))
 

        
    elif choice == “it3”:
        
        print(“\n item 3 = “, individual(item3))

 

        
    else:
        
        print (“\nIncorrect selction\nThanks for using this program and bye”)
    
    
elif noOfProduct == 2:
    
    print(“Available items are:\nitem 1 (worth 200) = it1\nitem 2 (worth 400) = it2\nitem 3 worth (600) = it3”)
    
    choices = [“it1”, “it2”, “it3”]
    
    choice1 = input(“\nwhat is your first choice: “)
        
    choice2 = input(“\nwhat is your second choice: “)
    
    if (choice1 or choice2) not in choices:
        
        print (“\nWrong selection entered\nThanks for using the program and bye”)
     
    elif choice1 == choice2:
        
        print(“\ncan’t make same choice twice\nThanks for using the program and bye”)
        
    else:
        
        print(“\n “, combo(choice1,  
 
 
 



elif noOfProduct == 3:
    
    print (“\n giftpack = “, gift())

 


    
else:
    
    print (“incorrect selection\nThanks for using the programe and bye”)





