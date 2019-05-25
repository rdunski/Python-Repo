import sys

if __name__ == '__main__':
    for x in sys.stdin:
        x.strip('\n')
        line = x.split()
        for y in line:                                          #read each integer in input line
            try:
                temp = 0                                        # comparison value, reset for every y
                if line.index(y)+1 <= len(line)-1:              #check if there are numbers in front of y
                    for z in range(line.index(y)+1, len(line)): #find all numbers in front of y and add them to temp
                        temp += int(line[z])
                if line.index(y) >= 1:                          #check if there are numbers behind y
                    for w in range(0, line.index(y)):           # find all numbers behind y and add them to temp
                        temp += int(line[w])
            except IndexError:                                  #just in case
                pass
            if int(y) == int(temp):
                print(y)                                        #when found, output the correct sum within the line
                break                                           # move to next line or eof
        