import sys

dummy = 0
bitcount = 0
digitlist = []
bitlist = []

for x in sys.stdin:
    x.strip('\n')                           # take newline out
    if dummy == 0:
        dummy = x                           # take the first integer they give and store it in a dummy variable
    else:
        intstr = list(x)                    # take the integer in one line and convert it to a list
        for y in intstr:                    # iterate through each digit
            digitlist = list(digitlist)     # make sure that the digit list is in fact a list to use list methods
            digitlist.append(y)             # append each digit onto the last one for binary comparison
            digitlist = ''.join(digitlist)  # convert list to string for string methods
            bitcount = bin(int(digitlist))  # first convert bilist into an integer, and then into a binary string
            bitcount = str(bitcount)        # convert bitcount to normal string
            bitcount = bitcount.count("1")  # count the amount of 1 bits in the string
            bitlist.append(bitcount)        # append to a comparison list for later interpretation
        digitlist = list(digitlist)         # after the string is interpreted, change digitlist back to a list type
        digitlist.clear()
        bitlist.sort()                      # sort the final bitcounts found
        print(bitlist.pop())                # print the largest value
    bitlist.clear()
