import sys
import math

result = 3

for x in sys.stdin:
    if not int(x) == 1:
        print(pow((int(x)*int(result))-1,2))
    else:
        print(result*result)
