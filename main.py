import csv

from data import init
try:
    file = open("database.csv", "r")
except Exception:
    init()

#reads csv file
with open("database.csv", "r", newline="") as myCSV:
   csv_reader = myCSV.readlines()

#appends each row of csv into individual lists within myList
myList = []
index = 0
for i in range(len(csv_reader)):
    if len(csv_reader[index].split(",")) >1:
        myList.append(csv_reader[index].split(","))
    index += 1
    if index > len(csv_reader):
        index -= 1

account = ""
password = ""
valid = True
exists = False
passCheck = True
follower = 0
checker = []
user = []
array = []
subList = []
chosen = 0

#The below function will take in the account name and check if the account already exists
#If account exists in the database, found will == True
#If account does not exist in the database found will == False
#Function returns array with the position of the account if found (0 if not found)
#And True if found/False if not found
def signIn(account, found):
    array = []
    follower = 0
    account = str(input("What is your account name? "))
    for row in myList:
        checker = myList[follower]
        if follower > len(myList):
            follower -= 1
        elif checker[0] == account:
            chosen = follower
            array.append(chosen)
            found = True
            array.append(found)
            follower += 1
        else:
            follower += 1
            found = False
    array.append(0)
    array.append(found)
    return(array)

#The below function runs if found from the previous function == True
#The function will ask for your password
#If the password is the same as the stored password you will be signed in
#Otherwise it will ask you to sign in again
def passwordIn(account, array):
    if array[1] == True:
        chosen = array[0]
        user = myList[chosen]
        password = str(input("Please input your password: "))
        if password == user[1]:
            passCheck = True
            return(passCheck)
            print("\nSigned in")
        else:
            passCheck = False
            return(passCheck)
            print("\nIncorrect")

#The below function takes in an account name
#The code checks if the account already exists
#If the account exists already it will return True and ask for a new name
#If the name does not already exists it will return True and continue the code
def signUpCheck(account, exists):
    exists = False
    follower = 0
    for row in myList:
        checker = myList[follower]
        if follower > len(myList):
            follower -= 1
        if checker[0] == account:
            print("This account already exists")
            exists = True
            follower += 1
        else:
            follower += 1
    return(exists)

#The below function runs if found from the previous function == False
#The function will append your inputs and temp points/level to a sublist
#This sublist will be appended to myList which is returned to the code
def signUpAppend(account, exists):
    if exists == False:       
        subList.append(account)
        subList.append(password)
        subList.append(0)
        subList.append(1)
        subList.append(0)
        subList.append("Filler")
        myList.append(subList)
        print("Account succesfully created")
        return(myList)
    
#Start of program
print("Welcome to 'Incentivise'\n\nYou will gain 1 level for every 8 points gained. \nYou will gain 3 points for every hour worked.")
option = str(input("\nWould you like to sign in ('I') or sign up ('U')? "))

#Asks you to input an option until you have inputted i/I/u/U
if option != "I" and option != "i" and option != "U" and option != "u":
    valid = False
    while valid == False:
        option = str(input("Please enter a valid option ('I' or 'U')? "))
        if option == "I" or option == "i" or option == "U" or option == "u":
            break

if option == "U" or option == "u":
    account = str(input("Please create an account name? "))
    password = str(input("Please set a password? "))
    exists = signUpCheck(account, exists)
    
    if exists == False:
        myList = signUpAppend(account, exists)
        array.append(len(myList)-1)
        array.append(True)
    
elif option == "I" or option == "i":
    array = signIn(account, array)
    option = ""
    passCheck = passwordIn(account, array)

#If the account already exists when you go to sign up, this below code will run
while exists == True:
    option = str(input("Account already exists, please try again (I/U) "))
    
    if option == "i" or option == "I":
        array = signIn(account, array)
        option = ""
        passCheck = passwordIn(account, array)
         
    elif option == "u" or option == "U":
        account = str(input("Please create an account name? "))
        password = str(input("Please set a password? "))
        exists = signUpCheck(account, exists)
        myList = signUpAppend(account, exists)
        array.append(len(myList)-1)
        array.append(True)
        break

#If the account is not found when you go to sign in, this below code will run
while array[1] == False:
    option = str(input("Account does not exist, please try again (I/U) "))
    
    if option == "i" or option == "I":
        array = signIn(account, array)
        option = ""
        passCheck = passwordIn(account, array)
         
    elif option == "u" or option == "U":
        account = str(input("Please create an account name? "))
        password = str(input("Please set a password? "))
        exists = signUpCheck(account, exists)
        myList = signUpAppend(account, exists)
        array.append(len(myList)-1)
        array.append(True)
        break

#If the name is correct but the password is incorrect, the below code will run
while passCheck == False:
    option = str(input("Your password is incorrect, please try again (I/U) "))
    
    if option == "i" or option == "I":
        array = signIn(account, array)
        option = ""
        passCheck = passwordIn(account, array)
         
    elif option == "u" or option == "U":
        account = str(input("Please create an account name? "))
        password = str(input("Please set a password? "))
        exists = signUpCheck(account, exists)
        myList = signUpAppend(account, exists)
        array.append(len(myList)-1)
        array.append(True)
        break
        
number = array[0]
user = myList[number]

user[4] = int(user[4]) + 1
#greets the user
print("\nHello", user[0], "you are currently level", user[3], "and on day number", user[4])
#asks for hour goal
goal = int(input("How many hours do you wish to work today? (0-12) "))

#decides the users bonus based around their hour goal
bonus = 0
check = False

while check == False:
    if goal >= 1 and goal <= 3:
        bonus = 3
        break
    elif goal > 3 and goal <=6:
        bonus = 6
        break
    elif goal > 6 and goal <=9:
        bonus = 9
        break
    elif goal > 9 and goal <=12:
        bonus = 12
        break
    else:
        goal = int(input("Please insert a valid option for hours goal (0-12) "))

print("If you meet your goal you will gain a bonus", bonus, "points.")

#When the user inputs e they will end their day and run the last bit of the code
end = str(input("\nPlease return at the end of your day ('E') "))

#Asks you to input an option until you have inputted e/E
valid = True
if end != "E" and end != "e":
    valid = False
    while valid == False:
        end = str(input("Please enter a valid option ('E') "))
        if end == "E" or end == "e":
            break

#Asks how many hours you have worked
if end == "E" or end == "e":
    hours = int(input("\nHow many hours did you work today? (0-12) "))

#Ensures that the user has inserted a valid option
while check == False:
    if hours >= 0 and hours < 13:
        break
    else:
        hours = int(input("Please insert a valid option for hours worked (0-12) "))

#If you meet your goal you will gain your points for hours worked + goal
#If you do not meet your goal you will only gain your points for hours worked 
total = 0
pointsAwarded = hours * 3
print("\nYou worked", hours, "hours today meaning that you have gained", pointsAwarded, "points.")
if hours >= goal:
    print("You met your goal today meaning that you have gained a bonus", bonus, "points.")
    total = bonus + pointsAwarded
elif hours < goal:
    print("You did not meet your goal today meaning that you will not gain a bonus", bonus, "points.")
    total = pointsAwarded    

#Writes level and points back to the user
firstPoints = int(user[2])
level = int(user[3])
totalPoints = firstPoints + total

points = 1
for i in range(1, total):
    points += 1
    if points == 8:
        level += 1
        points = 0
        
if points == 0:
    points = 8

print("\nOverall you have gained", total, "points bringing you from level", user[3], "to level", level, "\n\nYou need", points, "more point(s) to go for your next level.")

#writes new values to user list
#writes user back to mylist 
user[2] = totalPoints
user[3] = level
userAfter = myList[number]

follower = 0

file = open("database.csv", "w", newline="")
db = csv.writer(file)
for i in range(len(myList)):
    db.writerow(myList[follower])
    follower += 1
    if follower > len(myList):
        follower -= 1
file.close()



#Graph code found beneath
import matplotlib.pyplot as plt

follower = 1
level = []
day = []
name = []
length = int(len(myList))

#The below code makes a list with all names
follower = 1        
for i in range(length - 1):
    sublist = myList[follower]
    name.append(str(sublist[0]))
    follower += 1
    if follower > len(myList):
        follower -= 1
        
#The below code makes a list with all levels
follower = 1 
for i in range(length - 1):
    sublist = myList[follower]
    level.append(int(sublist[3]))
    follower += 1
    if follower > len(myList):
        follower -= 1
        
#The below code makes a list with all days
follower = 1        
for i in range(length - 1):
    sublist = myList[follower]
    day.append(int(sublist[4]))
    follower += 1
    if follower > len(myList):
        follower -= 1

#Plots the barcharts on the subplot
#Shows each user day count and level
plt.suptitle('"Incentivise" Current Users')

plt.subplot(1,2,1)
plt.bar(name, level)

plt.title("Levels")
plt.ylabel("Current level")
plt.xlabel("Names")

plt.subplot(1,2,2)
plt.bar(name, day)

plt.title("Days")
plt.ylabel("Day count")
plt.xlabel("Names")

plt.show()