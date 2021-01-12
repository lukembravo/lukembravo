# One of my first interactive scripts- a spin on the schoolbus classic IYKYK
# For now, user input has to be just a noun or plural noun- the code will still run fine, but the grammar in the output is a little weird

import re
import time
import sys
def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.01)
doublecheck=0
listofitems = []
items=0
vowels = ["a","e","i","o","u","A","E","I","O","U"]
n = 1

delay_print("What's good, brave explorer?")
print("\n")
delay_print("In preparation for for our journey to the moon, you can pack three personal items.")
print("\n")

while items <= 2:
    doublecheck=0
    if items==0:
        delay_print("What would you like to add to your list?\n")
    elif items==1:
        delay_print("What else do you want to bring?\n")    
    elif items==2:
        delay_print("One last personal item?\n")
    else:
        break
        
    rawinput = input("")
    chars = re.findall("[\w\s]", rawinput)
    #chars = re.sub("my", "", chars) # How could you account for input like "My shoes" such that the output won't be "Sorry, you can't bring a My shoes"? Regex .sub wasn't able to drop the "My"
    charsplusone = chars.append("")

    for x in range(len(chars)-1):
        if (chars[x])==(chars[x+1]):
            doublecheck +=1
        else:
            doublecheck +=0
        
    if doublecheck == 0:
        if rawinput[-1]=="s":
            print("Sorry, fam. You can't bring", rawinput.lower(), "to the moon.")
            print("\n")
        elif rawinput[0] in vowels:
            print("Sorry, fam. You can't bring an", rawinput.lower(), "to the moon.")
            print("\n")
        else:
            print("Sorry, fam. You can't bring a", rawinput.lower(), "to the moon.")
            print("\n")
    else:
        if rawinput[-1]=="s" or rawinput[-1]=="S":
            print("Aight bet. You can bring", rawinput.lower(), "to the moon.")
            print("\n")
        elif rawinput[0] in vowels:
            print("Aight bet. You can bring an", rawinput.lower(), "to the moon.")
            print("\n")
        else:
            print("Aight bet. You can bring a", rawinput.lower(), "to the moon.")
            print("\n")
        listofitems.append(rawinput.capitalize())
        items += 1
        
print("That's three! We'll load up your items right away! You're bringing")
for item in listofitems:
    print(n,".",item)
    n += 1
    


# In[ ]:




