import sys

if __name__ == "__main__":
    
    arr = []
    arrSums = []
    num = int(input("Please enter a number:"))
    
    for i in range(1, num + 1):
        if (num % i) == 0:
            arr.append(i)
    
    x = len(arr) - 1

    for j in range(0, int(len(arr)/2)):
        summ = arr[j] + arr[x]
        x-=1
        arrSums.append(summ)
    
    length = len(arrSums) - 1

    print(str(num) + " => " + str(arrSums[length]))

    

