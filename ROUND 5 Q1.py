"""
You have n bulbs, all initially OFF. On the 1st pass you toggle every bulb; on the 2nd pass you toggle every 2nd bulb; on
 the 3rd pass you toggle every 3rd bulb... continuing until the nth pass. At the end, which bulbs remain ON? Hint: perfect squares only. 
 What is the pattern and why do those bulbs remain lit? (Click the riddle title to start the 15:00 timer)

"""
n = int(input("Enter the number of bulbs: "))
bulbs = [False] * n
for pass_ in range(1, n + 1):
     for i in range(pass_ - 1, n, pass_):  
            bulbs[i] = not bulbs[i]
on_bulbs = [i + 1 for i, bulb in enumerate(bulbs) if bulb]
print("Bulbs that remain ON:", on_bulbs)












