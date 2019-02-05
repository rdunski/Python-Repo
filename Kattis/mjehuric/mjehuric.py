import sys


def swap(numlist):                                                      #function to repeatedly swap the indices of the given list
    for y in numlist:
        strlist = []
        try:                                                            #catching out of range error for list
            if y > numlist[numlist.index(y) + 1]:                       #compare index with the one after it
                temp1 = y                                               #if y > the next index, swap them
                temp2 = numlist[numlist.index(y) + 1]
                numlist[numlist.index(y) + 1] = temp1
                numlist[numlist.index(y)] = temp2
                for z in numlist:                                       #formating for later output
                    strlist.append(str(z))
                if not (len(sys.argv) > 1 and sys.argv[1] == "test"):   #only print out each step if not testing
                    print(" ".join(strlist))
                continue
        except IndexError:                                              #if caught, end of list is reached, so break out of loop
            break


if len(sys.argv) > 1 and sys.argv[1] == "test":                         #if testing...
    sortlist = [1, 2, 3, 4, 5]
    intlist = [2, 3, 4, 5, 1]
    while not intlist == sortlist:                                      #swap values until its sorted
        swap(intlist)
    assert (intlist == sortlist)                                        #the end list should = the pre-sorted list
    print("test 1 passed")
    intlist = [2, 1, 5, 3, 4]                                           #test for a second case
    while not intlist == sortlist:
        swap(intlist)
    assert (intlist == sortlist)
    print("test 2 passed")
    exit(0)                                                             #quit out and skip the actual program
for x in sys.stdin:
    sortlist = []
    intlist = []
    x.strip('\n')
    numlist = x.split()
    for z in numlist:                                                   #take the str list and assign it into int lists
        sortlist.append(int(z))
        intlist.append(int(z))
    sortlist.sort()                                                     #sort the list beforehand for comparison
    while not intlist == sortlist:                                      #keep swapping values until sorted
        swap(intlist)
    break                                                               #should be no more than one line, so end the program
