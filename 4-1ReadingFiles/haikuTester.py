import time
 
myFirstHaiku = open('haiku1.txt', 'r')
 
print('Here is the first haiku:') 
print(myFirstHaiku.read())
 
print('I will give you the second haiku line by line.') 
print('How many seconds should I wait between lines?') 
seconds = int(raw_input())
 
mySecondHaiku = open('haiku2.txt', 'r')
 
lineToPrint = mySecondHaiku.readline() 
while lineToPrint != "":
    print(lineToPrint)
    lineToPrint = mySecondHaiku.readline()
    time.sleep(seconds) 
myFirstHaiku.close()
mySecondHaiku.close()
