import random
import time

print("[1 = RandomSentences | 2 = NumberGuessingGame]")
promptAnswer = int(input("enter your choice (1 or 2): "))

count1 = 0
count2 = 0

if promptAnswer == 1:
    for i in range(3):
        count1 = count1 + 1
        if count1 == 1:
            print("[#..]")
            time.sleep(1)
        elif count1 == 2:
            print("[##.]")
            time.sleep(1)
        elif count1 == 3:
            print("[###]")
            time.sleep(1)
    time.sleep(1)
    print("-- number guessing game --")
    print("[NOTE: if you guess the wrong number, your files and directories will be deleted]")
    time.sleep(0.5)
    print("guess a random number from 1-10")
    rightNumber = random.randint(1, 10)
    guess = int(input("enter your guess: "))
    if guess == rightNumber:
        print("you guessed the right number!")
    elif promptAnswer > 10 or promptAnswer < 1:
        print("invalid choice, please try again.")
    else:
        print("wrong number, the right number was " + str(rightNumber))
        time.sleep(0.7)
        print("[WARNING: your files and directories will be deleted!]")
        print("deleting files and directories in...")
        time.sleep(0.6)
        print("3...")
        time.sleep(0.6)
        print("2..")
        time.sleep(0.6)
        print("1.")
        time.sleep(0.6)
        print("just kidding!!")
elif promptAnswer == 2:
    for i in range(3):
        count2 = count2 + 1
        if count2 == 1:
            print("[#..]")
            time.sleep(1)
        elif count2 == 2:
            print("[##.]")
            time.sleep(1)
        elif count2 == 3:
            print("[###]")
            time.sleep(1)
    print("-- random sentence generator --")
    time.sleep(0.5)
    print("this option is still in development, please check back later!")
else:
    print("invalid choice, please try again.")