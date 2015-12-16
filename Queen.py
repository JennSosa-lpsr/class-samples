print("Welcome to Jenn's Quest!")
print("Please name your character.")
character = raw_input()

print("Enter strength (1-10)")
strength = raw_input()
strength_int =int(strength)

print("Enter health (1-10)")
health = raw_input()
health_int = int(health)

print("Enter luck (1-10)")
luck = raw_input()
luck_int = int(luck)

x = int(luck_int + health_int + strength_int)
if x > 15:
        print("You gave your character too many points! Default values have been assigned, " + character_str + " strength: 5, health: 5,  luck:5. ")

else:
        print("Your character's name is  " + character + " strength: " + str(strength_int) + ", luck: " + str(luck_int) + ", health: " +str(health_int) + ".")


print(" " + character + " You've come to a fork in the road. Do you want to go right or left? Enter right or left. ")
direction = str(raw_input())
right = ("right")
left = ("left")
if direction == right:
        print("Oh no! You've encountered a powerful wizard!")
if luck_int >= 6 and direction == right:
        print(" Woah! It was just Harry Potter, your luck helped and he was very generous and invited you in for tea. You've won the game.")

elif luck_int < 6:
        print(" I'm sorry it was  Voldemort who happened to have his powers back. Your luck didn't help and he killed you. Sorry, you've lost the game.")

else:
        print("You went left and encountered The Rock, with all forces combined nothing beats him. Sorry you lost the game.")




