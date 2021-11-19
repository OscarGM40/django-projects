from django.shortcuts import render
#  realmente devolver una HttpResponse no tiene mucho sentido
# from django.http import HttpResponse


# hay que recoger el objeto request como argumento en cada controlador
def about(request):
   # return HttpResponse("<h1>About</h1>")
   return render(request,'about.html')