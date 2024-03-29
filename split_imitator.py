from typing import List

def split(data: str, sep=None, maxsplit=-1):
	"""
	Code imitates the built-in split function  
	"""
	result_str = []
	number_of_substrings = maxsplit + 1
	tmp  = ''
	#in case the data is an empty string
	if(len(data) == 0):
		print(result_str)
		return result_str
	#in cas the data is not an empty string
	elif(len(data) > 0):
		#this new_data is needed, so that the whitespaces are taken down from the left and right
		new_data = data.strip()
		#if there is no separator character and maxsplit is not given (default value is -1)
		if(sep==None and maxsplit == -1):
			for words in new_data:
				if words == ' ':
					result_str.append(tmp)
					tmp = ''
				else:
					tmp += words
			result_str.append(tmp)
			result_str = list(filter(None, result_str))
			print(result_str)
			return result_str
		#if there is no separator character and maxsplit is 0
		elif(sep==None and maxsplit == 0):
			result_str.append(new_data)
			print(result_str)
			return result_str
		#if there is no separator, but the maxsplit is bigger than zero
		elif(sep==None and maxsplit > 0):
			if(maxsplit == 1):
				K = 1  # kth occurrence
				idx = -1
				for i in range(K):
					idx = new_data.find(" ", idx + 1)
				
				if idx == -1:
					new_str = new_data
					rest = ""
				else:
					new_str = new_data[:idx]
					rest = new_data[idx+1:]
				
				#creating the other list with given number of elements based on maxsplit
				result_str = [] * number_of_substrings
				result_str.append(new_str)
				result_str.append(rest.strip())
				print(result_str)
				return result_str
			#additional test
			if(maxsplit > 1):
				K = 1  # kth occurrence
				idx = -1
				for i in range(K):
					idx = new_data.find(" ", idx + 1)
				
				if idx == -1:
					new_str = new_data
					rest = ""
				else:
					new_str = new_data[:idx]
					rest = new_data[idx+1:]
				
				#next step
				for j in range(K):
					idx = rest.find(" ", idx + 1)
				if idx == -1:
					new_str_1 = rest
					rest_1 = ""
				else:
					new_str_1 = rest[:idx]
					rest_1 = rest[idx+1:]
				#creating the other list with given number of elements based on maxsplit
				result_str = [] * number_of_substrings
				result_str.append(new_str)
				result_str.append(new_str_1.strip())
				result_str.append(rest_1.strip())
				print(result_str)
				return result_str				
		#if there is a separator given and the maxsplit is bigger than zero
		elif(sep!=None and maxsplit > 0):
			occurences_of_sep = new_data.count(sep)
			new_data = new_data.replace(sep, '', 1)
			result_str.append(new_data)
			print(result_str)
			return result_str
		else:
			for words in new_data:
				if words == '':
					result_str.append(tmp)
					tmp = ''
				elif words == sep:
					result_str.append(tmp)
					tmp = ''
				else:
					tmp += words
			result_str.append(tmp)
			print(result_str)
			return(result_str)

split('') 
#its expected result: []
split(',123,', sep=',')
#its expected result: ['', '123', '']
split('test')
#its expected result: ['test']
split('Python    2     3', maxsplit=1)
#its expected result: ['Python', '2     3']
split('    test     6    7', maxsplit=1)
#its expected result: ['test', '6    7']
split('    Hi     8    9', maxsplit=0) 
#its expected result: ['Hi     8    9']
split('    set   3     4')
#its expected result: ['set', '3', '4']
split('set;:23', sep=';:', maxsplit=0)
#its expected result: ['set;:23']
split('set;:;:23', sep=';:', maxsplit=2)
#its expected result: ['set', '', '23']