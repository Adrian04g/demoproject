from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('home', views.pathview, name='home'),
    #Ejemplo de parametros en la URL
    path('getuser/<name>/<id>', views.pathview, name='pathview'),
    #Ejemplo de cadena de consulta
    path('getuser/consulta', views.qryview, name='qryview'),
    #ejemplo de formulario
    path('showform', views.showform, name='showform'),
    path('getform', views.getform, name='getform'),
]