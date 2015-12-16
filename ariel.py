
# We set a list variable
people = ["Maria","Hailey","Fatima","Julie","Keili"]
# We set a for loop to print the names in a separate line
# We create a second list
peeps = ["Rodolfo","Noemi","Ramon","Michelle","Allison"]
# On the next two lines we convert the lists into strings.
# We add the two variables
family = peeps + people
# We ask for it to display them together.
# We set a loop for it to print it and display
for family in family:
    print(family)
num = 1
while num <= 5:
	print(str(num) + str(people))
	num = num + 1

family.sort()
family.reverse()
