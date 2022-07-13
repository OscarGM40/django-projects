def decorator(func):
  def wrapper(wrapper_parameter): #parameter
    print('decoration begins')
    func(wrapper_parameter) #argument
    print('decoration ends')
  return wrapper

@decorator
def func(func_parameter):
  print(func_parameter)

func('hello')

# a una funcion se le pasan parametros,pero se le llama con argumentos ??