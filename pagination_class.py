#Code implements a pagination based on a string
#Usage example at the last lines of the program
class Pagination:
	def __init__(self, data, items_on_page):
		self.data = data
		self.items_on_page = items_on_page
		self.list_to_work_with = []
		for idx in range(0, len(self.data), self.items_on_page):
			self.list_to_work_with.append(self.data[idx : idx + self.items_on_page])
		find_it_in_the_data = 0
	
	@property
	def page_count(self):
		print(len(self.list_to_work_with))
		return len(self.list_to_work_with)

	@property
	def item_count(self):
		self.items_to_count = 0
		for i in self.data:
			self.items_to_count += 1
		print(self.items_to_count)
		return self.items_to_count

	def count_items_on_page(self, page_number):
		try:
			self.page_number = page_number
			print(len(self.list_to_work_with[self.page_number]))
		except:
			print(f"Exception: Invalid index. Page is missing.")
			return f"Exception: Invalid index. Page is missing."
		else:
			return len(self.list_to_work_with[self.page_number])
		
	def find_page(self, data):
		self.search = data
		self.index_of_found = []
		self.substrings_of_search = []
		for i in range(len(self.search)):
			temp=""
			for j in range(i,len(self.search)):
				temp+=self.search[j]
				self.substrings_of_search.append(temp)
		if len(self.search) == 1:
			for j in self.list_to_work_with:
				for k in j:
					if self.search == k:
						self.index_of_found.append(self.list_to_work_with.index(j))
			try:
				check_it = len(self.index_of_found)
				if check_it == 0:
					raise Exception()
			except:
				print(f"Exception: '{self.search}' is missing on the pages")
				return f"Exception: '{self.search}' is missing on the pages"
			print(self.index_of_found)
			return self.index_of_found
		elif len(self.search) > 1:
			for j in self.list_to_work_with:
				if j.strip() in self.substrings_of_search:
					self.index_of_found.append(self.list_to_work_with.index(j))
			try:
				check_it = len(self.index_of_found)
				if check_it == 0:
					raise Exception()
			except:
				print(f"Exception: '{self.search}' is missing on the pages")
				return f"Exception: '{self.search}' is missing on the pages"					
			print(self.index_of_found)
			return self.index_of_found
			
	def display_page(self, page_number):
		try:
			self.page_number = page_number
			print(self.list_to_work_with[self.page_number])
		except:
			print(f"Exception: Invalid index. Page is missing.")
			return f"Exception: Invalid index. Page is missing."
		else:
			return self.list_to_work_with[self.page_number]	

pages = Pagination('Your beautiful text', 5)
pages.page_count
pages.item_count
pages.count_items_on_page(0)
pages.count_items_on_page(3)
pages.display_page(4)
pages.find_page('Your')
pages.find_page('e')
pages.find_page('beautiful')
pages.find_page('great')
pages.display_page(0)
pages.display_page(4)