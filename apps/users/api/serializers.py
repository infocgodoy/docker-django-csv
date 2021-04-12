from rest_framework import serializers
from apps.users.models import User,MasterProductsConfigurable

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'  #['name','edad']
      
        