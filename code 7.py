"""
You are at coordinates (x, y) in a maze. You can escape if you are on the edge (x=0 or y=0) but NOT if you are in a corner
 (x=0 AND y=0). If you can escape, print 'ESCAPE'. Otherwise, print 'TRAPPED'.

"""

X = int(input("X coordinate: "))
Y = int(input("Y coordinate: "))

if X==0 or Y==0:
    print("Escape")

elif X==0 and Y==0:
    print("TRAPPED")

else:
    print("WRONG COORDINATES")