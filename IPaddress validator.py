import ipaddress

ip = input("Enter an IP address: ").strip()

try:
    address = ipaddress.ip_address(ip)
    

    print("Valid IP address!")
    print("IP Version:", address.version)

    if address.version == 4:
        print("Type: IPv4")
    else:
        print("Type: IPv6")

except ValueError:
    print("Invalid IP address!")
    print("Please enter a correctly formatted IPv4 or IPv6 address.")
