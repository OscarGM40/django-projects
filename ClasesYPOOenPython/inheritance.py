# pylint: disable-all

class Monster:
    def __init__(self, health, energy):
        self.health = health
        self.energy = energy

    def attack(self, amount, other):
        print(f'The monster has attacked!')
        print(f'{amount} damage was dealt')
        other.health -= amount
        self.energy -= 20

    def move(self, speed):
        print('The monster has moved')
        print(f'It is moving at a speed of {speed}')


class Shark(Monster):
    def __init__(self, speed, health, energy):
        super().__init__(health, energy)
        self.speed = speed

    def bite(self):
        print(f'The shark has bitten')
    # para sobrescribir un método simplemente lo llamo igual
    def move(self):
      print(f'The shark is moving at {self.speed} speed!')



shark = Shark(30,100,100)
shark2 = Shark(speed=30,health = 100,energy = 100)
shark.attack(10,shark2)
print(shark2.health)

# create Scorpion class which inherits from Monster
# health and energy from the parent
# poison damage attr
# overwrite the damage method to show poison damage
class Scorpion(Monster):
  def __init__(self,poison_dmg,scorpion_health,scorpion_energy):
    self.poison_dmg=poison_dmg
    super().__init__(scorpion_health,scorpion_energy)
    
  
  def attack(self):
    print(f'Scorpion attacking with an amount of {self.poison_dmg} poison damage')

scorpion = Scorpion(50,100,30)
scorpion.attack()
scorpion.move(15)
print(scorpion.energy)