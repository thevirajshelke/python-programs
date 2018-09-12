num = int(input("Enter a number "))
num1 = num
rev = 0
while num1:
    digit = num1 % 10
    num1 = num1 / 10
    rev = rev * 10 + digit
if num == rev:
    print "The number",num,"is a plaindrome number!"
else:
    print "The number",num,"is not a plaindrome number!"    