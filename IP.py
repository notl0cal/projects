#!/usr/bin/env python3
import sys
import re

def harvester(file):
    for i in file.readlines():
        ip = re.findall("\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b")

def main():
    args = sys.argv[1]
    with open(args) as open_file:
        harvester(open_file)

if __name__ == "__main__":
    main()