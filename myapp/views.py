from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the myapp index.")
# Vista que maneja la URL con parametros
def menuitems(request, dish):
    items = {
        'pasta': 'Pasta with tomato sauce',
        'pizza': 'Pizza with cheese and pepperoni',
        'salad': 'Fresh garden salad'
    }
    description = items[dish]
    return HttpResponse(f"<h1>{dish}</h1>" + description)
    