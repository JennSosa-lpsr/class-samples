# Create empty dictionary
contacts = {}
# Create while loop to keep going for options.
while input != 0:
	print("(1) Add a phone number.")
	print("(2) Print the full list of contacts.")
	print("(3) Enter a name to retrieve that contact's phone number.")
	print("(0) Exit the Contacts app.")
	input = int(raw_input())
	# If they choose 1, they will be creating a contact
	if input == 1:
		print("Please enter the contact name.")
		a = raw_input()
		print("Please enter the phone number")
		b = raw_input()
		contacts[a] = b
	# If they choose 3 they will be able to access one person.
	elif input == 3:
		print("Input the contact name")
		a = raw_input()
		print("Here ya go!")
		print(contacts[a])
	# If they choose 2 they will be able to print all contacts inputed before.
	elif input == 2:
		print(contacts)

					
	
