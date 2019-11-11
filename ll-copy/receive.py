import socket

outfile = open("/home/esquire/Documents/copyTest", "wb")

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 55555)
sock.bind(server_address)
sock.listen(1)

connection, client_address = sock.accept()

print("Waiting for file...")
def receive_bytes(blocksize=1024):
    while True:
        block = bytearray(connection.recv(blocksize))   #read over socket
        if block:   #if block isn't empty
            outfile.write(block)
        else:
            print("File Received, closing connection...")
            break

receive_bytes()

connection.close()
outfile.close()
