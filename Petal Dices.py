##Notes##
#this program is a dice game of who can get the most points
#this program will allow you to login / signup, saving your accounts statistics
#this program gives the choice of playing as 1 player (vs an ai) or with 2 players (vs another person)
#Made by: Harry Patel - George Salter Academy - 11R1 (Year 11 Royal 1)

##Notes To Self##
#As of right now, the only real bug is that whenever you create a new account
#that another account already has a part of, it will think its already been
#made. Example: If account Harry has been made, account Arry cannot be made,
#as it is a if enterusername in username.txt type of thing.

#Plan: Use for i in range(amount of lines in file, and then check if line i
#is == to enterusername. If it is, add 1 to the count. If it isnt, do nothing.
#at the end if the count is 0, it means that the username doesnt already exist,
#therefore they are allowed to create it, else they cannot



##Program Necessities##


#function imports
import time #for the time.sleep command, which allows pauses so that the program can appear more user friendly
import random #allows for choices to be made without the user (the computer randomly chooses something, or rolling a dice)
import os #allows the making of folders / direction searching


#Starter Variables
oScreenSelect = int(1)
oScreenChoice = ""
loginScreenSelect = int(1)
loginScreenChoice = ""
signupScreenSelect = int(1)
signupScreenChoice = ""
startScreenSelect = int(1)
startScreenChoice = ""

player1password = ""
playerpassword = ""
player1Data = 0
enterusername = ""

player1Data = 0
player1score = 0
roll_1 = 0
roll_2 = 0
roll_3 = 0
data = 0

eNums = (2,4,6)
oNums = (1,3,5)

#Directory / Files
cwd = os.getcwd()

directory = os.path.join(cwd, 'Petal Dices');
if not os.path.exists(directory): #Checks if main directory is not there
    os.mkdir(directory) #Makes it if its isnt there
os.chdir(directory) #Files will be made/edited in 'Petal Dices'

if not os.path.exists('username.txt'): #Makes username.txt
    open('username.txt', 'w').close()

if not os.path.exists('password.txt'): #Makes password.txt
    open('password.txt', 'w').close()

if not os.path.exists('win.txt'): #Makes password.txt
    open('win.txt', 'w').close()

if not os.path.exists('loss.txt'): #Makes password.txt
    open('loss.txt', 'w').close()
    

#Functions
    
def signup(): #Creates a new account
    name = open('username.txt','a')#Makes their name
    name.write("\n"+enterusername)
    name.close()
    
    passs = open('password.txt','a')#Makes their password
    passs.write("\n"+enterpassword)
    passs.close()


    win = open('win.txt','a')#Makes their win count
    win.write("\n"+"0")
    win.close()
    
    loss = open('loss.txt','a')#Makes their lose count
    loss.write("\n"+"0")
    loss.close()
    
    input("Account Created.")



def findData(data: int): #Finds the data of the user trying to login in
    with open('username.txt', 'r') as file:
        content = file.readlines()
        index = [x for x in range(len(content)) if enterusername in content[x]]
        data = index[0]
        return data

def checkPassword(password,data,playerpassword):#Checks if the password matches
    with open('password.txt', 'r') as file:
        content = file.readlines()
        passe = content[data]
        password = passe.strip()
        playerpassword = password
        return playerpassword

def checkStats(data):#Checks if the password matches
    with open('loss.txt', 'r') as file:
        content = file.readlines()
        line = content[data]
        losses = line.strip()
    with open('win.txt', 'r') as file:
        content = file.readlines()
        line = content[data]
        wins = line.strip()
        if wins == 0 and losses == 0:
            ratio = "No "
        else:
            try:
                ratio = str(round((float(wins) / (float(wins) + float(losses)) * 100 )))
            except:
                ratio = "No "
        return wins, losses, ratio



def timer():
    #The timer itself
    input("Press Enter to start")
    start_time = time.time()
    input("Press Enter to stop")
    end_time = time.time()
    #Converts the timer into integer seconds
    timeTaken = round(end_time - start_time)
    print("The timer (amount added on) in seconds is " + str(timeTaken))
    return timeTaken

def roll(roll):
    #roll a random number
    roll = random.randint(1,6)
    print("Initial Dice Number : " + str(roll))
    timeTaken = timer()#timer
    #add the timer onto the roll
    for i in range(timeTaken):
        roll = roll + 1
        if roll == 7:
            roll = 1
    input("Final Dice Number : " + str(roll))
    return roll

eNums = (2,4,6)
oNums = (1,3,5)
def pointAffect(playerscore):
    print("Roll 1")
    roll(roll_1)
    if roll_1 in eNums:
        playerscore = playerscore + 10
    elif roll_1 in oNums:
        playerscore = playerscore - 5
        if playerscore < 0:
            playerscore = 0
    print("Roll 2")
    roll(roll_2)
    if roll_2 in eNums:
        playerscore = playerscore + 10
    elif roll_2 in oNums:
        playerscore = playerscore - 5
        if playerscore < 0:
            playerscore = 0
    if roll_1 == roll_2:
        print("Roll 3")
        roll(roll_3)
        playerscore = playerscore + roll_3
        return playerscore

def gameRound():
    pointAffect(player1score)
    pointAffect(player2score)
def rounds():
    for i in range(0,5):
        gameRound()
        
    
        
print("This part is for debugging the dice roll mechanic") 
roll(1)    
    

##CODE##


#Controls
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n") #\n means line skip, this program uses it to make the screen appear fresh for aesthetics
print("Controls: \nW     - Up \nS     - Down \nEnter - Select\n")
time.sleep(0.5) #time.sleep makes the program pause for a set period of time before moving onto the next line
print(" |Start|\n")
input("\nEnter To Continue:\n")
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")



#Login/Signup
while True:
    if oScreenSelect == 1:
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print("||PETAL DICES||\n\n |Login|\n|SignUp|\n|Help|\n|Exit|\n\n")
        oScreenChoice = str(input("Enter To Continue:\n"))
        if oScreenChoice.lower() == "w":
            oScreenSelect = 4
        if oScreenChoice.lower() == "s":
            oScreenSelect = 2

        #Login
        if oScreenChoice.lower() == "":
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            print("||LOGIN||\n\n |Username : |\n|Password : |\n\n")
            enterusername = str(input("Enter Username:\n"))
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            print("||LOGIN||\n\n|Username : "+enterusername+"|\n |Password : |\n\n")
            enterpassword = str(input("Enter Password:\n"))

            
            while True:

                
                if loginScreenSelect == 1:
                    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                    print("||LOGIN||\n\n|Username : "+enterusername+"|\n|Password : "+enterpassword+"|\n\n\n |Login|\n|Back|\n\n")
                    loginScreenChoice = str(input("Enter To Continue:\n"))
                    if loginScreenChoice.lower() == "w":
                        loginScreenSelect = 2
                    if loginScreenChoice.lower() == "s":
                        loginScreenSelect = 2
                        
                    #Confirm
                    if loginScreenChoice.lower() == "":
                        if len(enterusername) != 0:
                            if len(enterpassword) != 0:
                                if not ' ' in enterusername:
                                    if not ' ' in enterpassword:
                                        if enterusername in open('username.txt').read():
                                            
                                            player1Data = findData(player1Data) #find the data of player1
                                            player1password = checkPassword(playerpassword,player1Data,player1password)
                                                

                                            if enterpassword == player1password:
                                                #Start Screen
                                                while True:
                                                    if startScreenSelect == 1:
                                                        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                                                        print("||" + enterusername + "||\n\n |1 Player|\n|2 Player|\n|Stats|\n|Help|\n|Logout|\n\n")
                                                        startScreenChoice = str(input("Enter To Continue:\n"))
                                                        if startScreenChoice.lower() == "w":
                                                            startScreenSelect = 5
                                                        if startScreenChoice.lower() == "s":
                                                            startScreenSelect = 2
                                                        #1 Player
                                                        if startScreenChoice.lower() == "":
                                                            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                                                            player1Data = 0
                                                            rounds()

                                                            
                                                    if startScreenSelect == 2:
                                                        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                                                        print("||" + enterusername + "||\n\n|1 Player|\n |2 Player|\n|Stats|\n|Help|\n|Logout|\n\n")
                                                        startScreenChoice = str(input("Enter To Continue:\n"))
                                                        if startScreenChoice.lower() == "w":
                                                            startScreenSelect = 1
                                                        if startScreenChoice.lower() == "s":
                                                            startScreenSelect = 3
                                                        #2 Player
                                                        if startScreenChoice.lower() == "":
                                                            roll()


                                                    if startScreenSelect == 3:
                                                        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                                                        print("||" + enterusername + "||\n\n|1 Player|\n|2 Player|\n |Stats|\n|Help|\n|Logout|\n\n")
                                                        startScreenChoice = str(input("Enter To Continue:\n"))
                                                        if startScreenChoice.lower() == "w":
                                                            startScreenSelect = 2
                                                        if startScreenChoice.lower() == "s":
                                                            startScreenSelect = 4
                                                        #Statistics
                                                        if startScreenChoice.lower() == "":
                                                            player1Wins, player1Losses, player1Ratio = checkStats(player1Data)

                                                            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                                                            
                                                            print("||Stats||\n\n[Win : " + player1Wins + "]\n[Loss : " + player1Losses + "]\n[WLR : " + player1Ratio + "%]")
                                                            startScreenSelect = 1
                                                            str(input("\nEnter To Continue:\n"))

                                                            
                                                    if startScreenSelect == 4:
                                                        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                                                        print("||" + enterusername + "||\n\n|1 Player|\n|2 Player|\n|Stats|\n |Help|\n|Logout|\n\n")
                                                        startScreenChoice = str(input("Enter To Continue:\n"))
                                                        if startScreenChoice.lower() == "w":
                                                            startScreenSelect = 3
                                                        if startScreenChoice.lower() == "s":
                                                            startScreenSelect = 5
                                                        #Help
                                                        if startScreenChoice.lower() == "":
                                                            print("")


                                                    if startScreenSelect == 5:
                                                        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                                                        print("||" + enterusername + "||\n\n|1 Player|\n|2 Player|\n|Stats|\n|Help|\n |Logout|\n\n")
                                                        startScreenChoice = str(input("Enter To Continue:\n"))
                                                        if startScreenChoice.lower() == "w":
                                                            startScreenSelect = 4
                                                        if startScreenChoice.lower() == "s":
                                                            startScreenSelect = 1
                                                        #Leave
                                                        if startScreenChoice.lower() == "":
                                                            startScreenSelect = 1
                                                            loginScreenSelect = 2
                                                            enterpassword = ""
                                                            break
                                                            
                                                        
                                                
                                                
                                            else:
                                                input("Invalid Password : Incorrect Password\n")
                                                break
                                                
                                        else:
                                            input("Invalid Username : Username Not Found\n")
                                            break
                                    else:
                                        input("Invalid Password : No Spaces Allowed\n")
                                        break
                                else:
                                    input("Invalid Username : No Spaces Allowed\n")
                                    break
                            else:
                                input("Invalid Password : Password required\n")
                                break
                        else:
                            input("Invalid Username : Username required\n")
                            break


        
                if loginScreenSelect == 2:
                    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                    print("||LOGIN||\n\n|Username : "+enterusername+"|\n|Password : "+enterpassword+"|\n\n\n|Login|\n |Back|\n\n")
                    loginScreenChoice = str(input("Enter To Continue:\n"))
                    if loginScreenChoice.lower() == "w":
                        loginScreenSelect = 1
                    if loginScreenChoice.lower() == "s":
                        loginScreenSelect = 1
                        
                    #Back
                    if loginScreenChoice.lower() == "":
                        loginScreenSelect = 1
                        break
                        
                        
                    

                    
                    
    if oScreenSelect == 2:
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print("||PETAL DICES||\n\n|Login|\n |SignUp|\n|Help|\n|Exit|\n\n")
        oScreenChoice = str(input("Enter To Continue:\n"))
        if oScreenChoice.lower() == "w":
            oScreenSelect = 1
        if oScreenChoice.lower() == "s":
            oScreenSelect = 3
        if oScreenChoice.lower() == "":
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            print("||SIGNUP||\n\n |Username : |\n|Password : |\n\n")
            enterusername = str(input("Enter Username:\n"))
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            print("||SIGNUP||\n\n|Username : "+enterusername+"|\n |Password : |\n\n")
            enterpassword = str(input("Enter Password:\n"))

            
            while True:

                
                if signupScreenSelect == 1:
                    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                    print("||SIGNUP||\n\n|Username : "+enterusername+"|\n|Password : "+enterpassword+"|\n\n\n |Confirm|\n|Back|\n\n")
                    signupScreenChoice = str(input("Enter To Continue:\n"))
                    if signupScreenChoice.lower() == "w":
                        signupScreenSelect = 2
                    if signupScreenChoice.lower() == "s":
                        signupScreenSelect = 2

                     #Confirm
                    if signupScreenChoice.lower() == "":
                        #Open username file as a string
                        with open('username.txt', 'r') as username:
                            content = username.read()
                            lines = username.readlines()
                            
                            
                        
                        #Check if they even inputted information, and make sure there are no spaces (else they could just input nothing)
                        if len(enterusername) != 0:
                            if len(enterpassword) != 0:
                                if not ' ' in enterusername:
                                    if not ' ' in enterpassword:
                                        #Check if the username is available
                                        count = 0
                                        with open('username.txt') as file:
                                            for index, line in enumerate(file):
                                                message = line.strip()
                                                if message.lower() == enterusername.lower():
                                                    count = count + 1

                                                    
                                        if  count > 0:
                                            input("Invalid Username: Username Taken")
                                        else:
                                            signup()
                                    else:
                                        input("Invalid Password : No Spaces Allowed")
                                else:
                                    input("Invalid Username : No Spaces Allowed")
                            else:
                                input("Invalid Password : Password Required")
                        else:
                            input("Invalid Username : Username Required")
                        oScreenSelect = 1
                        break
                       
                            




                if signupScreenSelect == 2:
                    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                    print("||SIGNUP||\n\n|Username : "+enterusername+"|\n|Password : "+enterpassword+"|\n\n\n|Confirm|\n |Back|\n\n")
                    signupScreenChoice = str(input("Enter To Continue:\n"))
                    if signupScreenChoice.lower() == "w":
                        signupScreenSelect = 1
                    if signupScreenChoice.lower() == "s":
                        signupScreenSelect = 1
                        
                    #Back
                    if signupScreenChoice.lower() == "":
                        signupScreenSelect = 1
                        oScreenSelect = 1
                        break


    
    if oScreenSelect == 3:
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print("||PETAL DICES||\n\n|Login|\n|SignUp|\n |Help|\n|Exit|\n\n")
        oScreenChoice = str(input("Enter To Continue:\n"))
        if oScreenChoice.lower() == "w":
            oScreenSelect = 2
        if oScreenChoice.lower() == "s":
            oScreenSelect = 4
        if oScreenChoice.lower() == "":
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n") #\n means line skip, this program uses it to make the screen appear fresh for aesthetics
            print("Controls: \nW     - Up \nS     - Down \nEnter - Select\n")
            time.sleep(0.5) #time.sleep makes the program pause for a set period of time before moving onto the next line
            print("Account Summary:\nAn account is needed in order to store your statistics.")
            print("Each account requires a different name.\n")
            time.sleep(0.5)
            print("Game Rules:")
            input("\nEnter To Continue:\n")
            oScreenSelect = 1
            






    if oScreenSelect == 4:
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print("||PETAL DICES||\n\n|Login|\n|SignUp|\n|Help|\n |Exit|\n\n")
        oScreenChoice = str(input("Enter To Continue:\n"))
        if oScreenChoice.lower() == "w":
            oScreenSelect = 3
        if oScreenChoice.lower() == "s":
            oScreenSelect = 1

            
        #End the code
        if oScreenChoice.lower() == "":
            try:
                    quit()
            except:
                    print("")
        
      
        

