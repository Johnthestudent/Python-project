#Code checks whether the class is a singleton class or not
class Sun(object):
    def inst():
        def __new__(cls):
            if not hasattr(cls, 'instance'):
                cls.instance = super(Sun, cls).__new__(cls)
            return cls.instance
			
p = Sun.inst()
f = Sun.inst()
p is f
