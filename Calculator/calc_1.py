a = int(input("Enter first number "))
b = int(input("Enter second number "))
print "Select any one of the following:"
print "1. Addition"
print "2. Subtraction"
print "3. Multiplication"
print "4. Division"
choice = int(input())
if choice == 1:
    print "The addition of",a,"&",b,"is",a + b 
elif choice == 2:
    print "The subtraction of",a,"&",b,"is",a-b
elif choice == 3:
    print "The multiplication of",a,"&",b,"is",a*b    
elif choice == 4:
    if b == 0:
        print "Division by zero is not possible!"
    else:
        print "The division of",a,"&",b,"is",a/b        
else:
    print "Invalid input"