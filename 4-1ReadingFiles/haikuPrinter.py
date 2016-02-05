# import the module
import time
 
# this sets a file object.
myFirstHaiku = open('haiku1.txt', 'r')
 
# print out all of this.
print('Here is the first haiku:') 
print(myFirstHaiku.read())
 
print('I will give you the second haiku line by line.') 
print('How many seconds should I wait between lines?') 
# we convert their input into an integer
seconds = int(raw_input())

# This focuses on the object text file. 
mySecondHaiku = open('haiku2.txt', 'r')
 
# We tell the program to print out line by line.
lineToPrint = mySecondHaiku.readline() 
# We set a while loop to print out each line with seconds in between according to the user.
while lineToPrint != "":
    print(lineToPrint)
    lineToPrint = mySecondHaiku.readline()
    time.sleep(seconds)
# We close both files. 
myFirstHaiku.close()
mySecondHaiku.close()
