
def countup( n ) :

    if n >= 0 :

        print('Blastoff')

    else:

        print(n)   

        countup (n + 1)  

        

print(countup(-20))

#Explanation : if the number is negative, it start to countdup till zero as shown below in the output

 



Q2 :

denom = int(input(" Please Input Denominator :"))

numer = int(input( " Please input Numerator :"))



if numer == 0:

    print(" Can't divide by zero")

   

else :

    answer = denom / numer

    print(answer)



#Explanation : if you allow the user to divide by zero it will create a runtime error, which is not user – friendly that is why we need to catch the error to make it user friendly.



 









