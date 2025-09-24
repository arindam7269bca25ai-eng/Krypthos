"""
A goblin demands a toll. If a traveler has more than 50 silver OR more than 5 gold, they pay the 'RICH TAX'.
 If they have less than 10 silver AND 0 gold, they are 'TOO POOR' and pass free. Everyone else pays the 'NORMAL TOLL'. 
 What is the traveler's fate?

"""

G = int(input("Enter the amount of GOLD you have: "))
S = int(input("Enter the amount of SILVER you have: "))
if G>5 or S>50:
    print("RICH TAX")
elif G==0 and S<10:
    print("TOO POOR")
else:
    print("NORMAL TOLL")