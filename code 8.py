"""
A guardian has three heads, each speaking a number. You can only pass if the sum of ANY two heads' numbers is greater than the third head's
 number. This must be true for all three combinations! If you can pass, print 'PROCEED', otherwise, print 'HALT'.

"""


A = int(input("Enter your number 1:_"))
B = int(input("Enter your number 2:_"))
c = int(input("Enter your number 3:"))

if A+B == c or B+c == A or A+c == B:
    print("Pass")
else:
    print("HALT")