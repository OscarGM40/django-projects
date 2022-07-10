# si imprimo la referencia a una funcion,puedo ver que es un object y su puntero a la memoria.Recuerda que en Python todo es un objeto
def func():
  print(f'Function')

# esto es un decorador,recibe una funcion por argumento,obviamente
def wrapper(func):
  print('hello')
  func()
  print('goodbye')

#el segundo paso es entender que una funcion puede retornar otra
def function_generator():
  def new_function():
    print('New function')
  return new_function

print(func) # impresion de la referencia a la funcion/objeto
wrapper(func)

new_function = function_generator()
new_function()

