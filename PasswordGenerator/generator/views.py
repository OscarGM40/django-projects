from django.shortcuts import render
#  realmente devolver una HttpResponse no tiene mucho sentido
# from django.http import HttpResponse
import random

# hay que recoger el objeto request como argumento en cada controlador
def about(request):
   # return HttpResponse("<h1>About</h1>")
   return render(request,'generator/about.html')

def home(request):
   return render(request,'generator/home.html')

def password(request):
   characters = list('abcdefghijklmnopqrstuvwxyz')
   generated_password = ''
   
   length = int(request.GET.get('length'))
   # si viene como queryParam 'uppercase' 
   if(request.GET.get('uppercase')):
      characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')) 
      
   if(request.GET.get('special')):
      characters.extend(list('!@#$%^&*()-_+<>?/'))

   if(request.GET.get('numbers')):
      characters.extend(list('0123456789'))
   
   for char in range(0,length,1):
      generated_password += random.choice(characters)
      
   # fijate que debo devolver un diccionario con los pares de valores que desee a la template
   return render(request,'generator/password.html',{'password': generated_password})