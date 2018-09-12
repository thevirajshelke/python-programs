num = int(input("Enter a number "))
num1 = num
arm = 0
while num1:
    digit =  num1 % 10
    num1 = num1 / 10
    arm = arm + digit * digit * digit
if arm == num:
    print "The number",num,"is an Armstrong Number!!"
else:
    print "The number",num,"is not an Armstrong Number!!"