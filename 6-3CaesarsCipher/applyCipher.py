# Imports string so that we could use it to access the alphabet.
import string

# applyCipher.py
# A program to encrypt/decrypt user text
# Using Ceasar's Cipher
# Author: rc.sosa.jennifer [at] leadps.org
# Makes a mapping of encoded alphabet to decoded alphabet 
# Arguments: key
# Returns: dictionary of mapped letters
def createDictionary(key):
	# Make our alphabet(lowercase and uppercase.)
	alphabetL = string.ascii_lowercase
	alphabetU = string.ascii_uppercase
	# Make empty Dictionary.
	Dictionary = {}
	# We use a for loop to access the range to the length of the alphabet.
	for a in range(0, len(alphabetU)):
		Dictionary[alphabetU[(a - key) % 26]] = alphabetU[a] 	
	for a in range(0, len(alphabetL)):
		Dictionary[alphabetL[(a - key) % 26]] = alphabetL[a]
	# Append more in a loop.
	for a in range(32, 64):
		Dictionary[chr(a)] = chr(a)
	# Return our dictionary.
	return Dictionary

# Gets the encrypted message from the user.
# Arguments: none
# Returns: encoded message
def getMessage():
	# Ask user for message and make it a string that will be returned.
	print("Good. What's the message you would like to be encoded?")
	message = raw_input()
	return message	


# For each letter in the message,  decodes and records.
# Arguments: encoded message, dictionary
# Returns: decoded message.
def decodeMessage(message, dictionary):
	# Made a blank variable.
	newMsg = ""
	# For loop is used to append variables using the key to decode the message.
	for l in message:
		newMsg = newMsg + dictionary[l]
	return newMsg
# Outputs the decoded message to the terminal.
# Arguments: decoded message.
# Returns: none.
def printMessage(message):
	print(message)

# Execution starts here.
# Made try and except to tell the user if an input is wrong.
try:
	# Ask for key and make variable.
	print("What key would be best?")
	key = int(raw_input())

	
	dictionary = createDictionary(key)
	encodedMessage = getMessage()
	decodedMessage = decodeMessage(encodedMessage, dictionary)
	print("Here's your message, bye!")
	printMessage(decodedMessage)

except: 
	print("Sorry this could not be done.")
