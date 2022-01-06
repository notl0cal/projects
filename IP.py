#!/usr/bin/env python3
import matplotlib
import sys
import re

def harvester(file):
    d = {}
    i = file.read()
    count = 0
    ips = re.findall(r'(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})', i)
    if ips:
        for ip in ips:
            count += 1
            if ip in d:
                d[ip] += 1
            else:
                d[ip] = 1
    for key, value in sorted(d.items()):
        perc = ((value / count) * 100)
        print(key + " - " + str(round(perc, 2))+ "%")
    print("Number of IP Addresses: " + str(count))


            
            
        

def main():
    args = sys.argv[1]
    with open(args) as open_file:
        harvester(open_file)

if __name__ == "__main__":
    main()