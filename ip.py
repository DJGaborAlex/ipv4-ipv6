
import ipaddress

def is_ipv6(address):
    try:
        ip = ipaddress.ip_address(address)
        return isinstance(ip, ipaddress.IPv6Address)
    except ValueError:
        return False

# Input alapú ellenőrzés
if __name__ == "__main__":
    while True:
        cim = input("Add meg az IP-címet (kilépéshez üss Entert): ")
        if not cim:  # Üres input esetén kilép
            print("Kilépés...")
            break
        if is_ipv6(cim):
            print(f"{cim}: IPv6")
        else:
            print(f"{cim}: Nem IPv6")