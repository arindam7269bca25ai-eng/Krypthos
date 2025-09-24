X = int(input("Enter the YEAR: "))
if X%4==0 and (X%100!=0 or X%400==0):
    print(f"{X} is a LEAP YEAR you will see 'GRYPHON SIGHTING'")
else:
    print(f"{X} is NOT a LEAP YEAR/ QUIET YEAR")