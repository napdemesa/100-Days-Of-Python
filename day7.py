import sys

if __name__ == "__main__":

    arr = []
    nums = ""
    
    print("Type end when you are done inputting times.")

    while nums != "end":
        nums = input("Enter times entered then left: ")
        if nums == "end":
            break
        arr.append(nums)
    
    newArr = []
    totalTime = 0
    maxTime = 0
    minTime = 0

    for i in arr:
        someTime = i.split(" ")
        newArr.append(someTime)
        
    for j in newArr:
        if minTime == 0 and maxTime == 0:
            minTime = j[0]
            maxTime = j[1]
            continue
        if j[0] < minTime:
            minTime = j[0]
        if j[1] > maxTime:
            maxTime = j[1]
        totalTime = int(maxTime) - int(minTime)
    

    print(newArr)
    
    for index in range(1, len(newArr)):

        currentValueNum = int(newArr[index][0])
        currentValue = newArr[index]
        position = index

        while position > 0 and int(newArr[position - 1][0]) > currentValueNum:
            newArr[position] = newArr[position - 1]
            position-=1

        newArr[position] = currentValue    
    
    for q in range(0, len(newArr) - 1):
        if (int(newArr[q + 1][0]) - int(newArr[q][1])) > 0:
            totalTime = totalTime - (int(newArr[q + 1][0] - int(newArr[q][1])))
        
    print("The total time the lights have been on is " + str(totalTime) + " hours.")    

    
