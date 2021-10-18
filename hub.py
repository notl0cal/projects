#!/usr/bin/python
import sys
import os
import math
def clear():
    os.system("cls")
def exit():
    sys.exit("Exiting...")
def intro():
    y = ["Y", "y", "YES", "yes"]
    n = ["N", "n", "NO", "no"]
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
        if a == "1":
            clear()
            pChange()
            continue
        if a == "2":
            clear()
            dca()
            continue
        if a == "3":
            clear()
            eMath()
            continue
        if a == "0":
            clear()
            exit()
        else:
            clear()
            d = input("Not a valid option. Want to try again? (Y/N)")
            if d in y:
                continue
            if d in n:
                exit()
            else:
                exit()
def pChange():
    pc1 = float(input("Enter the current price: "))
    pc2 = float(input("Enter the final price: "))
    pc2 = (pc1 - pc2) / pc1
    result = "%.0f%%" % (100 * pc2)
    print(result)
    input("Press any key to continue...")
def dca():
    dca1 = [int(x) for x in input("Please enter dollar amounts with spaces inbetween.\n$: ").split()]
    dca2 = (sum(dca1) / len(dca1))
    dca1.sort()
    values = "Values: $" + str(dca1)
    result = "Average: $" + str(dca2) + "\n"
    clear()
    print(values)
    print(result)
    input("Press any key to continue...")
def eMath():
    em1 = float(input("Enter your entry point in dollars:\n$: "))
    eVol = float(input("Please enter number of units purchased:\nU:"))
    emTake = (em1 * 0.12) + em1
    emStop = em1 - (em1 * 0.06)
    ePos = em1 * eVol
    emProfit = (emTake - em1) * eVol
    emLoss = (em1 - emStop) * eVol
    eFut = emProfit + ePos
    result = "Entry: $" + str(em1) + "\n" + "Position: $" + str(ePos) + "\n" + "Future Position: $" + str(eFut) + "\n\n" + "Take: $" + str(emTake) + "\n" + "Stop: $" + str(emStop) + "\n\n" + "Profit: $" + str(emProfit) + "\n" + "Loss: $" + str(emLoss) + "\n"
    clear()
    print(result)
    input("Press any key to continue...")
intro()