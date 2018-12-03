def araby(str):

	vowels = ["A","a", "E","e", "I","i", "O","o", "U","u"]

	str_list = str.split

	for l in str_list:

		if l in vowels:

			del(l)

		print(str_list)

	return str_list.join

araby("This computer is old.")