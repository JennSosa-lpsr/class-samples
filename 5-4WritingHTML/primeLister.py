# Takes myNum, an integer
# Returns True if myNum is prime
# Returns False if myNum is composite
def isPrime(y, list):
	x = range(1,int(y))
	number = y - 2 
        goes_on = 0
	# We create a for loop to check if prime.
        for num in x:
                remainder = int(y) % int(num)
		#if the remainder is not 0 let the range keep going.
                if remainder != 0:
                        goes_on = goes_on + 1
                        	# if its prime add it to the list.
			if goes_on == number:
				print(y)
				list.append(y)
	

# Make an empty list.
primeLister = []
# Open the file for primes.
myPrimes = open("primes.txt", "w")
# Make a range for the def function to do.
rangeList = range(2, 10000)
# make a For loop for the range to go on and check each number.
for i in rangeList:
	current_number =  isPrime(i, primeLister)
# For this loop we write on the file each time it's true.
for x in primeLister:
	myPrimes.write(str(x) + "\n")		
#We close the file.
myPrimes.close()
