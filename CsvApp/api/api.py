from rest_framework.response import Response
from rest_framework.views import APIView
from CsvApp.models import MasterProductsConfigurable
from CsvApp.api.serializers import MasterProductsConfigurableSerializer

class MasterProductsConfigurableAPIView(APIView):

    def get(self,request):
        productos = MasterProductsConfigurable.objects.all()
        productos_serializer = MasterProductsConfigurableSerializer(productos,many = True)
        return Response(productos_serializer.data)