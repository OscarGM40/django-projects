# pylint: disable-all
def add(a, b):
    return a + b


# como en Python todo es un object puedo guardar una funcion en una variable
a = add
# fijate que el método dir es super-useful.LLamar a dir sobre una función mostrará el dunder __call__,entre muchos otros.
print(dir(add))


class Test:
    def __init__(self, add_function):
        # fijate como en Python creo propiedades 'on the fly'.Genial
        self.add_function = add_function


# y fijate como esa propiedad es una función,de nuevo porque todo es un object en Python.Awesome
test = Test(add_function=add)
print(test.add_function(1, 2))

# create a Monster class with a parameter called func,
class Monster:
    def __init__(self, func):
        self.func = func


# create a class called Attacks,that has 4 methods: bite,strike,slash and kick(they just print some str)
class Attacks:
    def __init__(self):
        pass

    def bite(self):
        print('bitting...')

    def strike(self):
        print('striking...')

    def slash(self):
        print('slashing...')

    def kick(self):
        print('kicking...')

attacks = Attacks()
# fijate como acepta cualquier cosa como parametro de clase Python
monster = Monster(attacks.bite)
# realmente no tengo porque instanciar Attacks,lo puedo pasar a un Objeto llamando,ya que una Class tiene el método __call__
monster2 = Monster(Attacks().bite) # forma PRO TOTAL
# y llamo al método,muy asinto todo
monster.func()

