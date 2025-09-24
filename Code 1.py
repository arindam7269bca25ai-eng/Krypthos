X = int(input("Enter your age:"))
y = input("Do you have a royal decree? (yes/no):").lower()

if (X<18):
    print("You are a MINOR")
elif X==25 and y=="yes":
    print("You are a NOBLE")

elif (X>=18 and X<65):
    print("You are an ADULT")

else:
    print("You are a SENIOR CITIZEN")
