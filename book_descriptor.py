#initialization example at the last lines of the program
class PriceControl:
    """
    Descriptor which don't allow to set price
    less than 0 and more than 100 included.
    """

    def __init__(self):
        self.value = 0

    def __get__(self, instance, owner):
        if self.value > 0 or self.value < 100:
            return self.value

    def __set__(self, instance, value):
        try:
            self.value = value
            if value < 0 or value > 100:
                raise ValueError('Price must be between 0 and 100.')
        except ValueError as e:
            exception_name = type(e).__name__ + ':'
            print(exception_name, e)
            return exception_name, e


class NameControl:
    """
    Descriptor which don't allow to change field value after initialization.
    """

    def __init__(self):
        self.person = ""
        self.book = ""

    def __set__(self, instance, owner):
        try:
            self.person = owner
            self.book = instance
            if self.person != owner:
                raise ValueError('Author can not be changed.')
            if self.book != instance:
                raise ValueError('Name can not be changed.')
        except ValueError as g:
            print(f'Error code: {g}')
            return f'Error code: {g}'

    def __get__(self, instance, owner):
        return self.book, self.person


class Book:
    author = NameControl
    name = NameControl
    price = PriceControl()

    def __init__(self, author, name, price):
        self.author = author
        self.name = name
        self.price = price

    def __setattr__(self, author, name):
        try:
            if author in self.__dict__:
                raise ValueError("Author can not be changed.")
            elif author == 'name' and author in self.__dict__:
                raise ValueError("Name can not be changed.")
        except ValueError as h:
            exception_name = type(h).__name__ + ':'
            print(exception_name, h)
            return exception_name, h
            raise
        else:
            super().__setattr__(author, name)


b = Book("William Faulkner", "The Sound and the Fury", 12)
print(f"Author='{b.author}', Name='{b.name}', Price='{b.price}'")
