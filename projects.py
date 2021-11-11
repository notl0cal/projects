def projects():
    c = 1
    while c > 0:
        print ("""
        Welcome to Projects!\n
        1.) Num Divisible By 2.\n
        2.) Palindrome Checker.\n
        3.) Char in Word.\n
        4.) Invert Case.\n
        5.) Text Altenator.\n
        6.) Vowels In Word.\n
        
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
        if a == "9":
            clear()
            projects()
        if a == "0":
            clear()
            exit()
        else:
            clear()
            d = input("Not a valid option. Want to try again? (Y/N)")
            if d in y:
                continue
            else:
                exit()