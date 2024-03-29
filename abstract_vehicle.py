from abc import ABC
# from abc import abstractmethod

#Code shows a vehicle analysis based abstract class example
#Usage around the last lines of the program
class Vehicle(ABC):
	def __init__(
			self,
			brand_name: str,
			year_of_issue: int,
			base_price: int,
			mileage: int
	):
		pass

	def wheels_num(self) -> int:
		return 0

	def vehicle_type(self) -> str:
		pass

	def is_motorcycle(self) -> bool:
		pass

	def purchase_price(self) -> float:
		pass


# Don't change class implementation
class Car(Vehicle):
	def __init__(
			self,
			brand_name: str,
			year_of_issue: int,
			base_price: int,
			mileage: int
	):
		self.brand_name = brand_name
		self.year_of_issue = year_of_issue
		self.base_price = base_price
		self.mileage = mileage
	
	def wheels_num(self):
		return 4
		
	def vehicle_type(self):
		self.vehicle_name = self.brand_name + " " + self.__class__.__name__
		return self.vehicle_name

	def is_motorcycle(self):
		if self.wheels_num() == 2:
			return True
		else:
			return False

	@property
	def purchase_price(self):
		self.result_price = (self.base_price - 0.1 * self.mileage)
		if self.result_price > 100000.0:
			return self.result_price
		elif self.result_price < 100000.0:
			self.result_price = 100000.0
			return self.result_price
	
# Don't change class implementation
class Motorcycle(Vehicle):
	def __init__(
			self,
			brand_name: str,
			year_of_issue: int,
			base_price: int,
			mileage: int
	):
		self.brand_name = brand_name
		self.year_of_issue = year_of_issue
		self.base_price = base_price
		self.mileage = mileage
		
	def wheels_num(self):
		return 2

	def vehicle_type(self):
		self.vehicle_name = self.brand_name + " " + self.__class__.__name__
		return self.vehicle_name

	def is_motorcycle(self):
		if self.wheels_num() == 2:
			return True
		else:
			return False

	@property		
	def purchase_price(self):
		self.result_price = (self.base_price - 0.1 * self.mileage)
		if self.result_price > 100000.0:
			return self.result_price
		elif self.result_price < 100000.0:
			self.result_price = 100000.0
			return self.result_price

# Don't change class implementation
class Truck(Vehicle):
	def __init__(
			self,
			brand_name: str,
			year_of_issue: int,
			base_price: int,
			mileage: int
	):
		self.brand_name = brand_name
		self.year_of_issue = year_of_issue
		self.base_price = base_price
		self.mileage = mileage
		
	def wheels_num(self):
		return 10
		
	def vehicle_type(self):
		self.vehicle_name = self.brand_name + " " + self.__class__.__name__
		return self.vehicle_name

	def is_motorcycle(self):
		if self.wheels_num() == 2:
			return True
		else:
			return False

	@property		
	def purchase_price(self):
		self.result_price = (self.base_price - 0.1 * self.mileage)
		if self.result_price > 100000.0:
			return self.result_price
		elif self.result_price < 100000.0:
			self.result_price = 100000.0
			return self.result_price

# Don't change class implementation
class Bus(Vehicle):
	def __init__(
			self,
			brand_name: str,
			year_of_issue: int,
			base_price: int,
			mileage: int
	):
		self.brand_name = brand_name
		self.year_of_issue = year_of_issue
		self.base_price = base_price
		self.mileage = mileage
		
	def wheels_num(self):
		return 6

	def vehicle_type(self):
		self.vehicle_name = self.brand_name + " " + self.__class__.__name__
		return self.vehicle_name

	def is_motorcycle(self):
		if self.wheels_num() == 2:
			return True
		else:
			return False
	
	@property
	def purchase_price(self):
		self.result_price = (self.base_price - 0.1 * self.mileage)
		if self.result_price > 100000.0:
			return self.result_price
		elif self.result_price < 100000.0:
			self.result_price = 100000.0
			return self.result_price

vehicles = (
	Car(brand_name="Toyota", year_of_issue=2020, base_price=1_000_000, mileage=150_000),
	Motorcycle(brand_name="Suzuki", year_of_issue=2015, base_price=800_000, mileage=35_000),
	Truck(brand_name="Scania", year_of_issue=2018, base_price=15_000_000, mileage=850_000),
	Bus(brand_name="MAN", year_of_issue=2000, base_price=10_000_000, mileage=950_000)
)

for vehicle in vehicles:
	print(
		f"Vehicle type={vehicle.vehicle_type()}\n"
		f"Is motorcycle={vehicle.is_motorcycle()}\n"
		f"Purchase price={vehicle.purchase_price}\n"
	)
