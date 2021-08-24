kill = False

while not kill:
	n1 = int(input("please enter a number: "))
	if n1 == 0:
		kill = True
		break
	n2 = int(input("please enter 2nd number: "))
	if n2 == 0:
		kill = True
		break
	while True:
		i = input("Please enter a operation(a/s/m/d)[q to quit]: ")
		if i == "q":
			kill = True
			break
		elif i not in ["a","s","m","d"]:
			print("I dont understand that please try again!")
			continue
		elif i == "s":
			print(n1 - n2,"is your answer")
			break
		elif i == "a":
			print(n1 + n2,"is your answer")
			break
		elif i == "m":
			print(n1 * n2,"is your answer")
			break
		elif i == "d":
			print(n1 / n2,"is your answer")
			break
