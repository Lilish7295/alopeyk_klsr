from .models import CustomUser
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class CustomUserSerializer(serializers.ModelSerializer):
   
    class Meta:
        
        model = CustomUser
        fields = (
            'id', 'username', 'phone_number' ,
            'city', 'adress', 'user_type', 'register_date'
                )
        

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    
    def validate(self, attrs):
        
        data = super(CustomTokenObtainPairSerializer, self).validate(attrs)
        return data