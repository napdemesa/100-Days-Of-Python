import string

def solve(s):
    strName = s.split(" ")
    strNameOut = ""
    for i in strName:
        strNameOut = strNameOut + i.capitalize() + " "
    
    print(strNameOut)


def question(s):
    count = 0
    ten = 0
    initiate = 0
    result = ""
    for j in range(0, len(s)):
        if s[j].isdigit():
            initiate+=1
            ten = ten + int(s[j])
            print(ten)
    
      
        if initiate > 0 and initiate < 3:
            if s[j] == "?":
                if ten == 10:
                    if count == 3:
                        result = "true"
                        count = 0
                        initiate = 0
                        ten = 0
                    else:
                        result = "false"
                else:
                    result = "false"
                count+=1
            print(count)

        if j == (len(s) - 1) and ten != 10 and count != 3:
            result = "false"

    print(result)

if __name__ == "__main__":   
    #s = input()
    #solve(s)

    s = input()
    question(s)
