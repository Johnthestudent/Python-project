from typing import List

def check(row_start:int, row_end:int, column_start:int, column_end:int) -> List[List[int]]:
	"""
	Code returns pretty print of a multiplication table
	"""
	product_list = []
	x = range(row_start, row_end+1)
	n = range(column_start, column_end+1)
	for i in x:
		for j in n:
			product_list = [[i*j for j in n] for i in x]

	print(product_list)
	print("that is equal to the following multiplication table: \n")
	print(f"{'':>5}", end="\t")
	for n in range(column_start, column_end+1):
		print(f"{n:5}", end="")
	print("")

	for n in range(row_start, row_end+1):
		print(f"{n:8}", end="")
		for i in range(column_start, column_end+1):
			print(f"{i*n:5}", end="")
		print("")

	return(product_list)
