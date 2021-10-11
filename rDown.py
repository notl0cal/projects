#!/usr/bin/python
import os
# var
def bal():
    print (c1 , "Current Position Size (USD): $" , (v1 * p1))
    print (c1 , "Future Position Size (USD): $" , (v1 * p2))
def pChange():
    v1 = (p2 - p1) / p2
    print(c1 , "Percent Change: %.0f%%" % (100 * v1))
def profit():
    d1 = (v1 * p2) - (v1 * p1)
    print (c1 , "Profit: $" , d1)
# input
c1 = str(input("Ticker?: "))
v1 = float(input("Volume?: "))
p1 = float(input("Purchase Price?: "))
p2 = float(input("Sell Price?: "))
# return
bal()
pChange()
profit()
# nameSave
