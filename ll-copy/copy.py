import sys

infile = open("/home/esquire/Documents/test", "rb") # Read Binary
outfile = open("/home/esquire/Documents/copyTest", "wb") # Write Binary

def read_bytes(filename, blocksize=1024):
    while True:
        chunk = bytearray(filename.read(blocksize))
        if chunk:
            yield chunk   #Yield instead of return
        else:             #When file reaches EOF
            print("File Copied")
            break

for block in read_bytes(infile):    #Iterate through the file
    outfile.write(block)

outfile.close()
infile.close()
