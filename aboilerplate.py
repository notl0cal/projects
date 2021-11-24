#!/usr/bin/env python3
import sys

def func(file):
    result = 0

def main():
    args = sys.argv[1]
    with open(args) as open_file:
        func(open_file)

if __name__ == "__main__":
    main()