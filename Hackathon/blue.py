from scapy.all import *

bt=BluetoothHCISocket(0)
ans, unans = bt.sr(HCI_Hdr()/HCI_Command_Hdr())

pkt=Raw(load="u")

srbt1('B4:E6:2D:E8:CA:9F',pkt)
