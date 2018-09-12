# without user input
# using three variables
a = 10
b = 20
c = a + b
print "The addition of the numbers is", c

# using 2 variables
a = 10 
b = 20
print "The addition of the numbers is", a + b

# with user input 
# using three variables
a = int(input("Enter first number "))
b = int(input("Enter first number "))
c = a + b
print "The addition of the numbers is", c

# using 2 variables
# int() - will convert the input into numbers if string is passed!
a = int(input("Enter first number "))
b = int(input("Enter first number "))
print "The addition of the numbers is", a + b

#Some explanation
# CASE 1
# input => "10" "20" (Giving input as string)
# output => 30

# CASE 2
# input => 10 20 (Giving input as numbers)
# output => 30

# CASE 3
# input => 10 "hello10" (Giving one input as number and other as string with alphabets and numbers)
# output => Error because int() wont be able to convert "hello10" into number!

###################################################################################

a = input("Enter first number ")
b = input("Enter first number ")
print "The addition of the numbers is", a + b

# Here if you put 10 & 20 answer will be 30
# Here if you put "10" & "20" answer will be 1020
# Here if you put "Hello" & "World" answer will be "HelloWorld"
 
###################################################################################