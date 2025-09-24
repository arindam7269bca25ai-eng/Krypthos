""""A dragon guards three piles of gold: 10, 15, and 20 coins. A knight can only pass if the total is NOT exactly 45, 
AND the first pile has exactly 10 coins. Tell the knight if he should 'PASS' or 'FAIL'."""
A = int(input("Enter the number of coins pile 1:"))
B = int(input("Enter the number of coins pile 2:"))
C = int(input("Enter the number of coins pile 3:"))

if A+B+C == 45:
    print("FAIL")
elif A+B+C != 45 and A==10:
    print("PASS")