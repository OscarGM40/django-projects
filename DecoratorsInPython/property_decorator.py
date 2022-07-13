from datetime import datetime

class Generic:
  def __init__(self,**kwargs):
    super().__init__(**kwargs)
    self._x = 10 # variable privada
    
  def getter(self):
    print(datetime.now())
    print('getting x...')
    return self._x

  def setter(self,value):
    print(datetime.now())
    print('setting x')
    self._x = value

  def deleter(self):
    print(datetime.now())
    print('deleting x...')
    del self._x

  x = property(getter,setter,deleter) # metodo property muy importante

generic = Generic()
print(generic.x)
generic.x = 5
del generic.x

# FORMA CON DECORADOR @PROPERTY
class GenericDecorated:
  def __init__(self,x):
    self._x = x 
 
  @property
  def x(self):
    return self._x

  @x.setter
  def x(self,value):
    self._x =value

  @x.deleter
  def x(self):
    del self._x
