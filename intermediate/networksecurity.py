from scapy.all import ARP, Ether, srp
import socket

def network_scan(subnet):
    print("Scanning network", subnet)
    arp_req = ARP(pdst=subnet)
    broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
    combined = broadcast/arp_req
    ans, _ = srp(combined, timeout=1, verbose=False)
    print("IP Address\t\tMAC Address")
    print("-----------------------------------------")
    for sent, received in ans:
        print(received.psrc + "\t\t" + received.hwsrc)

def port_scan(target_ip, port_range):
    print(f"Scanning ports on {target_ip}")
    for port in range(1, port_range + 1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target_ip, port))
        if result == 0:
            print(f"Port {port}: Open")
        s.close()

def main():
    print("Network Security Tools")
    choice = input("Choose a function:\n1. Network Scan\n2. Port Scan\nOption: ")
    if choice == '1':
        subnet = input("Enter the subnet to scan (e.g., 192.168.1.0/24): ")
        network_scan(subnet)
    elif choice == '2':
        target_ip = input("Enter the target IP address: ")
        port_range = int(input("Enter the range of ports to scan (e.g., 100 for first 100 ports): "))
        port_scan(target_ip, port_range)
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
