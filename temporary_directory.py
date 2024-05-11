import os
import shutil

#this code creates a temporary directory
class TempDir:
	def __init__(self, tmpwd=""):
		self.tmpwd = tmpwd
		self.temporary = ""

	def __enter__(self):
		try:
			location = os.getcwd()
			self.temporary = self.tmpwd
			os.mkdir(self.temporary)
			os.chdir(self.temporary)
			return os.getcwd()
		except FileExistsError:
			shutil.rmtree(self.temporary)

	def __exit__(self, exc_type, exc_value, exc_traceback):
		os.chdir("..")
		shutil.rmtree(self.temporary)
		return os.getcwd()


c = TempDir("/home")

with TempDir("/home") as t:
	t.getwd()