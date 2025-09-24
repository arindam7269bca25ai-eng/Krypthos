A= int(input("Enter your income:"))

S1=(500*10/100)
S2=(500*15/100)
S3=(A-1000)*20/100

if A==0:
    print("You are EXEMPTED from TAX")

elif A>0 and A<=500:
    X = A*10/100
    B = A+X+S1
    print(f"Your TAX is {X} and your TOTAL INCOME after TAX is {B}")

elif A>500 and A<=1000: 
    C = A-500
    X = A*15/100
    B = A+X+S1+S2
    print(f"Your TAX is {X} and your TOTAL INCOME after TAX is {B}")

elif A>1000:
    C = A-1000
    X = A*20/100
    B = A+S1+S2+S3+X
    print(f"Your TAX is {X} and your TOTAL INCOME after TAX is {B}")

