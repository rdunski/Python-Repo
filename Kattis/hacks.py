import sys

n = 0

for x in sys.stdin:
    n=x
    break;

while (int(n) > 0):
    for x in sys.stdin:
        x = x.strip('\n')
        x = x.split(" ")
        if int(x[0]) < int(x[1]) - int(x[2]):
            print ("advertise")
        elif int(x[0]) > int(x[1]) - int(x[2]):
            print ("do not advertise")
        else:
            print ("does not matter")
        n = int(n)-1
        break;
