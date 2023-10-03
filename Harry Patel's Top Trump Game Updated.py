#Notes#
#this program is based on the card game Top Trumps
#this program will allow you to switch between different decks of Top Trump cards
#this program gives the choice of playing as 1 player (vs an ai) or with 2 players (vs another person)
#Made by: Harry Patel - George Salter Academy - 11R1 (Year 11 Royal 1)


##Program Necessities##



#decks and categories
drinks = {'WATER': [5, 9, 6], 'SPARKLING WATER': [3, 10, 1], 'COCA COLA': [8, 1, 9], 'PEPSI': [9, 2, 8], 'SPRITE': [7, 5, 5], 'LUCOZADE': [6, 7, 7]}
dCategories = ("Taste", "Health", "Popularity")
reindeer = {'RUDOLPH': [1, 1, 1000], 'CUPID': [5, 5, 5], 'DASHER': [9, 2, 9], 'DANCER': [6, 4, 8], 'PRANCER': [7, 3, 7], 'COMET': [8, 6, 2]}
rCategories = ("Speed", "Strength", "Favourite")
names = {'HARRY': [9999, 9999, 9999], 'BARRY': [2, 9, 3], 'SALLY': [9, 3, 2], 'ARRY': [5, 5, 5], 'PALLY': [3, 2, 9], 'LARRY': [0, 0, 0]}
nCategories = ("Intelligence", "Strength", "Speed")
#the card names are upper case to make them stand out, however they can be enterred in any format, so long as the characters match up.

#function imports
import time #for the time.sleep command, which allows pauses so that the program can appear more user friendly
import random #allows for choices to be made without the user (the computer randomly chooses something)

#stages (how the loop of the code is maintained, and also makes it easier to tell which section of the code your looking at)
menu = "true"
nPlayers = "true"
sDeck = "true"
dMenu = "true"
drinksMenu = "true"
reindeerMenu = "true"
nameMenu = "true"
player1 = "true"
player2 = "true"
player22 = "true"



#variables
#__Select = int(1) (What option you are on in a menu)
#__Choice = ""     (What key is while your on a specific option, so it know what screen to go to next)
menuSelect = int(1) 
menuChoice = "" 

playerSelect = int(1)
playerChoice = "" 

deck = drinks #default deck
deckName = "DRINKS" #default deck name
categories = dCategories #default categories
deckSelect = int(1)
deckChoice = ""

list1 =[0,1,2] #these numbers are randomly chosen by the computer to determine the category

drinkSelect = int(1)
drinkChoice = ""

reindeerSelect = int(1)
reindeerChoice = ""

nameSelect = int(1)
nameChoice = ""

userCard = "" #the card that player1 picks
userCard2 = "" #the card the second player or bot picks
#usersCard (Contains the attributes of userCard)
#usersCard2 (Contains the attributes of userCard2)

fix = "false" #allows the two player loop to end



##Program##



#Controls
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n") #\n means line skip, this program uses it to make the screen appear fresh for aesthetics
print("Controls: \nW + Enter     - Up \nS + Enter     - Down \nEnter         - Select\n")
time.sleep(0.5) #time.sleep makes the program pause for a set period of time before moving onto the next line
print(" |Start|\n")
input("\n------------------\nEnter To Continue:\n") #------------------\n is included at the front to make the users inputs seem seperated from the prints to make it feel like a real screen/menu
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

#loading screen
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
print("\n\n\nLoading")
time.sleep(1)
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nLoading.")
time.sleep(1)
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nLoading..")
time.sleep(1)
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nLoading...")
time.sleep(1)
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")


#menu
while menu  == "true":   
    if menuSelect == 1: #Play is selected
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n") 
        print("||PETAL TOP TRUMPS||\n\n |Play|\n|Deck|\n|Help|\n|Exit|\n\n")#Starting Screen
        menuChoice = str(input("------------------\nEnter To Continue:\n"))
        #Cycle the menu
        if menuChoice.lower() == "w":
            menuSelect = 4
        if menuChoice.lower() == "s":
            menuSelect = 2


            
            
        #Player Selection Screen
        if menuChoice.lower() == "":#1 Player is selected
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            while nPlayers == "true":
                if playerSelect == 1:
                    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                    print("||PLAY||\n\n |1 Player|\n|2 Player|\n|Back|\n\n")
                    playerChoice = str(input("------------------\nEnter to Continue:\n"))
                    #Cycle the Player Selection Screen
                    if playerChoice.lower() == "w":
                        playerSelect = 3
                    if playerChoice.lower() == "s":
                        playerSelect = 2

                        

                    #1 Player Mode
                    if playerChoice.lower() == "":
                        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                        
                        #First Player's Card                        
                        while player1 == "true":
                            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                            print("||",deckName,"||\n")
                            print("Categories:")
                            print(categories)
                            print("Cards:")
                            print(deck)
                            userCard = input("\n |Player 1's Card|\n\n\n------------------\nEnter to Continue:\n")

                            #if they inputted a valid card
                            if userCard.upper() in deck:
                                usersCard = deck[userCard.upper()]
                                del deck[userCard.upper()] #remove the card from the deck, to ensure the computer cant use it as well (you can't really duplicate cards in real life)
                                
                                #Just for aesthetics to make it look like the computer is the second player
                                print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                                print("||",deckName,"||\n")
                                print("Categories:")
                                print(categories)
                                print("Cards:")
                                print(deck)
                                
                                #Computer's Card
                                print("\n |Player 2's Card|\n\n\n------------------\nComputer:")
                                userCard2 = random.choice(list(deck.keys()))
                                usersCard2 = deck[userCard2]
                                time.sleep(2)
                                print(userCard2)
                                time.sleep(1)
                                del deck[userCard2] #removes the computers as well
                                
                                #adds both cards back to the end of the deck / dictionary
                                deck[userCard2]= usersCard2 
                                deck[userCard.upper()]= usersCard

                                print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                                num = random.choice(list1) #decide the category to compare

                                #Results Screen
                                print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                                print("\n\n\n||RESULTS||\n")
                                time.sleep(1)
                                print("|| Category:",categories[num],"||\n")
                                time.sleep(1)
                                print("Player1's Card:")
                                print(userCard.upper())
                                time.sleep(1)
                                print(categories[num],":")
                                print(usersCard[num])
                                time.sleep(1)
                                print("\nPlayer2's Card:")
                                print(userCard2)
                                time.sleep(1)
                                print(categories[num],":")
                                print(usersCard2[num])
                                time.sleep(1)
                                print("\n\n")
                                if usersCard[num] > usersCard2[num]:
                                    print("|Player1 Wins!|")
                                else:
                                    print("|Player2 Wins!|")
                                input("\n\n------------------\nEnter to Continue:\n")
                                break
                                
                                
                                

                if playerSelect == 2: #2 player is selected
                    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                    print("||PLAY||\n\n|1 Player|\n |2 Player|\n|Back|\n\n")
                    playerChoice = str(input("------------------\nEnter to Continue:\n"))
                    #Cycle the Player Selection Screen
                    if playerChoice.lower() == "w":
                        playerSelect = 1
                    if playerChoice.lower() == "s":
                        playerSelect = 3


                        

                    #2 Player Mode
                    if playerChoice.lower() == "":
                        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                        player2 == "true"

                        #First Player's Card
                        while player2 == "true":
                            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                            print("||",deckName,"||\n")
                            print("Categories:")
                            print(categories)
                            print("Cards:")
                            print(deck)
                            userCard = input("\n |Player 1's Card|\n\n\n------------------\nEnter to Continue:\n")
                            
                            #if they have a valid card
                            if userCard.upper() in deck:
                                usersCard = deck[userCard.upper()]
                                del deck[userCard.upper()]
                                print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                                
                                #Second Player's Card
                                while player22 == "true":
                                    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                                    print("||",deckName,"||\n")
                                    print("Categories:")
                                    print(categories)
                                    print("Cards:")
                                    print(deck)
                                    userCard2 = input("\n |Player 2's Card|\n\n\n------------------\nEnter to Continue:\n")
                                    #if they have a valid card
                                    if userCard2.upper() in deck:
                                        usersCard2 = deck[userCard2.upper()]
                                        del deck[userCard2.upper()] #delete that card too
                                        deck[userCard2.upper()]= usersCard2 #add both cards back to the end of the deck / dictionary
                                        deck[userCard.upper()]= usersCard

                                        #Results Screen
                                        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                                        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                                        num = random.choice(list1) #decides the category to compare
                                        print("\n\n\n||RESULTS||\n")
                                        time.sleep(1)
                                        print("|| Category:",categories[num],"||\n")
                                        time.sleep(1)
                                        print("Player1's Card:")
                                        print(userCard.upper())
                                        time.sleep(1)
                                        print(categories[num],":")
                                        print(usersCard[num])
                                        time.sleep(1)
                                        print("\nPlayer2's Card:")
                                        print(userCard2.upper())
                                        time.sleep(1)
                                        print(categories[num],":")
                                        print(usersCard2[num])
                                        time.sleep(1)
                                        print("\n\n")
                                        playerSelect = 1
                                        if usersCard[num] > usersCard2[num]:
                                            print("|Player1 Wins!|")
                                        else:
                                            print("|Player2 Wins!|")
                                        input("\n\n------------------\nEnter to Continue:\n")
                                        
                                        #tells the program we have reached the end of 2 player
                                        fix = "true"
                                        break

                                #This all essentially means "if we just finished 2 player, then go back")
                                if fix == "true":
                                    fix = "false"
                                    break

                                        
                if playerSelect == 3: #Back is selected
                    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                    print("||PLAY||\n\n|1 Player|\n|2 Player|\n |Back|\n\n")
                    playerChoice = str(input("------------------\nEnter to Continue:\n"))
                    #Cycle the Player Selection Screen
                    if playerChoice.lower() == "w":
                        playerSelect = 2
                    if playerChoice.lower() == "s":
                        playerSelect = 1
                    #Back
                    if playerChoice.lower() == "":
                        playerSelect = int(1)
                        break

                        
                    
                        
            
    if menuSelect == 2: #Switch Deck is selected
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n") #
        print("||PETAL TOP TRUMPS||\n\n|Play|\n |Deck|\n|Help|\n|Exit|\n\n")#Starting Screen
        menuChoice = str(input("------------------\nEnter To Continue:\n"))
        #Cycle the menu
        if menuChoice.lower() == "w":
            menuSelect = 1
        if menuChoice.lower() == "s":
            menuSelect = 3



            
        #Switch Deck
        if menuChoice.lower() == "":
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            while sDeck == "true": 


                #drinks reindeer names show up
                if deckSelect == 1: #Drinks is selected
                    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                    print("||DECKS||\n\n |Drinks|\n|Reindeers|\n|Names|\n|Back|\n\n")
                    deckChoice = str(input("------------------\nEnter to Continue:\n"))
                    #Cycle the decks
                    if deckChoice.lower() == "w":
                        deckSelect = 4
                    if deckChoice.lower() == "s":
                        deckSelect = 2


                    #Drinks Menu
                    if deckChoice.lower() == "":
                        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                        while drinksMenu == "true":
                            if drinkSelect == 1: #if Select is selected
                                print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                                print("||DRINKS||")
                                if deck == drinks: #tells you if this deck is already selected
                                    print("||SELECTED||")
                                else:
                                    print("")
                                print("\nCategories:\n",dCategories)
                                print("Cards:\n",drinks)
                                print("\n\n |Select|\n|Back|\n\n")
                                drinkChoice = str(input("------------------\nEnter to Continue:\n"))
                                #Cycle through drinks menu
                                if drinkChoice.lower() == "w":
                                    drinkSelect = 2
                                if drinkChoice.lower() == "s":
                                    drinkSelect = 2
                                #Changes the deck to drinks
                                if drinkChoice.lower() == "": 
                                    categories = dCategories
                                    deck = drinks
                                    deckName = "DRINKS"
                            if drinkSelect == 2: #if Back is selected
                                print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                                print("||DRINKS||")
                                if deck == drinks: #tells you if this deck is already selected
                                    print("||SELECTED||")
                                else:
                                    print("")
                                print("\nCategories:\n",dCategories)
                                print("Cards:\n",drinks)
                                print("\n\n|Select|\n |Back|\n\n")
                                drinkChoice = str(input("------------------\nEnter to Continue:\n"))
                                #Cycle through the drinks menu
                                if drinkChoice.lower() == "w":
                                    drinkSelect = 1
                                if drinkChoice.lower() == "s":
                                    drinkSelect = 1
                                #Go Back to Decks menu
                                if drinkChoice.lower() == "":
                                    drinkSelect = int(1)
                                    deckSelect = int(1)
                                    break

                                
                                    
                             
                if deckSelect == 2: #Reindeers is selected
                    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                    print("||DECKS||\n\n|Drinks|\n |Reindeers|\n|Names|\n|Back|\n")
                    deckChoice = str(input("\n------------------\nEnter to Continue:\n"))
                    if deckChoice.lower() == "w":
                        deckSelect = 1
                    if deckChoice.lower() == "s":
                        deckSelect = 3
                        

                    #Reindeer Menu
                    if deckChoice.lower() == "":
                        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                        while reindeerMenu == "true":
                            if reindeerSelect == 1: #Reindeer Select button selected
                                print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                                print("||REINDEER||")
                                if deck == reindeer: #Tells you if reindeer is selected
                                    print("||SELECTED||")
                                else:
                                    print("")
                                print("\nCategories:\n",rCategories)
                                print("Cards:\n",reindeer)
                                print("\n\n |Select|\n|Back|\n\n")
                                reindeerChoice = str(input("------------------\nEnter to Continue:\n"))
                                #Cycle between buttons
                                if reindeerChoice.lower() == "w": 
                                    reindeerSelect = 2
                                if reindeerChoice.lower() == "s":
                                    reindeerSelect = 2

                                #changes to this deck
                                if reindeerChoice.lower() == "": 
                                    categories = rCategories
                                    deck = reindeer
                                    deckName = "REINDEER"
                            if reindeerSelect == 2: #Reindeer Back button selected
                                print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                                print("||REINDEER||")
                                if deck == reindeer: #Tells you if reindeer is seleceted
                                    print("||SELECTED||")
                                else:
                                    print("")
                                print("\nCategories:\n",rCategories)
                                print("Cards:\n",reindeer)
                                print("\n\n|Select|\n |Back|\n\n")
                                reindeerChoice = str(input("------------------\nEnter to Continue:\n"))
                                #Cycle between buttons
                                if reindeerChoice.lower() == "w": 
                                    reindeerSelect = 1
                                if reindeerChoice.lower() == "s":
                                    reindeerSelect = 1
                                #Go back to Deck Select
                                if reindeerChoice.lower() == "":
                                    reindeerSelect = int(1)
                                    deckSelect = int(1)
                                    break

                        


                if deckSelect == 3: #Names is selected
                    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                    print("||DECKS||\n\n|Drinks|\n|Reindeers|\n |Names|\n|Back|\n\n")
                    deckChoice = str(input("------------------\nEnter to Continue:\n"))
                    #Cycle Deck Menu
                    if deckChoice.lower() == "w":
                        deckSelect = 2
                    if deckChoice.lower() == "s":
                        deckSelect = 4


                    #Names Menu
                    if deckChoice.lower() == "":
                        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                        while nameMenu == "true":
                            if nameSelect == 1: #Select is selected
                                print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                                print("||NAMES||")
                                if deck == names: #if names is already selected
                                    print("||SELECTED||")
                                else:
                                    print("")
                                print("\nCategories:\n",nCategories)
                                print("Cards:\n",names)
                                print("\n\n |Select|\n|Back|\n\n")
                                #Cycle the Names Menu
                                nameChoice = str(input("------------------\nEnter to Continue:\n"))
                                if nameChoice.lower() == "w":
                                    nameSelect = 2
                                if nameChoice.lower() == "s":
                                    nameSelect = 2
                                #Change deck to Names
                                if nameChoice.lower() == "":
                                    categories = nCategories
                                    deck = names
                                    deckName = "NAMES"

                            if nameSelect == 2: #Back is seleceted
                                print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                                print("||NAMES||")
                                if deck == names: #if names is already selected
                                    print("||SELECTED||")
                                else:
                                    print("")
                                print("\nCategories:\n",nCategories)
                                print("Cards:\n",names)
                                print("\n\n|Select|\n |Back|\n\n")
                                nameChoice = str(input("------------------\nEnter to Continue:\n"))
                                #Cycle the Names Menu
                                if nameChoice.lower() == "w":
                                    nameSelect = 1
                                if nameChoice.lower() == "s":
                                    nameSelect = 1
                                #Go back to Deck Menu
                                if nameChoice.lower() == "":
                                    nameSelect = int(1)
                                    deckSelect = int(1)
                                    break
                                    
                                
                                




                if deckSelect == 4:
                    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                    print("||DECKS||\n\n|Drinks|\n|Reindeers|\n|Names|\n |Back|\n\n")
                    deckChoice = str(input("------------------\nEnter to Continue:\n"))
                    #Cycle the Deck Menu
                    if deckChoice.lower() == "w":
                        deckSelect = 3
                    if deckChoice.lower() == "s":
                        deckSelect = 1


                    #Back to Main Menu
                    if deckChoice.lower() == "":
                        deckSelect = int(1)
                        menuSelect = 1
                        break
                        
                    
                    
                        
                    
                     
                     
                     
                    

 
    if menuSelect == 3: #Help is selected
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print("||PETAL TOP TRUMPS||\n\n|Play|\n|Deck|\n |Help|\n|Exit|\n\n")#Starting Screen
        menuChoice = str(input("------------------\nEnter To Continue:\n"))
        #Cycle the menu
        if menuChoice.lower() == "w":
            menuSelect = 2
        if menuChoice.lower() == "s":
            menuSelect = 4



            
        #Help Menu (give user information on how the game works)
        if menuChoice.lower() == "":
            menuSelect = 1
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            print("||HELP||\n\n")
            print("Two players choose a card\n")
            time.sleep(1)
            print("Each card has statistics attached to it, each based on different categories\n")
            time.sleep(1)
            print("A random category will be picked\n")
            time.sleep(1)
            print("The card with the highest statistic in that category wins\n")
            time.sleep(0.5)
            print("\n |Back|\n")
            input("\n------------------\nEnter To Continue:\n")
            
            
        

            
    if menuSelect == 4: #Exit is selected
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n") #
        print("||PETAL TOP TRUMPS||\n\n|Play|\n|Deck|\n|Help|\n |Exit|\n\n")#Starting Screen
        menuChoice = str(input("------------------\nEnter To Continue:\n"))
        #Cycle the menu
        if menuChoice.lower() == "w":
            menuSelect = 3
        if menuChoice.lower() == "s":
            menuSelect = 1



            
        #Exit the whole loop
        if menuChoice.lower() == "":
            break



#Ending screen
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
print("Ending")
time.sleep(1)
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nEnding.")
time.sleep(1)
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nEnding..")
time.sleep(1)
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nEnding...")
time.sleep(1)
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
