print("How many miles away do you live?")
live = raw_input()

live_int = int(live)
if live_int <= 30:
	print("You need a GPA of 2.0 to get in.")
else:
	print("You need a GPA of 2.5 to get in.")
print("What is you GPA?")
GPA = raw_input()
print("What is your ACT score?")
ACT = raw_input()
ACT_int = int(ACT)

GPA_float = float(GPA)

if GPA_float >= 2.0 and live_int <= 30 and ACT_int >= 18:
	print("Great your in!")

if live_int >= 30 and GPA_float >= 2.5 and ACT_int >= 18:
	print("Great your in!")
if live_int > 30 or GPA_float < 2.5 or ACT_int < 18:
	print("Sorry you need all three")
if live_int < 30 or GPA_float < 2.0 or ACT_int < 18:
	print("Sorry you need all three.")
	
