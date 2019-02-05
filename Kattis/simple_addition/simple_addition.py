import sys
a = 0
b = 0
for x  in sys.stdin:
    if a == 0:
        a = x
        continue
    if b == 0:
        b = x
    total = int(a) + int(b)
    print(total)