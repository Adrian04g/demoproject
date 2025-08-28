from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
#Ejemplo de la lectura
def index(request):
    return HttpResponse("Hello, world. You're at the demoapp index.")
#Ejemplo de otra vista
def other_view(request):
    return HttpResponse("This is another view in demoapp.")
#Ejemplo de pantalla de inicio
def home(request):
    content = "<html><body><h1>Welcome to the Home Page</h1></body></html>"
    return HttpResponse(content)
#Ejemplo de lectura de objetos request y response
def indext(request): 
    path = request.path 
    method = request.method 
    content=''' 
<center><h2>Testing Django Request Response Objects</h2> 
<p>Request path : " {}</p> 
<p>Request Method :{}</p></center> 
'''.format(path, method) 
    return HttpResponse(content)
# Ejemplo de parametros en la URL
def pathview(request, name, id):
    name = "Adrian"
    id = 12345
    return HttpResponse("Hello:{} Your ID is {}".format(name, id))
# Ejemplo de cadena de consulta
def qryview(request): 
    name = request.GET['name'] 
    id = request.GET['id'] 
    return HttpResponse("Name:{} UserID:{}".format(name, id)) 
#Ejemplo de formulario
def showform(request): 
    return render(request, 'form.html')
def getform(request):
    if request.method == 'POST': 
        name = request.POST['name'] 
        id = request.POST['id'] 
        return HttpResponse("Name:{} UserID:{}".format(name, id)) 
    else: 
        return HttpResponse("Error: Form submission failed.")
