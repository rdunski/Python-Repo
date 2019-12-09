import socket
import sys

filearg = sys.argv[1]

infile = open(filearg, "rb")

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('10.5.104.22', 55555)
sock.connect(server_address)

def read_bytes(filename, blocksize=1024):
    while True:
        chunk = bytearray(filename.read(blocksize))
        if chunk:
            yield chunk
        else:
            print("File Sent, closing connection...")
            break

for block in read_bytes(infile):
    sock.send(block)

sock.close()
infile.close()
