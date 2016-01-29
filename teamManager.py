# create a player class
class Player(object):
	def __init__(self, name, age, goals):
		self.name = name
		self.age = age
		self.goals = goals
# Allows us to print back their players input.
	def printStats(self):
		print("Name: " + self.name)
		print("Age: " + str(self.age))
		print("Goals: " + str(self.goals))
# Create an empty list.
myPlayers = []
print("Welcome to our soccer team!")
print("(1) Add Player")
print("(2) Print all")
# Convert their input into an int.
x = int(raw_input())
# Create while loop to repeat choices.
while x != 0:
	# Create an if statement if they choose to add player.
	if x == 1:
		print("You want to add a player, fill in the info:")
		print("Name. ")
		n = raw_input()
		print("Age. ")
		a = int(raw_input())
		print("Goals. ")
		g = int(raw_input())
		# Add their attributes to the list.
		myPlayers.append(Player(n, a, g))
		print("Good to go!")
		print("(1) Add another player.")
		print("(2) Player status")
		print("(0) to exit")
		x = int(raw_input())
	# Else and if incase they choose 2. To print all players.
	elif x ==  2 :
		print("Here are the status.")
		# Use for to print out each attribute from the append.
		for p in myPlayers:
			# P is the variable attaching to function of stats.
			p.printStats()
		x =  int(raw_input())
		#Ask again till they choose to exit.
		print("(1) Add another player.")
	        print("(2) Player status")
                print("(0) to exit")

			
