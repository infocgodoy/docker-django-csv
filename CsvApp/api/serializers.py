from rest_framework import serializers
from CsvApp.models import MasterProductsConfigurable 

class MasterProductsConfigurableSerializer(serializers.ModelSerializer):
    class Meta:
        model = MasterProductsConfigurable
        fields = ['model','name','price']

