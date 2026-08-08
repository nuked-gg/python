import random
import time

print("[1 = NumberGuessingGame | 2 = RandomSentences]")
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
        delPrank1 = "(..Templates/KDSur://99Iioo//ISO.64x_86x//Directory../)"
        delPrank2 = "(../Repositories/Bin/Trash/ [ALL])"
        delPrank3 = "(Home//Bin://Directory//[ALL]USERS//ll0kkiopp-oKa233xxIaodd14$ookIaodd14$ookaaaaxxIaodd14$ookaa)"
        delPrank4 = "(User://Home://Profile://xxIaodd14Iaodd14$ookaIaodd14$ookaa774a$ookaa)"
        removeText = "[Remove] {FROM BIN://TRASH} --NO_PRESERVE_ROOT"
        for 1, 20 
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
    
else:
    print("invalid choice, please try again.")