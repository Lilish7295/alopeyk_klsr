from typing import Any, Dict
from .models import CustomUser
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenRefreshSerializer


class CustomUserSerializer(serializers.ModelSerializer):
   
    class Meta:
        
        model = CustomUser
        fields = (
            'username', 'phone_number' ,
            'password', 'city', 'user_type',
        )
        