A = int(input("Enter the number 1: "))
B = int(input("Enter the number 2: "))
C = int(input("Enter the number 3: "))

if A>0 and B<0 and C==0:
    print("True")

elif A<0 and B>0 and C==0:
    print("True")

elif A==0 and B>0 and C<0:
    print("True")

elif A==0 and B<0 and C>0:
    print("True")

elif A<0 and B==0 and C>0:
    print("True")

elif A>0 and B==0 and C<0:
    print("True")


else:
    print("False")