# pylint: disable-all

# scope problem with variables
def update_health(amount):
    global health  # sin global health tiene scope local
    health += amount


health = 10

print(health)
update_health(20)
print(health)

# objects doesn't have local scope for their attributes
def update_health_of_object(amount):
    monster.health += amount


class Monster:
    def __init__(self, health, energy):
        self.health = health
        self.energy = self.set_energy(energy)

    def update_energy(self, amount):
        self.energy += amount

    def set_energy(self,energy):
        new_energy = energy * 2
        return new_energy

    def get_damage(self,amount):
        self.health -= amount

# exercise
# create a hero class with 2 parameters: damage, monster
# the monster class should have a method that lowers the health(get_damage)
# the hero class should have an attack method that calls the get_damage method from the monster
# the amount of damage is hero.damage

class Hero:
  def __init__(self,damage,monster):
    self.damage = damage
    self.monster = monster

  def attack(self):
    self.monster.get_damage(self.damage)

monster = Monster(health=100, energy=50)
update_health_of_object(20)
monster.update_energy(amount = 75)
print(monster.health)
print(monster.energy)
#fijate que en Python puedo pasarle arg = value o solo el value
hero = Hero(damage = 10,monster = monster)
hero.attack()
print(hero.monster.health)