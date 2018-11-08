import math

def print_formatted(num):
    
    octal = 0
    hexidecimal = ""
    binary = ""
    
    if num > 99 or num < 1:
        print("Please enter a number from 1 to 99.")
        exit()
    
    for x in range(1, num+1):
        if (x % 8) == 0:
            octal+=3
        else:
            octal+=1
        
        #dernary = num
        #binary = str(dernary%2) + binary
        #dernary = dernary//2        

        if x < 10:
            hexidecimal = str(x)
        elif x >= 10 and x <= 15:
            if x == 10:
                hexidecimal = "A"
            elif x == 11:
                hexidecimal = "B"
            elif x == 12:
                hexidecimal = "C"
            elif x == 13:
                hexidecimal = "D"
            elif x == 14:
                hexidecimal = "E"
            elif x == 15:
                hexidecimal = "F"
        elif x >= 16:
            if (x%16) == 10:
                hexidecimal = str(math.floor(x/16)) + "A"
            elif (x%16) == 11:
                hexidecimal = str(math.floor(x/16)) + "B"
            elif (x%16) == 12:
                hexidecimal = str(math.floor(x/16)) + "C"
            elif (x%16) == 13:
                hexidecimal = str(math.floor(x/16)) + "D"
            elif (x%16) == 14:
                hexidecimal = str(math.floor(x/16)) + "E"
            elif (x%16) == 15:
                hexidecimal = str(math.floor(x/16)) + "F"
            else:
                hexidecimal = str(math.floor(x/16)) + str(x%16)

        print(str(x) + " " + str(octal) + " " + hexidecimal + " " + binary) 
        dernary = num

    while dernary>0:
        binary = str(dernary%2) + binary
        dernary = dernary//2
        print(binary)
        
    print(binary)

if __name__ == "__main__":    
    n = int(input())
    print_formatted(n)
