from django.contrib.auth.models import User, PermissionsMixin
from django.db import models
from rest_framework_simplejwt.tokens import RefreshToken

class CustomUser(User, PermissionsMixin):
    
    USER_TYPE_CHOICES = [
        ('customer', 'کاربر عادی'),
        ('courier', 'کاربر پیک')
    ]

    phone_number = models.CharField(max_length=12, unique=True)
    city = models.CharField(max_length=8, choices=[('tehran', 'تهران')])
    address = models.TextField()
    user_type = models.CharField(max_length=8, choices=USER_TYPE_CHOICES)
    register_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.username

