from .models import CustomUser, CourierRequest
from rest_framework import serializers


class CustomUserSerializer(serializers.ModelSerializer):
   
    class Meta:
        
        model = CustomUser
        fields = (
            'username', 'phone_number' ,
            'password', 'city', 'user_type',
        )


class CourierRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourierRequest
        fields = '__all__'
        