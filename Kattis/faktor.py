import sys

for x in sys.stdin:
    x = x.split(" ")
    if not x[0] == 1:
        print((int(x[0])*(int(x[1])-1)+1))
    else:
        print(x[1])
    break;
