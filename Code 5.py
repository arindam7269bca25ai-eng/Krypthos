X = int(input("Enter the Temprature: "))

if X<0:
    print("Blue")
elif X>100:
    print("Red")
elif X==50:
    print("Purple")
else:
    print("Clear")