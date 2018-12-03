Num_of_Numbers = 5

num_list = []

def main():
	for i in range(Num_of_Numbers):
		userInput = int(input("please enter number: "))
		num_list.append(userInput)

	info()

def find_lowest(anything):
	lowestNumber = min(anything)
	return lowestNumber

def totalN(anything):
	
	total = 0

	for i in anything:
		total += i

	return total
	
def info():
	print("The lowest number is:  ", str(find_lowest(num_list)))
	print("The total is:  ", str(totalN(num_list)))

main()