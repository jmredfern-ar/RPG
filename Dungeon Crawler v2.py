import time

direction_prompt = "Choose a direction (n, s, e, w, q)"

def printText(sentence):
    for char in sentence:
        print(char, end ='')
        time.sleep(.045)
    print()

def inputText(sentence):
    for char in sentence:
        print(char, end = '')
        time.sleep(.045)
    return input(" >> ")

printText("~~~ DUNGEON ESCAPE ~~~")
printText("You awaken to discover your DUNGEON cell door ajar...")

direction = inputText(direction_prompt)

# START OUT IN THE DUNGEON - EAST TO ANTECHAMBER
while direction != "e":
    printText("You can't go that way!")
    direction = inputText(direction_prompt)

print()
printText("Moving east...")
printText("You enter an ANTECHAMBER")
direction = inputText(direction_prompt)


#ANTECHAMBER - SOUTH TO THRONE ROOM
while direction != "s":
        printText("You can't go that way!")
        direction = inputText(direction_prompt)

print()
printText("Moving south...")
printText("You enter the THRONE ROOM...")
direction = inputText(direction_prompt)


#THRONE ROOM - EAST TO LIBRARY *OR* WEST TO THE ARMORY
while direction != "e" and direction != "w":
    printText("You can't go that way!")
    direction = inputText(direction_prompt)

#ARMORY - DEAD END
if direction == "w":
    print()
    printText("Moving west...")
    printText("You find a sword in the ARMORY. Add to inventory..?")
    #put more code here...
    
elif direction == "e":
    print()
    printText("Moving east...")
    printText("You are surrounded by books in the LIBRARY...")
    choice = inputText("Do you (p) pick up a book or (c) light a candle...")

    #BOOK OR CANDLE?
    while choice != "p" and choice != "c":
        printText("Choose p or c >> ")

    if choice == "p":
        printText("This SPELL OF GHOSTLY SPEAKING looks handy...")
    else:
        printText("You've summoned a FIRE SPIRIT. Prepare to fight!")
printText("THE END... FOR NOW...")
