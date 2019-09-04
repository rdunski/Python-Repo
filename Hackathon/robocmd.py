from scapy.all import *
import sys

ip=IP(src='192.168.1.101',dst='192.168.1.111')
packet=UDP(sport=random.randint(1024,49151),dport=3000)
try:
    if sys.argv[1] == 'help':
        print("Usage: ./rc.sh | sudo python robocmd.py [command][packet count]")
        print("")
        print("Commands: 'u' - Forward")
        print("          'd' - Backward")
        print("          'l' - Turn Left")
        print("          'r' - Turn Right")
        print("          'h' - Control Tail Position")
        print("          'o' - Open Pincers")
        print("          'c' - Close Pincers")
        print("          Note: Pincers must be fully open before sending 'c' command")
        print("")
        print("Command default = 'u'")
        print("Packet count default = 1")
        exit(0)
except IndexError:
    pass
try:
    msg = list(sys.argv[1])
except IndexError:
    print("No command given, using default 'u'")
    msg = 'u'
try:
    print(sys.argv[2])
    if len(sys.argv[1]) < 2:
        count = int(sys.argv[2])
    else:
        print("Not a valid command to loop, try 'u', 'd', 'l', or 'r'")
        exit(2)
except ValueError:
    print("Enter a number for second argument")
    exit(1)
except IndexError:
    count = 1
for x in msg:
    command = x
    send(ip/packet/Raw(load=command),count=count)
