# open a file for writing
# r is for reading
# r + is for reading and writing(existing file)
# w is writing (be careful! starts writing from the beginning.)
# a is append - is for writing *from the end*
myFile = open("numlist.txt", "w")

# creat a list to write to my file
nums = range(1, 501)

# write each item to the file
for n in nums:
	myFile.write(str(n) + '\n' )

# close the file
myFile.close()


