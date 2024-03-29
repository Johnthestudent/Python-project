from __future__ import annotations
from typing import Type

#Code uses __add__, __str__, __eq__, __lt__, __gt__ magic values to change curriencies
#Used currency values in the Currency class
#Example of usage, and the expected output at the last lines of the program
class Currency:
    """
    1 EUR = 2 USD = 100 GBP

    1 EUR = 2 USD    ;  1 EUR = 100 GBP
    1 USD = 0.5 EUR  ;  1 USD = 50 GBP
    1 GBP = 0.02 USD ;  1 GBP = 0.01 EUR
    """

    def __init__(self, value: float):
        self.value = value

    @classmethod
    def course(cls, other_cls: Type[Currency]) -> str:
        cls.other_cls = other_cls
        return other_cls

    def to_currency(self, other_cls: Type[Currency]):
        self.other_cls = other_cls
        return self.other_cls


class Euro(Currency):
    def __init__(self, value: float):
        self.value = value

    def __str__(self):
        return str(self.value) + " EUR"

    @classmethod
    def course(cls, other_cls: Type[Currency]):
        cls.other_cls = other_cls
        if other_cls == Pound:
            return "100.0 GBP for 1 EUR"
        elif other_cls == Dollar:
            return "2.0 USD for 1 EUR"
        elif other_cls == Euro:
            return "1.0 EUR for 1 EUR"

    def to_currency(self, other_cls: Type[Currency]):
        self.other_cls = other_cls
        if other_cls == Pound:
            return Pound(str(float(100 * self.value)))
        elif other_cls == Dollar:
            return Dollar(str(float(2 * self.value)))
        elif other_cls == Euro:
            return Euro(str(float(self.value)))

    def __add__(self, val2):
        if (str(val2)[-3:]) == 'GBP':
            help_that = float(str(val2).split(" ")[0])
            return Euro(str(float(self.value) + (float(0.01 * help_that))))
        elif (str(val2)[-3:]) == 'USD':
            help_that = float(str(val2).split(" ")[0])
            return Euro(str(float(self.value) + (float(0.5 * help_that))))
        elif (str(val2)[-3:]) == 'EUR':
            return Euro(str(float(self.value) + (float(str(val2).split(" ")[0]))))

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def is_equal(val_1, val_2):
        if (str(val_2)[-3:]) == 'EUR':
            second_number = Euro(float(str(val_2).split(" ")[0]))
            first_number = Euro(float(str(val_1).split(" ")[0]))
            if (first_number == second_number):
                return True
            else:
                return False
        elif (str(val_2)[-3:]) == 'USD':
            first_number = Euro(float(str(val_1).split(" ")[0]))
            second_number = Euro(float(float(str(val_2).split(" ")[0]) * 0.5))
            if (first_number == second_number):
                return True
            else:
                return False
        elif (str(val_2)[-3:]) == 'GBP':
            first_number = Euro(float(str(val_1).split(" ")[0]))
            second_number = Euro(float(float(str(val_2).split(" ")[0]) * 0.01))
            if (first_number == second_number):
                return True
            else:
                return False

    def __lt__(self, other):
        return self.value < other.value

    def is_less(val_1, val_2):
        if (str(val_2)[-3:]) == 'EUR':
            second_number = Euro(float(str(val_2).split(" ")[0]))
            first_number = Euro(float(str(val_1).split(" ")[0]))
            if (first_number < second_number):
                return True
            else:
                return False
        elif (str(val_2)[-3:]) == 'USD':
            first_number = Euro(float(str(val_1).split(" ")[0]))
            second_number = Euro(float(float(str(val_2).split(" ")[0]) * 0.5))
            if (first_number < second_number):
                return True
            else:
                return False
        elif (str(val_2)[-3:]) == 'GBP':
            first_number = Euro(float(str(val_1).split(" ")[0]))
            second_number = Euro(float(float(str(val_2).split(" ")[0]) * 0.01))
            if (first_number < second_number):
                return True
            else:
                return False

    def __gt__(self, other):
        return self.value > other.value

    def is_more(val_1, val_2):
        if (str(val_2)[-3:]) == 'EUR':
            second_number = Euro(float(str(val_2).split(" ")[0]))
            first_number = Euro(float(str(val_1).split(" ")[0]))
            if (first_number > second_number):
                return True
            else:
                return False
        elif (str(val_2)[-3:]) == 'USD':
            first_number = Euro(float(str(val_1).split(" ")[0]))
            second_number = Euro(float(float(str(val_2).split(" ")[0]) * 0.5))
            if (first_number > second_number):
                return True
            else:
                return False
        elif (str(val_2)[-3:]) == 'GBP':
            first_number = Euro(float(str(val_1).split(" ")[0]))
            second_number = Euro(float(float(str(val_2).split(" ")[0]) * 0.01))
            if (first_number > second_number):
                return True
            else:
                return False


class Dollar(Currency):
    def __init__(self, value: float):
        self.value = value

    def __str__(self):
        return str(self.value) + " USD"

    @classmethod
    def course(cls, other_cls: Type[Currency]):
        cls.other_cls = other_cls
        if other_cls == Pound:
            return "50.0 GBP for 1 USD"
        elif other_cls == Euro:
            return "0.5 EUR for 1 USD"
        elif other_cls == Dollar:
            return "1.0 USD for 1 USD"

    def to_currency(self, other_cls: Type[Currency]):
        self.other_cls = other_cls
        if other_cls == Pound:
            return Pound(str(float(50 * self.value)))
        elif other_cls == Dollar:
            return Dollar(str(float(self.value)))
        elif other_cls == Euro:
            return Euro(str(float(0.5 * self.value)))

    def __add__(self, val2):
        if (str(val2)[-3:]) == 'GBP':
            helper_var = float(str(val2).split(" ")[0])
            return Dollar(str(float(self.value) + (float(0.02 * helper_var))))
        elif (str(val2)[-3:]) == 'EUR':
            help_it = float(str(val2).split(" ")[0])
            return Dollar(str(float(self.value) + (float(help_it * 2))))
        elif (str(val2)[-3:]) == 'USD':
            return Dollar(str(float(self.value) + (float(str(val2).split(" ")[0]))))

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def is_equal(val_1, val_2):
        print(type(val_1))
        print(type(val_2))
        if (str(val_2)[-3:]) == 'USD':
            second_number = Dollar(float(str(val_2).split(" ")[0]))
            first_number = Dollar(float(str(val_1).split(" ")[0]))
            if (first_number == second_number):
                return True
            else:
                return False
        elif (str(val_2)[-3:]) == 'EUR':
            first_number = Dollar(float(str(val_1).split(" ")[0]))
            second_number = Dollar(float(float(str(val_2).split(" ")[0]) * 2))
            if (first_number == second_number):
                return True
            else:
                return False
        elif (str(val_2)[-3:]) == 'GBP':
            first_number = Dollar(float(str(val_1).split(" ")[0]))
            second_number = Dollar(float(float(str(val_2).split(" ")[0]) * 0.02))
            if (first_number == second_number):
                return True
            else:
                return False

    def __lt__(self, other):
        return self.value < other.value

    def is_less(val_1, val_2):
        if (str(val_2)[-3:]) == 'USD':
            second_number = Dollar(float(str(val_2).split(" ")[0]))
            first_number = Dollar(float(str(val_1).split(" ")[0]))
            if (first_number < second_number):
                return True
            else:
                return False
        elif (str(val_2)[-3:]) == 'EUR':
            first_number = Dollar(float(str(val_1).split(" ")[0]))
            second_number = Dollar(float(float(str(val_2).split(" ")[0]) * 2))
            if (first_number < second_number):
                return True
            else:
                return False
        elif (str(val_2)[-3:]) == 'GBP':
            first_number = Dollar(float(str(val_1).split(" ")[0]))
            second_number = Dollar(float(float(str(val_2).split(" ")[0]) * 0.02))
            if (first_number < second_number):
                return True
            else:
                return False

    def __gt__(self, other):
        return self.value > other.value

    def is_more(val_1, val_2):
        if (str(val_2)[-3:]) == 'USD':
            second_number = Dollar(float(str(val_2).split(" ")[0]))
            first_number = Dollar(float(str(val_1).split(" ")[0]))
            if (first_number > second_number):
                return True
            else:
                return False
        elif (str(val_2)[-3:]) == 'EUR':
            first_number = Dollar(float(str(val_1).split(" ")[0]))
            second_number = Dollar(float(float(str(val_2).split(" ")[0]) * 2))
            if (first_number > second_number):
                return True
            else:
                return False
        elif (str(val_2)[-3:]) == 'GBP':
            first_number = Dollar(float(str(val_1).split(" ")[0]))
            second_number = Dollar(float(float(str(val_2).split(" ")[0]) * 0.02))
            if (first_number > second_number):
                return True
            else:
                return False


class Pound(Currency):
    def __init__(self, value: float):
        self.value = value

    def __str__(self):
        return str(self.value) + " GBP"

    @classmethod
    def course(cls, other_cls: Type[Currency]):
        cls.other_cls = other_cls
        if other_cls == Dollar:
            return "0.02 USD for 1 GBP"
        elif other_cls == Euro:
            return "0.01 EUR for 1 GBP"
        elif other_cls == Pound:
            return "1.0 GBP for 1 GBP"

    def to_currency(self, other_cls: Type[Currency]):
        self.other_cls = other_cls
        if other_cls == Pound:
            return Pound(str(float(self.value)))
        elif other_cls == Dollar:
            return Dollar(str(float(0.02 * self.value)))
        elif other_cls == Euro:
            return Euro(str(float(0.01 * self.value)))

    def __add__(self, val2):
        if (str(val2)[-3:]) == 'USD':
            help_the_multiplication = float(str(val2).split(" ")[0])
            return Pound(str(float(self.value) + (float(50 * help_the_multiplication))))
        elif (str(val2)[-3:]) == 'EUR':
            help_the_multiplication = float(str(val2).split(" ")[0])
            return Pound(str(float(self.value) + (float(100 * help_the_multiplication))))
        elif (str(val2)[-3:]) == 'GBP':
            return Pound(str(float(self.value) + (float(str(val2).split(" ")[0]))))

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def is_equal(val_1, val_2):
        if (str(val_2)[-3:]) == 'GBP':
            second_number = Pound(float(str(val_2).split(" ")[0]))
            first_number = Pound(float(str(val_1).split(" ")[0]))
            if (first_number == second_number):
                return True
            else:
                return False
        elif (str(val_2)[-3:]) == 'EUR':
            first_number = Pound(float(str(val_1).split(" ")[0]))
            helper_number = float(str(val_2).split(" ")[0])
            second_number = Pound(float(helper_number * 100))
            if (first_number == second_number):
                return True
            else:
                return False
        elif (str(val_2)[-3:]) == 'USD':
            first_number = Pound(float(str(val_1).split(" ")[0]))
            helper_number = float(str(val_2).split(" ")[0])
            second_number = Pound(float(helper_number * 50))
            if (first_number == second_number):
                return True
            else:
                return False

    def __lt__(self, other):
        return self.value < other.value

    def is_less(val_1, val_2):
        if (str(val_2)[-3:]) == 'GBP':
            second_number = Pound(float(str(val_2).split(" ")[0]))
            first_number = Pound(float(str(val_1).split(" ")[0]))
            if (first_number < second_number):
                return True
            else:
                return False
        elif (str(val_2)[-3:]) == 'EUR':
            first_number = Pound(float(str(val_1).split(" ")[0]))
            helper_number = float(str(val_2).split(" ")[0])
            second_number = Pound(float(helper_number * 100))
            if (first_number < second_number):
                return True
            else:
                return False
        elif (str(val_2)[-3:]) == 'USD':
            first_number = Pound(float(str(val_1).split(" ")[0]))
            helper_number = float(str(val_2).split(" ")[0])
            second_number = Pound(float(helper_number * 50))
            if (first_number < second_number):
                return True
            else:
                return False

    def __gt__(self, other):
        return self.value > other.value

    def is_more(val_1, val_2):
        if (str(val_2)[-3:]) == 'GBP':
            second_number = Pound(float(str(val_2).split(" ")[0]))
            first_number = Pound(float(str(val_1).split(" ")[0]))
            if (first_number > second_number):
                return True
            else:
                return False
        elif (str(val_2)[-3:]) == 'EUR':
            first_number = Pound(float(str(val_1).split(" ")[0]))
            helper_number = float(str(val_2).split(" ")[0])
            second_number = Pound(float(helper_number * 100))
            if (first_number > second_number):
                return True
            else:
                return False
        elif (str(val_2)[-3:]) == 'USD':
            first_number = Pound(float(str(val_1).split(" ")[0]))
            helper_number = float(str(val_2).split(" ")[0])
            second_number = Pound(float(helper_number * 50))
            if (first_number > second_number):
                return True
            else:
                return False

"""print(
	  f"Euro.course(Pound)   ==> {Euro.course(Pound)}\n"
	  f"Dollar.course(Pound) ==> {Dollar.course(Pound)}\n"
	  f"Pound.course(Euro)   ==> {Pound.course(Euro)}\n"
  )"""
"""  
  Euro.course(Pound)   ==> 100.0 GBP for 1 EUR
  Dollar.course(Pound) ==> 50.0 GBP for 1 USD
  Pound.course(Euro)   ==> 0.01 EUR for 1 GBP
  
"""
"""
e = Euro(100)
r = Pound(100)
d = Dollar(200)
"""
"""
print(
	  f"e = {e}\n"
	  f"e.to_currency(Dollar) = {e.to_currency(Dollar)}\n"
	  f"e.to_currency(Pound) = {e.to_currency(Pound)}\n"
	  f"e.to_currency(Euro)   = {e.to_currency(Euro)}\n"
)"""
"""
  e = 100 EUR
  e.to_currency(Dollar) = 200.0 USD  # Dollar instance printed
  e.to_currency(Pound) = 10000.0 GBP  # Pound instance printed
  e.to_currency(Euro)   = 100.0 EUR  # Euro instance printed
"""

"""
print(
	  f"r = {r}\n"
	  f"r.to_currency(Dollar) = {r.to_currency(Dollar)}\n"
	  f"r.to_currency(Euro)   = {r.to_currency(Euro)}\n"
	  f"r.to_currency(Pound) = {r.to_currency(Pound)}\n"
  )"""

"""
  r = 100 GBP
  r.to_currency(Dollar) = 2.0 USD  # Dollar instance printed
  r.to_currency(Euro)   = 1.0 EUR  # Euro instance printed
  r.to_currency(Pound) = 100.0 GBP  # Pound instance printed
"""


e = Euro(55)
f = Euro(50)
r = Pound(5)
d = Dollar(90)
print(
	f"e more f  =>  {e.is_more(f)}\n"
  )

"""
  e + r  =>  101.0 EUR  # Euro instance printed
  r + d  =>  10100.0 GBP  # Pound instance printed
  d + e  =>  400.0 USD  # Dollar instance printed
"""