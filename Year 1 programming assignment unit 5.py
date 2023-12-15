#Write program to display your name and perform following operations on it: 
#Display n characters from left. (Accept n as input from the user)
#Count the number of vowels. 
#Reverse it. 

user = input(str("please input your name :"))

vowel = [ "a" , "e" , "i" , "o" , "u" ]


count = 0

for i in vowel :
             if i in user :
                 count += 1
        
             
print(count)

print(user[::-1])
