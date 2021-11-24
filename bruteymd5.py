import sys
import hashlib
def main():
    number = 000
    hash_text = "9ab0d88431732957a618d4a469a0d4c3"
    clear_text = "FS{cabbage-wait_that's_not_right_" + str(number) + "}"
    while number <= 999:
        number += 1
        clear_text = "FS{cabbage-wait_that's_not_right_" + str(number) + "}"
        if hash_text == hashlib.md5(clear_text.encode()).hexdigest():
            print(clear_text)
            break
        else:
            continue
main()