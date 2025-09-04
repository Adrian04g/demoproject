# manejo de errores 
from django.http import HttpResponse, HttpResponseNotFound

def handler404(request, exception):
    return HttpResponse("<h1>Page not found</h1>")

def handle_404(request):
    return HttpResponseNotFound("<h1>Custom 404 Page Not Found</h1>")