import sys

if __name__ == "__main__":

    arr = []
    nums = ""
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
    
    for k in range(0, len(newArr)):
        for p in range(k):
            if p == (len(newArr) - 1):
                if int(newArr[len(newArr) - 1][0]) < int(newArr[p][0]):
                    temp = newArr[p]
                    newArr[p] = newArr[len(lenArr) - 1]
                    newArr[len(newArr) - 1] = temp
                break    

            if int(newArr[p][0]) > int(newArr[p + 1][0]):
                temp = newArr[p]
                newArr[p] = newArr[p + 1]
                newArr[p + 1] = temp
    
            if int(newArr[p][0]) == int(newArr[p + 1][0]):
                if int(newArr[p][1]) > int(newArr[p + 1][1]):
                    temp = newArr[p]
                    newArr[p] = newArr[p + 1]
                    newArr[p + 1] = temp

    print(newArr)
    print(maxTime + " maxTime")
    print(minTime + " minTime")

    if 5 > 5:
        print("true")
    else:
        print("false")
