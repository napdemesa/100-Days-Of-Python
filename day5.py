import sys

if __name__ == "__main__":
    passwords = input("Please enter possible passwords:")
    parsedPasswords = passwords.split(",")
    
    lowerCase = "abcdefghijklmnopqrstuvwxyz"
    upperCase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    nums = "0123456789"
    specialCharacters = "$#@"
    correctnessCounter = 0
    

    for i in parsedPasswords:
        for w in lowerCase: 
            if i.find(w) > -1:
                correctnessCounter+=1
                break
        for x in upperCase:
            if i.find(x) > -1:
                correctnessCounter+=1
                break
        for y in nums:
            if i.find(y) > -1:
                correctnessCounter+=1
                break
        for z in specialCharacters:
            if i.find(z) > -1:
                correctnessCounter+=1
                break 
        if len(i) >= 6 and len(i) <= 12:
            correctnessCounter+=1
        if correctnessCounter == 5:
            print(i + " is the password(s) that fit the criteria.")
        correctnessCounter = 0    
