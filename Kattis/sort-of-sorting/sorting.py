import sys

def func(e):
    return e[:2]                        #returns the first 2 elements of a list/ list of chars in this case

if len(sys.argv) > 1 and sys.argv[1] == "test":     #if testing...
    name = []
    name.append("Marge")
    name.append("Nathan")
    name.append("Jorge")
    name.append("Ned")
                                        #output should be -> Jorge, Marge, Nathan, Ned
    name.sort(key=func)                 #sort it using the first 2 letters in each element
    assert name[0] == "Jorge"
    assert name[1] == "Marge"
    assert name[2] == "Nathan"
    assert name[3] == "Ned"
    print("Test passed, list contents are:\n")
    for x in range(0, len(name)):       #print out the list just to make sure
        print(name[x])
    print("\n")
else:
    name = []
    for line in sys.stdin:              #keep looping through standard input until the end
        line = line.strip("\n")         #take off new line to avoid problems
        try:
            line = int(line)            #if the line is an integer, don't append it to the name list
        except ValueError:
            name.append(line)           #if it's a string, append it the the list
            continue
        name.sort(key=func)             #sorts the list after all necessary elements are appended
                                        #by the first two letters of each element
        for x in range(0, len(name)):   #Loop through the list and print the values in sorted order
            print(name[x])
        print("\n")
        if int(line) == 0:              #if the last line is integer 0, the input is confirmed to end
            break                       #so break out of the for loop
        name.clear()                    #clear the list if there are more elements in stdin to sort