
class Monster:
  def __init__(self, health, energy,**kwargs):
    print(kwargs)
    self.health = health
    self.energy = energy
    super().__init__(**kwargs)

  def attack(self, amount, other):
    print(f'The monster has attacked!')
    print(f'{amount} damage was dealt')
    other.health -= amount
    self.energy -= 20

  def move(self, speed):
    print('The monster has moved')
    print(f'It is moving at a speed of {speed}')

class Fish:
  def __init__(self, speed, has_scales,**kwargs):
    print(kwargs)
    self.speed = speed
    self.has_scales = has_scales
    super().__init__(**kwargs)

  def swim(self):
    print(f'The fish is swimming at a speed of {self.speed}')
   
   # mro stands for method resolution order 
class Shark(Monster,Fish):
  def __init__(self,bite_strength,health,energy,speed,has_scales):
    self.bite_strength = bite_strength
    super().__init__(
      health=health,
      energy=energy,
      speed=speed,
      has_scales=has_scales)
    
# print(Shark.mro())

shark = Shark(
  bite_strength = 50,
  health = 250,
  energy = 55,
  speed = 120,
  has_scales = True)
shark.swim()

sharknado = Shark(
  bite_strength = 40,
  health = 250,
  energy = 65,
  speed = 100,
  has_scales = False)
sharknado.swim()
sharknado.attack(20,shark)