#!/usr/bin/python
import sys
import os
import math
def intro():
    c = 1
    while c > 0:
        print ("""
        Welcome to the Hub!\n
        1.) Percent Change Calculator.\n
        2.) Dollar Cost Averager.\n
        3.) Entry Maths.\n
        0.) To Exit.\n
        """)
        a = int(input("Please select an option: "))
        if a == 1:
            pChange()
        if a == 2:
            dca()
        if a == 3:
            eMath()
        if a == 0:
            sys.exit("Exiting...")
        break
def pChange():
    pc1 = float(input("Enter the current price: "))
    pc2 = float(input("Enter the final price: "))
    pc2 = (pc1 - pc2) / pc1
    print("%.0f%%" % (100 * pc2))
    input("Press any key to continue...")
def dca():
    dca1 = [int(x) for x in input("Please enter dollar amounts with spaces inbetween.\n$: ").split()]
    dca1 = (str(sum(dca1) / len(dca1)))
    print("$" + dca1)
    input("Press any key to continue...")
def eMath():
    em1 = str(input("Enter your entry point in dollars:\n$: "))
    em2 = em1 * 0.12
    em3 = em1 * 0.6
    em4 = em1 + em2
    em5 = em1 + em3
    print(em4)
    print(em5)
intro()
