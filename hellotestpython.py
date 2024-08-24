"""num_string = '12'
num_integer = 23

print("Data type of num_string before Type Casting:",type(num_string))

# explicit type conversion
num_string = int(num_string)

print("Data type of num_string after Type Casting:",type(num_string))

num_sum = num_integer + num_string

print("Sum:",num_sum)
print("Data type of num_sum:",type(num_sum))"""


'''num1 = 5
print(num1, 'is of type', type(num1))

num2 = 5.42
print(num2, 'is of type', type(num2))

num3 = 8+2j
print(num3, 'is of type', type(num3))'''

#write the code for testing assigning value!!!
 
'''name = "Samananda"
print(name)'''

#testing with own code some add or algebra code 
# add 
'''a = 2
b = 3 
sum = a+b 
print(sum)'''
#algebra 
'''x = 2 
z = x + 3
print(z)'''  
# testing string connection and showing data type 
#x = "samnananda"
#print("Nice "+ x)
#print(type(x))


#connection with the two string 
#name = "Samananda"
#sur_name = "Thoudam"
#full_name = name + " " + sur_name 
#print((full_name))

#change the data_TYPE 
#roll_no = 34
#full_name = "Thoudam Samananda Singh"
#student =  full_name +" " + str (roll_no)
#print(student)

#boolean checking 
#male = True
#print(male)

#Using all the varaible in one code 
'''first_name = "Samananda "
last_name ="Thoudam "
age = 21 
male = True 
full_name = first_name + last_name 
print(full_name)
print(age)
print(male)'''

#using in the string  methode in python
#name = "I Love You "
#1 . find the length for that string  / space is also count length 
#print(len(name )) 
#2 . find the character in the string 
#print(name.find("S"))
#3 . Change the string into capital 
#print(name.capitalize())
#4 . Check the string is include  digit or not 
#print(name.isdigit())
#5 . all the string is modified into all upper_case\
#print(name.upper())
#6 . all the string is modified into all lower_case
#print(name.lower())
#7 .Checked all the string is alphabet or not 
#print(name.isalpha())
#8. Count the character / string  // it is case sensitive
#print(name.count("a"))
#9 It can replace what we want on the string 
#print(name.replace("a","r"))
# it can also dispaly multiple string 
#print(name*100)

#type casting = convert the data type of a value to another data type 
#x = 1 #int 
#y = 2.0 #float 
#z = "3"  #str
#x = str(x)
#y = str(y) 
#z = str(z)
#print(x)
#print(y)
#print(z*4)

# let check how the input from the user 
#name = input("What is your name :")
#age = int(input("How old are you ??:"))
#age = age + 1
#height = float(input("How tall are you "))
#print("hello "+name)
#print("You are "+str(age)+" old ")
#print("You are "+str(height)+ ".cm tall")\

# PYTHON USING MATHS 

import math
pi = 3.14
x = 3 
y = 6 
z = 1
#round function it is  round up the value means if the input is 3.14 is out is only 3 
#print(round(pi))
#In the ceil function is also the round up the nearest high value 
#print(math.ceil(pi))
#In the floor function is also same as round funtion it give nearest to lower value
#print(math.floor(pi))
# In this absolute value to giving the value to how far from the zero in positive value 
#print(abs(pi))
# In this power methode it give result for power value of the given input 
#print(pow(pi,4)) 
#In this square root funtion is to  find the root value for given no. 
#print(math.sqrt(pi))
# In this minimun function to find the minimum value  
#print(min(pi,x,y,z))
#In this maximum function is to find the value for the maximum value
#print(max(x,y,z,pi))
# this are main function in maths module 


#slicing methode 
#creating a substring by extraction from another string 
# indxing[] 
#  [start : stop : step ]

#name = "Samananda Thoudam "
#first_name = name[0:3] #[0:3S]
#last_name = name[9:]  #[4:1]
#try_name = name[::4]  #[0:end:4]
#reverse_name = name[::-1] #[0:end:-1]
#print(reverse_name)

# slice () methode 

'''website= "http://facebook.com"
website1= "http://google.com"

tryslice = slice(7,-4)
print(website[tryslice])
print(website1[tryslice])'''

# Next we learn the if and else in python
# if statement = a block of code that will if it is condition is true only
#age = int(input("How old are you ??"))
#if age >= 21:
 # print("You are an adult !! ")
#elif age < 0 :
  #print(" You are not not born yet !!")
#else :
    #  print("You are minor !!") 



# logical  operator (and,or,not) = used to check if two or more conditional statement  
'''temp = float(input("how old are you "))
if temp >=0 and temp <=30:
    print("You are not too old ")
elif temp >= 70 or  temp <=90 :
    print("You are senior right now ") '''

# while loop = a statement that will execute it is block of code
#                as long as it is condition remain true 
'''while 1 ==  :
    name = print("-----hello world -----")'''

# try to using the while loop 
#name = "" 
#password =""
#name = input("Username: "+name)
#while len(password ) == 0: 
 #        password = input ("Enter your password : ")
#print("Thanks for entering password !")        

# next we learn for loop
# for loop  = statement that will excute it is block of code 
 # limited amount of time 
#for loop = limited 
#while loop = unlimited 

#for i in range(10):
  #print(i+1)

#for i in range(1,3):
#    print(i)

#import time  time moduled 
#for i in range(10,0,-1):
#    print(i)
#    time.sleep(2)
#print("GO!!!!!")


#  nested loop in python 
# nested loop = The "inner loop" wil finish all of it's 
#  iterations before finishing one iteration of the "outer loop"
'''row = int(input("How many row "))
column =int(input("How many column need ?? "))
t = input("What you want to print ")
for i in range(row):
  for j in range(column):
     print(t,end="")
  print()'''

#loop control statements = chnage a loop execution from its normal sequence
# break = used to terminate  the loop entirely 
# continue = skips to the next iteration of the loop .
# pass =  does nothing , acts as a placeholder 

