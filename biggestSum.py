import time

array = [8, 2, 4, 13, 28, 18, 82, 16, 32, 80]

# loop that multiplies each number in the array by 2
def multiply():
    arrayNum = 0
    
    for num in array:
        tempNum = array[arrayNum]
        sum = tempNum * 2
        time.sleep(0.5)
        print(tempNum, "*", 2, "=", sum)
        arrayNum += 1

# fix
def findMin():
    arrayIndex = 0
    numAfter = 1
    secondIndex = array[numAfter]
    minNum = array[arrayIndex]
    
    for i in array:
        if minNum < secondIndex:
            print(minNum)
            arrayIndex += 1
            numAfter += 1
            minNum = array[arrayIndex]
        else:
            arrayIndex += 1
            numAfter += 1
            minNum = array[arrayIndex]
    print(minNum)
    
   
 

findMin()

# old version1 ---------------
# arrayNum1 = 0
#    arrayNum2 = 1
#   arrayIndex1 = array[arrayNum2]
#    arrayIndex = array[arrayNum1]
#    minNum = arrayIndex
#    for i in array:
#        if arrayIndex < arrayIndex1:
#            minNum = arrayIndex
#            arrayNum1 += 1
#            arrayNum2 += 1
#        else: 
#            arrayNum1 += 1
#            arrayNum2 += 1
#    print("minimum", "number", "in", "this", "array", "is", minNum)

        
