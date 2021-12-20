#!/usr/bin/env python3
import os
import sys
def clear():
    if "linux" in sys.platform:
        os.system("clear")
    if "win32" in sys.platform:
        os.system("cls")
def exit():
    sys.exit("Exiting...")
y = ["Y", "y", "YES", "yes", "Yes"]
n = ["N", "n", "NO", "no", "No"]
while True:
    clear()
    a = input("Ready?(Y/N)\n: ")
    if a in y:
        clear()
        print("""
        THE RULES:
        RULE 1: Always have an escape plan.
        RULE 2: It's not reality unless it's shared.
        RULE 3: Be aware of your surroundings.
        RULE 4: Assumption is the mother of all fuckups.
        RULE 5: Trust your gut.
        RULE 6: Simple and light equals freedom, agility, mobility.
        RULE 7: The solution is in the problem.
        RULE 8: Never take the elevator.
        RULE 9: Act, don't react.
        """)
        input("Press enter to continue...")
    else:
        clear()
        b = input("Want to try again?(Y/N)\n: ")
        if b in y:
            clear()
            continue
        else:
            clear()
            exit()
        