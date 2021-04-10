from django.urls import path
from CsvApp import views 

urlpatterns = [    
    path('', views.home, name="Home"),
    path('export', views.export, name="Export"),
    path('servicios', views.servicios, name="Servicios"),
]
