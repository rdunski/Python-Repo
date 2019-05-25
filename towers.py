import string
import sys
import re

compList = []

list=["null"]
count=0

def partition(sortList,start,end):
    i = (start-1)
    pivot = sortList[end]

    for j in range(start,end):
        if sortList[j][1] < pivot[1]:
            if sortList[j][2] <= pivot[2]/6.75 or sortList[j][2]*6.75 <= pivot[2]:
                i = i+1
                sortList[i],sortList[j] = sortList[j],sortList[i]

        if sortList[j][2] <= pivot[2]/6.75 or sortList[j][2]*6.75 <= pivot[2]:
                i = i+1
                sortList[i],sortList[j] = sortList[j],sortList[i]

    sortList[i+1],sortList[end] = sortList[end],sortList[i+1]
    return (i+1)

def quickSort(sortList,start,end):
    try:
        if sortList[start][1] < sortList[end][1]/6.75 or sortList[start][1]*6.75 < sortList[end][1]:
            pi = partition(sortList,start,end)

            quickSort(sortList,start,pi-1)
            quickSort(sortList,pi+1, end)

            return sortList
    except:
        pass

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

secondList=list

for line in list:
    try:
        line=int(line)
        compList.append((line,line,line))
    except ValueError:
        numline = line.split("^")
        base=int(numline[0])
        numline.reverse()

        sum=pow(int(numline[1]),int(numline[0]))

        compList.append((line,base,sum))

        print(compList)

quickSort(compList,0,len(compList)-1)

for line,base,sum in compList:
    print(line)
print(compList)
