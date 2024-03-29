#Code tries to change the working directory to the class parameter given one
import os


class Cd:
	def __init__(self, nwd):
		try:
			self.nwd = nwd
			path = nwd
			os.path.isdir(path)
			if os.path.isdir(path) == False:
				raise ValueError("passed directory is not a directory or does not exist")
		except ValueError as f:
			print(f'Error code: {f}')
		
	def __enter__(self):
		cwd = os.getcwd()
		os.getcwd()
		try:
			os.chdir("nwd")
		except ValueError as g:
			print(f'Error code: {g}')
	
	def __exit__(self, exc_type, exc_val, exc_tb):
		os.chdir('..')
	
c = Cd('/home')
