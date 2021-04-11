from django.urls import path
from CsvApp.api.api import MasterProductsConfigurableAPIView

urlpatterns = [
    path('producto/',MasterProductsConfigurableAPIView.as_view(), name = 'usuario_api')
]