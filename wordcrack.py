from words import *
import sys
import time

level_Passed = 0
level = 1


def decor(func):
    def wrap():
        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
        print("-------- WORD CRACK--------")
        print(f"You Passed {level_Passed} level(s)")
        print(f"LEVEL {level}")
        print("")
        func()
    return wrap


@decor
def first_level():
    global level
    global level_Passed
    level_Passed = 0
    level = 1
    score = 0
    start = input("Click ENTER to start")
    if start == "":
        i = 0
        while i < len(l1uncracked):
            print(f"Word To Crack: {l1uncracked[i]}")
            crack = input("CRACK: ")
            if crack.upper() == l1cracked[i]:
                print("Correct!")
                score += 1
                print(f"Score: {score}/{len(l1uncracked)}")
                print("")
                i += 1
            else:
                print("")
                print("Wrong! You Lose")
                print(f"You scored: {score}/{len(l1uncracked)}")
                sys.exit()
        else:
            print(f"CONGRATULATIONS! You Passed Level {level}")
            level += 1
            level_Passed += 1
    else:
        print("Learn To Follow Instructions!!!")
        sys.exit()


@decor
def second_level():
    global level
    global level_Passed
    level_Passed = 1
    level = 2
    score = 0
    start = input("Click ENTER to start")
    if start == "":
        i = 0
        while i < len(l2uncracked):
            print(f"Word To Crack: {l2uncracked[i]}")
            crack = input("CRACK: ")
            if crack.upper() == l2cracked[i]:
                print("Correct!")
                score += 1
                print(f"Score: {score}/{len(l2uncracked)}")
                print("")
                i += 1
            else:
                print("")
                print("<<<<<<<Last chance>>>>>>>")
                print(f"Word To Crack: {l2uncracked[i]}")
                crack = input("CRACK: ")
                if crack.upper() == l2cracked[i]:
                    print("Correct!")
                    score += 1
                    print(f"Score: {score}/{len(l2uncracked)}")
                    print("")
                    i += 1
                else:
                    print("")
                    print("Wrong! You Lose")
                    print(f"You scored: {score}/{len(l2uncracked)}")
                    sys.exit()
        else:
            print(f"CONGRATULATIONS! You Passed Level {level}")
            level += 1
            level_Passed += 1
    else:
        print("Learn To Follow Instructions!!!")
        sys.exit()


@decor
def third_level():
    global level
    global level_Passed
    level_Passed = 2
    level = 3
    score = 0
    start = input("Click ENTER to start")
    if start == "":
        i = 0
        while i < len(l3uncracked):
            print(f"Word To Crack: {l3uncracked[i]}")
            crack = input("CRACK: ")
            if crack.upper() == l3cracked[i]:
                print("Correct!")
                score += 1
                print(f"Score: {score}/{len(l3uncracked)}")
                print("")
                i += 1
            else:
                print("")
                print("<<<<<<< 1/2 CHANCES >>>>>>>")
                print(f"Word To Crack: {l3uncracked[i]}")
                crack = input("CRACK: ")
                if crack.upper() == l3cracked[i]:
                    print("Correct!")
                    score += 1
                    print(f"Score: {score}/{len(l3uncracked)}")
                    print("")
                    i += 1
                else:
                    print("")
                    print("<<<<<<< LAST CHANCE >>>>>>>")
                    print(f"Word To Crack: {l3uncracked[i]}")
                    crack = input("CRACK: ")
                    if crack.upper() == l3cracked[i]:
                        print("Correct!")
                        score += 1
                        print(f"Score: {score}/{len(l3uncracked)}")
                        print("")
                        i += 1
                    else:
                        print("")
                        print("Wrong! You Lose")
                        print(f"You scored: {score}/{len(l3uncracked)}")
                        sys.exit()
        else:
            print(f"CONGRATULATIONS! You Passed Level {level}")
            print("CONGRATULATIONS! You succeeded in finishing this game")
            level += 1
            level_Passed += 1
    else:
        print("Learn To Follow Instructions!!!")
        sys.exit()


first_level()

second_level()

third_level()
