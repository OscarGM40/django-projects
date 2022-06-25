# 1 match/case -> simplified if/elif statements
# Pythonic way to do the same thing.Python tiene ya un match/case inbuild(ojo,desde python 3.10)
a = 2
# forma beginner
if a == 0:
    print('a is zero')
elif a == 1:
    print('a is one')
elif a == 2:
    print('a is two')
# forma pro
match a:
  case 0: print('a is 0')
  case 1: print('a is 1')

# 2- ternary operator / single line if statement
# python tiene su propia versión de un operador ternario 
day_time = False
print(f"The day is {'bad' if day_time else 'good'}")

# 3 - chain comparisons.Puedo encadenar comparaciones para comparar si un valor esta entre un maximo y un minimo
min_value = 0
max_value = 10
value = 5

#forma menos legible:
if min_value < value and  max_value > value:
    print('value is between min and max')
# pero es mejor encadenar comparadores.Además,se puede hacer en cualquier lenguaje
if min_value < value < max_value:
    print('value is between min and max')

# 4 - si quiero que una variable nunca pase de un rango,puedo usar min y max
# while True:
#     value += 0.0001
#     #forma menos legible
#     if value > max_value:
#         value = max_value
#     elif value < min_value:
#         value = min_value
#     # forma pro
#     value = max(min_value,min(value,max_value))
            
# 5 - eval + exec Imaginando que tengo una variable sobre la que quiero ejecutar varios métodos puedo usar la función eval() para mayor legibilidad
test_string = 'hello'

# en vez de.
print(test_string.upper())
print(test_string.lower())
print(test_string.casefold())
print(test_string.title())
# puedo usar una tupla para pasarle los métodos a eval()
for operation in ['upper', 'lower','casefold','title']:
    print(f"{operation}: {eval(f'{operation}(test_string)')}")
# aunque obviamente es algo que no usaré mucho

# 6 - dict.get(): Realmente no se suele saber las keys de un diccionario/map de antemano.Puedo usar dict.get(key) para que no pete cuando intente acceder al valor de una key que no existe

test_dict = {'a':1,'b':2,'c':3}
if test_dict.get('d') is None:
    print('d is not in the dict')

# list flattening with sum() Imagina una tupla que tenga otras tuplas en su interior,y quiero sacarla a una tupla de 1 dimensión(flatMap de Javascript)
test_list = [1,2,3,[4,5,6],[7,8]] 
# en python en vez de flatMap puedo usar sum(2Dlist,[]) pasandole una tupla vacia.Lamentablemente sólo funciona para arrays de 2D
print(sum(test_list,[]))