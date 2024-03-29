def decode(message_file):
	file1 = open(message_file, "r")
	lines_to_list = []	# list of the read lines
	the_nums = []	# list of only the numbers
	for x in file1:
		lines_to_list.append(x.rstrip())
	file1.close()
	helper = 0	# helper variable
	the_words = []	# list of only the words
	for i in lines_to_list:
		helper = int(i.split()[0])
		the_nums.append(helper)
		the_words.append(i.split()[1])
	
	#creates list of lists out of the pyramid of numbers
	def triangle(lvls):
		lst = [1]
		for _ in range(lvls):
			yield lst  
			start = lst[-1] + 1
			lst = list(range(start, start + len(lst) + 1))

	listed_pyramid = list(triangle(24))	#the parameter of the inner function for the amount of numbers
	max_of_pyramid_lines = []	#the max values of each line of the pyramid
	for k in listed_pyramid:
		max_of_pyramid_lines.append(max(k))
	
	helper_index = 0
	final_result = ""	#the string having the words related to the max numbers
	for m in max_of_pyramid_lines:
		helper_index = the_nums.index(m)
		final_result += the_words[helper_index] + " "
	print(final_result)
	return final_result

#usage example
decode("something.txt")