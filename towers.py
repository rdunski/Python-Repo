import string
import sys

compDict = {"null":0}

list=["null"]
count=0

for line in sys.stdin:
    count=int(line)
    break

for line in sys.stdin:
    line = line.strip('\n')
    if list[0] == "null":
        list[0]=line
        count-=1
    else:
        list.append(line)
        count-=1
    if count == 0:
        break

print(list)

for line in list:
    try:
        line=int(line)
        if "null" in compDict.keys():
            compDict[line]=line
            compDict.pop("null")
        else:
            compDict[line]=line
    except ValueError:
        newline = line.split("^")
        newline.reverse()
        sum=pow(int(newline[1]),int(newline[0]))
        if "null" in compDict.keys():
            compDict[line]=sum
            compDict.pop("null")
        else:
            compDict[line]=sum
        print(compDict)