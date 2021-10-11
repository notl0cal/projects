#!/usr/bin/python
import sys
import math
def intro():
    c = 1
    while c > 0:
        print ("""
        Welcome to Quick Maths!\n
        1.) Percent Change Calculator.\n
        2.) Dollar Cost Averager.\n
        3.) Entry Maths.\n
        0.) To Exit.\n
        """)
        a = input("Please select an option: ")
        if a == 1:
            pChange()
            continue
        if a == 2:
            dca()
            continue
        if a == 3:
            eMath()
            continue
        if a == 0:
            sys.exit("Exiting...")
        else:
            d = input("Not a valid option. Want to try again? (Y/N)")
            if d != "Y" or "y" or "yes" or "YES":
                sys.exit("Exiting...")
            else:
                continue
def pChange():
    pc1 = float(input("Enter the current price: "))
    pc2 = float(input("Enter the final price: "))
    pc2 = (pc1 - pc2) / pc1
    print("%.0f%%" % (100 * pc2))
    input("Press any key to continue...")
def dca():
    dca1 = [int(x) for x in input("Please enter dollar amounts with spaces inbetween.\n$: ").split()]
    dca1 = (sum(dca1) / len(dca1))
    print("$" + str(dca1))
    input("Press any key to continue...")
def eMath():
    em1 = float(input("Enter your entry point in dollars:\n$: "))
    u1 = " per unit"
    emTake = (em1 * 0.12) + em1
    emStop = em1 - (em1 * 0.06)
    emProfit = emTake - em1
    emLoss = em1 - emStop
    print("Take$: " + str(emTake) + "\n" + "Stop$: " + str(emStop) + "\n" + "Profit$/unit: " + str(emProfit) + "\n" + "Loss$/unit: " + str(emLoss))
    input("Press any key to continue...")
intro()
