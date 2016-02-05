# We ask the user for an input.
print("Hi, welcome to the Haiku Reader!")
print("Choose one.")
print("(3) For a Haiku about a silly person")
print("(4) For a Haiku about writing haikus")
haiku = int(raw_input())
# We open both text files.
myHaiku3 = open('haiku3.txt', 'r')
myHaiku4 = open('haiku4.txt', 'r')

# We create an if statement to match their user input.
if haiku ==  3:
	print(myHaiku3.read())
else:
	print(myHaiku4.read())
