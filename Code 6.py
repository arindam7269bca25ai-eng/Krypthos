""" 
To join the Alchemist's Guild, your entry score must be over 70. However, if you have a special recommendation (a true/false value), 
you only need a score over 50. But, a perfect score of 100 makes you a 'MASTER' regardless of recommendation. Otherwise, you're an 'APPRENTICE' 
if you pass, or 'REJECTED'.
"""


X = int(input("Enter your score:"))
B = bool(input("Special Recommendation (True/False):"))

if X>70:
    print("You are APPRENTICE")

elif X==100:
    print("You are MASTER")

elif X==50 and B==True:
    print("You are APPRENTICE")

else:
    print("You are REJECTED")