# recuerda que en Python se usa snake_case
class Monster():
  health = 90
  energy = 40

  # cualquier método en Python,incluso el constructor, empieza con def
  def __init__(self,health,energy,name):
    self.health = health
    self.energy = energy
    self.name = name
    
  # Python automáticamente pasa siempre una referencia a la clase como primer argumento en cualquier método que cree.Por convención se llama self
  def attack(self,monster,amount):
    print(f"The monster {self.name} attacks!")
    print(f'{amount} of hp damage dealt!')
    monster.health -= amount
    print(f'{monster.health} hp to {monster.name} health remaining!')

  def move(self,speed):
    print(f'{self.name} moving at {speed} speed!')

monster_01 = Monster(100,20,'goblin')
monster_02 = Monster(200,20,'troll')
print(monster_01.attack(monster_02,15))
print(monster_01.move(10))