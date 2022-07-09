
class Monster:
  '''A monster that has some attributes'''
  def __init__(self, health, energy):
    self.health = health
    self.energy = energy
    #private attributes -> realmente es una convención solo(usar un underscore)
    self._id = 5

  def attack(self, amount, other):
    print(f'The monster has attacked!')
    print(f'{amount} damage was dealt')
    other.health -= amount
    self.energy -= 20

  def move(self, speed):
    print('The monster has moved')
    print(f'It is moving at a speed of {speed}')

monster = Monster(10,20)
# hasattr Sintaxis: hasattr(object,'attribute'):boolean
print(hasattr(monster,'health')) # dará un si(igual que hasownproperty de JS)
# setattr Sintaxis: setattr(object,'attribute',newValue)
setattr(monster, 'health',20) # permite dar un nuevo valor
print(monster.health)

# doc Sintaxis: object.__doc__ <- hay que sobrescribirlo ya que retorna None por defecto.Explica que hace la instancia.Para sobrescribirlo se usan triples comillas en la primera linea de la clase,siempre en el mismo lugar
print(monster.__doc__)
