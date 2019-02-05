import sys

max = 0
counter = 0

if __name__ == '__main__':
    for x in sys.stdin:
        line = [] 
        sum = 0
        z = 1
        x.split('\n')
        if max == 0:                    # store first line of input to a counter
            max = int(x)
            continue
        for y in x:                     # take the large number and parse it into a list
            try:
                line.append(int(y))
            except ValueError:          # catching new line character
                break
        line.reverse()                  # reverse to ease calculations
        while z < len(line):            # step until end of list
            newInt = 0                  # temp variable to store digits that exceed 9 when multiplying
            if line[z]*2 >= 10:
                temp = str(line[z]*2)
                for w in temp:          # step through the temp number for both digits
                    newInt += int(w)    # add the digits together
                line[z] = newInt        # reassign the list at z index
            else:
                line[z] = line[z]*2     # if index z * 2 <= 9, then just reassign to that value
            z += 2                      # step every other element
        for i in line:
            sum += i                    # add all the new numbers together
        if sum % 10 == 0:               # now check if divisible by 10
            print("PASS")
        else:
            print("FAIL")
        counter += 1
        if counter == max:              # when counter reaches the max value as before, exit the program
            exit(0)