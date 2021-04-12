from django.urls import path
from CsvApp import views 
from CsvApp.management.commands import export

urlpatterns = [    
    path('', views.home, name="Home"),
    path('export', views.export, name="Export"),
    path('servicios', views.servicios, name="Servicios"),
    path('exports', export.Command.handle, name="exports"),
]
