import sys

x = 0
y = 0

for i in sys.stdin:
    if x == 0:
        x=i
    else:
        y=i
    if not x == 0 and not y == 0:
        break;

if int(x) / 1 > 0 and int(y) / 1 > 0:
    print(1)
elif int(x) / 1 < 0 and int(y) / 1 > 0:
    print(2)
elif int(x) / 1 < 0 and int(y) / 1 < 0:
    print(3)
elif int(x) / 1 > 0 and int(y) / 1 < 0:
    print(4)
