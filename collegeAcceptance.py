print("How old are you?")
age = int(raw_input())

print("What's your GPA?")
GPA = float(raw_input())

# if GPA is over 3.0 and age is over 16, accept
if GPA > 3.0 and age > 16:
	print("Congrats, you're into Columnia.")	
else:
	print("Sorry, guess you'll have to go to Harvard instead.")
