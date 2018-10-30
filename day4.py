import sys


if __name__ == "__main__":
    
    twoDimArr = []
    oneDimArr = []
    num = 0

    for x in range(0, int(sys.argv[1])):
        for y in range(0, int(sys.argv[2])):
            num = x * y
            oneDimArr.append(num)
            if len(oneDimArr) == int(sys.argv[2]):
                continue
        
        twoDimArr.append(oneDimArr)
        oneDimArr = []
    
    print(twoDimArr)
             
