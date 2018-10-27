import random
import sys


password = ""

passwords = []

def switch(num):
    global password
    if num == 1:
        password += "a"
    elif num == 2:
        password+="b"
    elif num == 3:
        password+="c"
    elif num == 4:    
        password+="d"
    elif num == 5:
        password+="e"
    elif num == 6:
        password+="f"
    elif num == 7:    
        password+="g"
    elif num == 8:
        password+="h"
    elif num == 9:
        password+="i"
    elif num == 10:    
        password+="j"
    elif num == 11:
        password+="k"
    elif num == 12:
        password+="l"
    elif num == 13:
        password+="m"
    elif num == 14:
        password+="n"
    elif num == 15:    
        password+="o"
    elif num == 16:
        password+="p"
    elif num == 17:
        password+="q"
    elif num == 18:
        password+="r"
    elif num == 19:
        password+="s"
    elif num == 20:
        password+="t"
    elif num == 21:
        password+="u"
    elif num == 22:
        password+="v"
    elif num == 23:
        password+="w"
    elif num == 24:
        password+="x"
    elif num == 25:
        password+="y"
    elif num == 26:
        password+="z"
    elif num == 27:
        password+="1"
    elif num == 28:
        password+="2"
    elif num == 29:
        password+="3"
    elif num == 30:
        password+="4"
    elif num == 31:
        password+="5"
    elif num == 32:
        password+="6"
    elif num == 33:
        password+="7"
    elif num == 34:
        password+="8"
    elif num == 35:
        password+="9"
    elif num == 36:
        password+="0"
    elif num == 37:
        password+="!"
    elif num == 38:
        password+="@"
    elif num == 39:
        password+="#"
    elif num == 40:
        password+="$"
    elif num == 41:
        password+="%"
    elif num == 42:
        password+="^"
    elif num == 43:
        password+="&"
    elif num == 44:
        password+="*"
    elif num == 45:
        password+="("
    elif num == 46:
        password+=")"
    elif num == 47:
        password+="-"
    elif num == 48:
        password+="_"
    elif num == 49:
        password+="="
    elif num == 50:
        password+="+"
    elif num == 51:
        password+="["
    elif num == 52:
        password+="{"
    elif num == 53:
        password+="]"
    elif num == 54:
        password+="}"
    elif num == 55:
        password+=";"
    elif num == 56:
        password+=":"
    elif num == 57:
        password+="<"
    elif num == 58:
        password+=">"
    elif num == 59:
        password+=","
    elif num == 60:
        password+="."
    elif num == 61:
        password+="/"
    elif num == 62:
        password+="?"
               
if __name__ == "__main__":               
    for x in range(1, int(sys.argv[1])+1):
        rand = random.randint(1, 62)
        switch(rand)    

    rand = random.randint(1, 2)
    if rand == 2:
        password = password.capitalize()
        
    print(password)

