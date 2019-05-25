import sys

for x in sys.stdin:
    x = x.strip('\n')
    x = x.split(" ")
    a = list(x[0])
    a.reverse()
    a = "".join(a)
    b = list(x[1])
    b.reverse()
    b = "".join(b)
    if a > b:
        print(a)
    else:
        print(b)
    break;
