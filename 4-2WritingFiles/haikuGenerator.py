# We ask the user for inputs and convert their response into a string.
print("Welcome to the Haiku Generator!")
print("Provide the first line of your haiku.")
x = str(raw_input())
print("Provide the second line to your haiku.")
y = str(raw_input())
print("Provide the third line to your haiku.")
z = str(raw_input())
print("What file would you like to write your haiku into.")
# We assing a variable to whatever they named their file.
myFile = str(raw_input())
print("Done! To view your haiku, type 'cat' and the name of your file at the command line")
# Here we open the file to what they have named it.
my_File = open((myFile), "a")
# We put their haiku together on seperate lines and save their input on that file.
my_File.write( x + '\n' + y + '\n' + z + '\n')
# We closde the file
my_File.close()
