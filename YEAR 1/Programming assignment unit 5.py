
user = input(str("please input your name :"))

vowel = [ "a" , "e" , "i" , "o" , "u" ]


count = 0

for i in vowel :
             if i in user :
                 count += 1
        
             
print(count)

print(user[::-1])
