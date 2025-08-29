from django.urls import path
from myapp import views

app_name = 'myapp'

urlpatterns = [
    #url con parametros
    path('dishes/<str:dish>', views.menuitems, name='dishview'),
    path('', views.index, name='index'),
]