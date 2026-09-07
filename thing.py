import time
import random

SCRIPT_TITLE = """
  ███████████  ███████████   █████████  █████                               █████████                               █████                        
▒▒███▒▒▒▒▒███▒▒███▒▒▒▒▒▒█  ███▒▒▒▒▒███▒▒███                               ███▒▒▒▒▒███                             ▒▒███                         
 ▒███    ▒███ ▒███   █ ▒  ███     ▒▒▒  ▒███████    ██████   ████████  ██ ███     ▒▒▒  ████████   ██████    ██████  ▒███ █████  ██████  ████████ 
 ▒██████████  ▒███████   ▒███          ▒███▒▒███  ▒▒▒▒▒███ ▒▒███▒▒███▒▒ ▒███         ▒▒███▒▒███ ▒▒▒▒▒███  ███▒▒███ ▒███▒▒███  ███▒▒███▒▒███▒▒███
 ▒███▒▒▒▒▒███ ▒███▒▒▒█   ▒███          ▒███ ▒███   ███████  ▒███ ▒▒▒    ▒███          ▒███ ▒▒▒   ███████ ▒███ ▒▒▒  ▒██████▒  ▒███████  ▒███ ▒▒▒ 
 ▒███    ▒███ ▒███  ▒    ▒▒███     ███ ▒███ ▒███  ███▒▒███  ▒███        ▒▒███     ███ ▒███      ███▒▒███ ▒███  ███ ▒███▒▒███ ▒███▒▒▒   ▒███     
 ███████████  █████       ▒▒█████████  ████ █████▒▒████████ █████     ██ ▒▒█████████  █████    ▒▒████████▒▒██████  ████ █████▒▒██████  █████    
▒▒▒▒▒▒▒▒▒▒▒  ▒▒▒▒▒         ▒▒▒▒▒▒▒▒▒  ▒▒▒▒ ▒▒▒▒▒  ▒▒▒▒▒▒▒▒ ▒▒▒▒▒     ▒▒   ▒▒▒▒▒▒▒▒▒  ▒▒▒▒▒      ▒▒▒▒▒▒▒▒  ▒▒▒▒▒▒  ▒▒▒▒ ▒▒▒▒▒  ▒▒▒▒▒▒  ▒▒▒▒▒    
                                                                                                                                           """                                 
beginline = "["
endLine = "]"
filled = "#"

loadingBar = beginline + filled + endLine

random = random.random() * 0.5


promptAnswer = int(input("(1 = continue & 0 = quit): "))
if promptAnswer == 1:
    print("LOADING...")
    for i in range(20):
        print(loadingBar, end="\r", flush=True)
        filled += "#"
        loadingBar = beginline + filled + endLine
        time.sleep(random)
elif promptAnswer == 0:
    print("QUITTING...")
    time.sleep(1)
    print("ok")
    quit()
else:
    print("error: nor 1 OR 0")
    quit()

print(SCRIPT_TITLE)
print("Brute Force Character Cracker (IMPORTANT: longer your input is, the slower the program will take to solve)")
print("- input any assortment of characters (uppercase letters, lowercase letters, numbers, and symbols) - ")

promptAnswer2 = str(input(":"))
charactersToSolve = promptAnswer2
if promptAnswer2 == charactersToSolve:
    characterCount = len(charactersToSolve)
    print("-" * characterCount)
    trueString_toSolve = list(charactersToSolve)
    print(trueString_toSolve[3])

