# Készítette Szabó Gábor Alex, Szilágyi Bálint

#IPv4
ipv4 = []
ipv41 = -1
while not(0<=ipv41<=255):
    ipv41 = int(input("Kérem adja meg az IPv4 első részét(pl. 192): "))
if 0<=ipv41<=255:
    ipv4.append(ipv41)
else:
    ipv41 = int(input("Kérem adja meg az IPv4 első részét(pl. 192): "))

ipv42 = -1
while not(0<=ipv42<=255):
    ipv42 = int(input("Kérem adja meg az IPv4 második részét(pl. 192): "))
if 0<=ipv42<=255:
    ipv4.append(ipv42)
else:
    ipv42 = int(input("Kérem adja meg az IPv4 második részét(pl. 192): "))

ipv43 = -1
while not(0<=ipv43<=255):
    ipv43 = int(input("Kérem adja meg az IPv4 harmadik részét(pl. 192): "))
if 0<=ipv43<=255:
    ipv4.append(ipv43)
else:
    ipv43 = int(input("Kérem adja meg az IPv4 harmadik részét(pl. 192): "))

ipv44 = -1
while not(0<=ipv44<=255):
    ipv44 = int(input("Kérem adja meg az IPv4 negyedik részét(pl. 192): "))
if 0<=ipv44<=255:
    ipv4.append(ipv44)
else:
    ipv44 = int(input("Kérem adja meg az IPv4 negyedik részét(pl. 192): "))



print(".".join(map(str, ipv4)))
    