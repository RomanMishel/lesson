from scapy.all import *

for adr in range(254):
    ip = f'192.168.56.{adr}'
    arp_out = Ether(dst='ff:ff:ff:ff:ff:ff')/ARP(pdst=ip, hwdst='ff:ff:ff:ff:ff:ff')
    arp_in = srp1(arp_out, timeout=1, verbose=0)
    if arp_in:
        print(f'IP: {arp_in.psrc}, MAC: {arp_in.hwsrc}' )
