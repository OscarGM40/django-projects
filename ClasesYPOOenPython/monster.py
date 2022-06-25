# pylint: disable-all
# recuerda que en Python se usa snake_case
class Monster():
    # fijate que al añadir valores por defecto puedo sobrescribirlos o no
    # no es muy común esto,realmente en Python
    health = 90
    energy = 40

    # cualquier método en Python,incluso el constructor, empieza con def
    def __init__(self, health, energy, name):
        print(f'The mosnter {name} was created!')
        self.health = health
        self.energy = energy
        self.name = name
    # con este dunder puedo sobrescribir lo que devuelva la ejecución de len()
    def __len__(self):
      return 53
    # incluso hay un dunder para que el objeto sea llamado como si fuera un método
    def __call__(self):
      return 'the monster has been called'
    # puedo sobrescribir lo que hará sumar algo sobre el objeto
    def __add__(self,other):
      return f'the monster healths in {other} quantity.Now is health is {self.health + other}'
    def __str__(self):
      return f'Hi!: I am the monster {self.name} with {self.health} of health'
    # Python automáticamente pasa siempre una referencia a la clase como primer argumento en cualquier método que cree.Por convención se llama self
    def attack(self, monster, amount):
        print(f"The monster {self.name} attacks!")
        print(f'{amount} of hp damage dealt!')
        monster.health -= amount
        print(f'{monster.health} hp to {monster.name} health remaining!')

    def move(self, speed):
        print(f'{self.name} moving at {speed} speed!')


monster_01 = Monster(100, 20, 'goblin')
monster_02 = Monster(200, 20, 'troll')
print(monster_01.attack(monster_02, 15))
print(monster_01.move(10))
# dado que sobreescribí el dunder __len__ dará 53
print(len(monster_01))
# con dir(instancia) puedo ver todos los dunders además de los atributos
print(dir(monster_01))
print(monster_01() )
print(monster_01 + 20)
print(monster_01)