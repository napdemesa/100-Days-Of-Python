import sys
import math


#solving the equation Q = Sqaure root of [(2 * C * D)/ H]
#C will always be 50, H will always be 30 and D will be variable input
#separated by comma i.g.: 100,150,180

C = 50
H = 30

def qEquation(num):
    Q = math.floor(math.sqrt((2 * C * num)/ H))
    return Q


if __name__ == "__main__":
    userInput = sys.argv[1].partition(",")
    userInput2 = userInput[2].partition(",")
    
    print(qEquation(int(userInput[0])))
    print(qEquation(int(userInput2[0])))
    print(qEquation(int(userInput2[2])))
