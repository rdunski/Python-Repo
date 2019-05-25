import sys

for x in sys.stdin:
    if int(x) % 2 == 0:
        print("Bob")
    else:
        print("Alice")
        
