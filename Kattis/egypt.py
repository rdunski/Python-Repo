import sys

for line in sys.stdin:
    if line == "0 0 0\n":
        break;
    line = line.strip('\n')
    line = line.split(" ")
    for i in line:
        line[line.index(i)] = (int(i))
    line.sort()
    if (int(line[0])**2) + (int(line[1])**2) == (int(line[2])**2):
        print("right")
    else:
        print("wrong")
