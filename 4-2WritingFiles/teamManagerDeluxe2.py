print("Welcome to Team Manager Deluxe!")
# make a class for Player
class Player(object):
	# objects for class
	def __init__(self, name, age, goals, jerseyNumber, position):
                self.name = name
                self.age = age
                self.goals = goals
                self.jerseyNumber = jerseyNumber
                self.position = position
 	# function for objects in class.
        def printStats(self):
		print("Name: " + self.name)
                print("Age: " + str(self.age))
                print("Goals: " + str(self.goals))
                print("Jersey Number: " + str(self.jerseyNumber))
                print("Position: " + self.position)
# def function to save players info in a file.
def saveTeam(myPlayer, filename):
	# open the file
    	file_name = open(filename, "a")
    	# write inside the file per object.
	for p in myPlayer:
		file_name.write(p.name + " " + str(p.age) + " " + str(p.goals) + " " + str(p.jerseyNumber) + " " + p.position + "\n")
    	# close the file
    	file_name.close()
   
# def function for a team in a file already saved.
def loadTeam(filename):
	# make empty list
	mylist = []
	# open the file to be able to read it.
        file_name = open(filename, "r")
        # read line per line
        myline = file_name.readline()
        # while loop to split objects when read line per line.
	while myline != "":
		splits = myline.split()
		# We append the objects we have split.
		mylist.append(Player(splits[0], splits[1], splits[2], splits[3], splits[4]))
		myline = file_name.readline()
	# close the file
        file_name.close()
	# return the completed list
   	return mylist
    
# instructions
print("Do you want to start with a new team or existing team?")  
print("(4) Start with a new team") 
print("(5) Open a file with existing team") 
choice = raw_input()
# if the users choice is a B open the file that they want to open and print all the players in the file
if choice == "5":
	print("Put file name, *.tmd extension*")
        filename = raw_input()
        myPlayers = loadTeam(filename)
	print("You are inside your team, pick the choices below.")
		
		
# if A just print a space to save time and space because the instructions for both A and B are going to be listed below
elif choice == "4":
	myPlayers = []
# this sets the userchouce to 1 but is later changed in the while loop
input = 1
# this creates a loop for the instructions
while input != "0":
	print("(1) Add a player")
	print("(2) Print all players")
	print("(3) Save your player in a file")
	print("(0) To exit *save first*")
	choice = raw_input()
	
        # if the user chooses 1, let them input their information
        if choice == "1":
                print("Name:")
                n = raw_input()
                print("Age:")
                a = raw_input()
                print("Goals:")
                g = raw_input()
		print("Jersey Number:")
		j = raw_input()
		print("Position")
		p = raw_input()
		 
                # this puts in the users data into the list
                myPlayers.append(Player(n, a, g, j, p))
	# if the user choose 2, it will print all the information that they inputed
        elif choice == "2":
		# this creates a loop to print everything in seperate lines from myPlayers
                for x in myPlayers:
			# this calls the def function that we make earlier
                        x.printStats()
	# this saves the players list to a file
	elif choice == "3":
		print("Input name file with .tmd extension, EX: Scholars.tmd")
		file = raw_input()
		#print(playerList)
		saveTeam(myPlayers, file)
	elif choice == "0":	
		# when they exit this happens. 
		print("Goodbye!")
                       
