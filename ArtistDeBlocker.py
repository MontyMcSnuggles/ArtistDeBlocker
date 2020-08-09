#Core modules and variables
import subprocess
import time
import os
import webbrowser
import random
def install(name):
    subprocess.call(['pip', 'install', name])
def clear():
    os.system('cls')
loop= ""

#ADD FEATURE: While these 2 modules below are installed, do not install them again.
install("pywin32")
install("requests")
clear()
import requests

#Characters and Settings:
mcharlist= requests.get('https://raw.githubusercontent.com/MontyMcSnuggles/ArtistDeBlocker/master/textfiles/mcharacters.txt').text.splitlines()
fcharlist= requests.get('https://raw.githubusercontent.com/MontyMcSnuggles/ArtistDeBlocker/master/textfiles/fcharacters.txt').text.splitlines()
settinglist= requests.get('https://raw.githubusercontent.com/MontyMcSnuggles/ArtistDeBlocker/master/textfiles/settings.txt').text.splitlines()

#Mildly Lewd Acts:
mFFFtriolist= requests.get('https://raw.githubusercontent.com/MontyMcSnuggles/ArtistDeBlocker/master/textfiles/mild/mFFFtrio.txt').text.splitlines()
mFFMtriolist= requests.get('https://raw.githubusercontent.com/MontyMcSnuggles/ArtistDeBlocker/master/textfiles/mild/mFFMtrio.txt').text.splitlines()
mFMMtriolist= requests.get('https://raw.githubusercontent.com/MontyMcSnuggles/ArtistDeBlocker/master/textfiles/mild/mFMMtrio.txt').text.splitlines()
mMMMtriolist= requests.get('https://raw.githubusercontent.com/MontyMcSnuggles/ArtistDeBlocker/master/textfiles/mild/mMMMtrio.txt').text.splitlines()
mfemalesololist= requests.get('https://raw.githubusercontent.com/MontyMcSnuggles/ArtistDeBlocker/master/textfiles/mild/mfemalesolo.txt').text.splitlines()
mmalesololist= requests.get('https://raw.githubusercontent.com/MontyMcSnuggles/ArtistDeBlocker/master/textfiles/mild/mmalesolo.txt').text.splitlines()
morgylist= requests.get('https://raw.githubusercontent.com/MontyMcSnuggles/ArtistDeBlocker/master/textfiles/mild/morgy.txt').text.splitlines()
mstraightduolist= requests.get('https://raw.githubusercontent.com/MontyMcSnuggles/ArtistDeBlocker/master/textfiles/mild/mstraightduo.txt').text.splitlines()
myaoiduolist= requests.get('https://raw.githubusercontent.com/MontyMcSnuggles/ArtistDeBlocker/master/textfiles/mild/myaoiduo.txt').text.splitlines()
myuriduolist= requests.get('https://raw.githubusercontent.com/MontyMcSnuggles/ArtistDeBlocker/master/textfiles/mild/myuriduo.txt').text.splitlines()

#Very Lewd Acts:
vFFFtriolist= requests.get('https://raw.githubusercontent.com/MontyMcSnuggles/ArtistDeBlocker/master/textfiles/very/vFFFtrio.txt').text.splitlines()
vFFMtriolist= requests.get('https://raw.githubusercontent.com/MontyMcSnuggles/ArtistDeBlocker/master/textfiles/very/vFFMtrio.txt').text.splitlines()
vFMMtriolist= requests.get('https://raw.githubusercontent.com/MontyMcSnuggles/ArtistDeBlocker/master/textfiles/very/vFMMtrio.txt').text.splitlines()
vMMMtriolist= requests.get('https://raw.githubusercontent.com/MontyMcSnuggles/ArtistDeBlocker/master/textfiles/very/vMMMtrio.txt').text.splitlines()
vfemalesololist= requests.get('https://raw.githubusercontent.com/MontyMcSnuggles/ArtistDeBlocker/master/textfiles/very/vfemalesolo.txt').text.splitlines()
vmalesololist= requests.get('https://raw.githubusercontent.com/MontyMcSnuggles/ArtistDeBlocker/master/textfiles/very/vmalesolo.txt').text.splitlines()
vorgylist= requests.get('https://raw.githubusercontent.com/MontyMcSnuggles/ArtistDeBlocker/master/textfiles/very/vorgy.txt').text.splitlines()
vstraightduolist= requests.get('https://raw.githubusercontent.com/MontyMcSnuggles/ArtistDeBlocker/master/textfiles/very/vstraightduo.txt').text.splitlines()
vyaoiduolist= requests.get('https://raw.githubusercontent.com/MontyMcSnuggles/ArtistDeBlocker/master/textfiles/very/vyaoiduo.txt').text.splitlines()
vyuriduolist= requests.get('https://raw.githubusercontent.com/MontyMcSnuggles/ArtistDeBlocker/master/textfiles/very/vyuriduo.txt').text.splitlines()

#Extremely Lewd Acts:
xFFFtriolist= requests.get('https://raw.githubusercontent.com/MontyMcSnuggles/ArtistDeBlocker/master/textfiles/xtreme/xFFFtrio.txt').text.splitlines()
xFFMtriolist= requests.get('https://raw.githubusercontent.com/MontyMcSnuggles/ArtistDeBlocker/master/textfiles/xtreme/xFFMtrio.txt').text.splitlines()
xFMMtriolist= requests.get('https://raw.githubusercontent.com/MontyMcSnuggles/ArtistDeBlocker/master/textfiles/xtreme/xFMMtrio.txt').text.splitlines()
xMMMtriolist= requests.get('https://raw.githubusercontent.com/MontyMcSnuggles/ArtistDeBlocker/master/textfiles/xtreme/xMMMtrio.txt').text.splitlines()
xfemalesololist= requests.get('https://raw.githubusercontent.com/MontyMcSnuggles/ArtistDeBlocker/master/textfiles/xtreme/xfemalesolo.txt').text.splitlines()
xmalesololist= requests.get('https://raw.githubusercontent.com/MontyMcSnuggles/ArtistDeBlocker/master/textfiles/xtreme/xmalesolo.txt').text.splitlines()
xorgylist= requests.get('https://raw.githubusercontent.com/MontyMcSnuggles/ArtistDeBlocker/master/textfiles/xtreme/xorgy.txt').text.splitlines()
xstraightduolist= requests.get('https://raw.githubusercontent.com/MontyMcSnuggles/ArtistDeBlocker/master/textfiles/xtreme/xstraightduo.txt').text.splitlines()
xyaoiduolist= requests.get('https://raw.githubusercontent.com/MontyMcSnuggles/ArtistDeBlocker/master/textfiles/xtreme/xyaoiduo.txt').text.splitlines()
xyuriduolist= requests.get('https://raw.githubusercontent.com/MontyMcSnuggles/ArtistDeBlocker/master/textfiles/xtreme/xyuriduo.txt').text.splitlines()

#Loop condition
while loop != "" or loop != "r":
    if loop == "":
        #Parameter query
        while True:
            numberofcharsm= int(input("Choose a number of male characters (0, 1, 3, etc.):\n"))
            if numberofcharsm > len(mcharlist):
                print("You cannot choose a number greater than the amount of male characters available.")
                continue
            else:
                break
        while True:
            numberofcharsf= int(input("Choose a number of female characters (0, 1, 3, etc.):\n"))
            if numberofcharsf > len(fcharlist):
                print("You cannot choose a number greater than the amount of female characters available.")
                continue
            else:
                break
        while True:
            lewdlevel= int(input("Choose how lewd the suggestion is.\nMildly Lewd = 1\nVery Lewd = 2\nExtremely Lewd = 3\n"))
            if lewdlevel <1:
                print("Gotta be at least somewhat lewd...\n")
                continue
            elif lewdlevel >3:
                print("Haha, can't get any lewder than that, nice try though.\n")
            else:
                break
        
        #Create 'retry' loop state
        loop= "r"
        continue
    elif loop == "r":
        #Create destructable lists and shuffle them
        fcharacters= fcharlist[:] 
        mcharacters= mcharlist[:]
        random.shuffle(fcharacters)
        random.shuffle(mcharacters)

        #Display characters
        for i in range(numberofcharsf):
            print("Female character #" + str(i+1) + ":", fcharacters.pop())
        for i in range(numberofcharsm):
            print("Male character #" + str(i+1) + ":", mcharacters.pop())
        print("\n")

        #Mildly lewd conditions
        if lewdlevel == 1:
            if numberofcharsf + numberofcharsm > 3:
                print("Lewd act:", random.choice(morgylist))
            elif numberofcharsf == 3:
                print("Lewd act:", random.choice(mFFFtriolist))
            elif numberofcharsf == 2 and numberofcharsm == 1:
                print("Lewd act:", random.choice(mFFMtriolist))
            elif numberofcharsf == 1 and numberofcharsm == 2:
                print("Lewd act:", random.choice(mFMMtriolist))
            elif numberofcharsm == 3:
                print("Lewd act:", random.choice(mMMMtriolist))
            elif numberofcharsf == 1 and numberofcharsm == 0:
                print("Lewd act:", random.choice(mfemalesololist))
            elif numberofcharsf == 0 and numberofcharsm == 1:
                print("Lewd act:", random.choice(mmalesololist))
            elif numberofcharsf == 1 and numberofcharsm == 1:
                print("Lewd act:", random.choice(mstraightduolist))
            elif numberofcharsf == 0 and numberofcharsm == 2:
                print("Lewd act:", random.choice(myaoiduolist))
            elif numberofcharsf == 2 and numberofcharsm == 0:
                print("Lewd act:", random.choice(myuriduolist))

        #Very lewd conditions
        elif lewdlevel == 2:
            if numberofcharsf + numberofcharsm > 3:
                print("Lewd act:", random.choice(vorgylist))
            elif numberofcharsf == 3:
                print("Lewd act:", random.choice(vFFFtriolist))
            elif numberofcharsf == 2 and numberofcharsm == 1:
                print("Lewd act:", random.choice(vFFMtriolist))
            elif numberofcharsf == 1 and numberofcharsm == 2:
                print("Lewd act:", random.choice(vFMMtriolist))
            elif numberofcharsm == 3:
                print("Lewd act:", random.choice(vMMMtriolist))
            elif numberofcharsf == 1 and numberofcharsm == 0:
                print("Lewd act:", random.choice(vfemalesololist))
            elif numberofcharsf == 0 and numberofcharsm == 1:
                print("Lewd act:", random.choice(vmalesololist))
            elif numberofcharsf == 1 and numberofcharsm == 1:
                print("Lewd act:", random.choice(vstraightduolist))
            elif numberofcharsf == 0 and numberofcharsm == 2:
                print("Lewd act:", random.choice(vyaoiduolist))
            elif numberofcharsf == 2 and numberofcharsm == 0:
                print("Lewd act:", random.choice(vyuriduolist))

        #Extremely lewd conditions
        elif lewdlevel == 3:
            if numberofcharsf + numberofcharsm > 3:
                print("Lewd act:", random.choice(xorgylist))
            elif numberofcharsf == 3:
                print("Lewd act:", random.choice(xFFFtriolist))
            elif numberofcharsf == 2 and numberofcharsm == 1:
                print("Lewd act:", random.choice(xFFMtriolist))
            elif numberofcharsf == 1 and numberofcharsm == 2:
                print("Lewd act:", random.choice(xFMMtriolist))
            elif numberofcharsm == 3:
                print("Lewd act:", random.choice(xMMMtriolist))
            elif numberofcharsf == 1 and numberofcharsm == 0:
                print("Lewd act:", random.choice(xfemalesololist))
            elif numberofcharsf == 0 and numberofcharsm == 1:
                print("Lewd act:", random.choice(xmalesololist))
            elif numberofcharsf == 1 and numberofcharsm == 1:
                print("Lewd act:", random.choice(xstraightduolist))
            elif numberofcharsf == 0 and numberofcharsm == 2:
                print("Lewd act:", random.choice(xyaoiduolist))
            elif numberofcharsf == 2 and numberofcharsm == 0:
                print("Lewd act:", random.choice(xyuriduolist))
        loop= input("\nHit ENTER to create new parameters, enter 'r' to create a new result with the existing parameters. Enter any other value to exit the program.\n ")
        continue
    else:
        break
