from django.urls import path
from myapp import views

urlpatterns = [
    #url con parametros
    path('dishes/<str:dish>', views.menuitems, name='dishview'),
]