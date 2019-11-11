import socket

infile = open("/home/esquire/Documents/test", "rb")

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 55555)
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
