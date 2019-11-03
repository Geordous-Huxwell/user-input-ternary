ageInt = 1
while(ageInt):
	ageInput = input("How old is the person?(0 to exit) ")
	try:
		ageInt = int(ageInput)
	except ValueError:
		print("Please enter a valid number")
	else:
		if(ageInt>=65):
			print("Free Drinks!")
		elif (ageInt >= 18):
			print("Let them in!")
		elif(ageInt>0):
			print("Call the cops!")
		else:
			if (ageInt != 0): print("Please enter a valid number")

