#Code does a simple value increase based on a start and stop value
class Counter:
	def __init__(self, start = 0, stop = 1000):
		self.start = start
		self.stop = stop

	def increment(self):
		self.start = self.start + 1
		if(self.start == self.stop):
			print("Maximum value is reached")
			return "Maximum value is reached"

	def get(self):
		if(self.start == self.stop + 1):
			print(self.start - 1)
			return self.start - 1
		elif(self.start <= self.stop):
			print(self.start)
			return self.start

c = Counter(start=42)
c.increment()
c.get()

d = Counter()
d.increment()
d.get()
d.increment()
d.get()


e = Counter(start=42, stop=43)
e.increment()
e.get()
e.increment()
e.get()

f = Counter(stop=43)
f.increment()
f.get()