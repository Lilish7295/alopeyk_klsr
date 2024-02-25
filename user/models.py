from django.contrib.auth.models import User
from django.db import models

class CustomUser(User):
    
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
    

class CourierRequest(models.Model):
    
    STATUS_CHOICES = [
        ('pending','در انتظار'),
        ('accepted','پذیرفته شده'),
        ('rejected','رد شده'),
    ]

    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default='pending')
    
    def __str__(self):
        return 'user {} courier_request {}'.format(self.user, self.status)
