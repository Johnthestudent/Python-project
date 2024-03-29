
def validate(func):
    '''
    Decorator returns a value stating whether the pixel is valid or not
    '''
    def inside(x, y, z):
        if((x >= 0 and x <= 256) and (y >= 0 and y <= 256) and (z >= 0 and z <= 256)):
            return "Pixel created!"
        else:
            return "Function call is not valid!"
        func(x, y, z)
    return inside

@validate
def set_pixel(x: int, y: int, z: int) -> str:
  return "Pixel created!"
