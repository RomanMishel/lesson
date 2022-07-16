import nmap

nmScan = nmap.PortScanner()

#nmScan.scan('scanme.nmap.org', '21-443')

nmScan.scan(hosts='scanme.nmap.org', arguments='-n -sP -PE -PA21,23,80,3389')

#nmScan.command_line()

print(nmScan.scan())
