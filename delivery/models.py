from typing import Any
from django.db import models
from user.models import CustomUser

class Courier(models.Model):
    
    first_name = models.CharField(max_length=100, default=None)
    last_name = models.CharField(max_length=100, default=None)
    phone_number = models.ForeignKey(CustomUser,
        on_delete=models.CASCADE, related_name='phone', default=None)
    condition = models.TextField(default=None)

    def __str__(self) -> str:
        return "{} {}".format(self.first_name, self.last_name)
    

class Customer(models.Model):
    
    first_name = models.CharField(max_length=100, default=None)
    last_name = models.CharField(max_length=100, default=None)
    adress = models.ForeignKey(CustomUser,
        on_delete=models.CASCADE, related_name='adrs', default=None)
    phone_number = models.ForeignKey(CustomUser,
        on_delete=models.CASCADE, related_name='phones', default=None)
    user_name = models.ForeignKey(CustomUser,
        on_delete=models.CASCADE, related_name='user', default=None)
    password = models.ForeignKey(CustomUser,
        on_delete=models.CASCADE, related_name='passw', default=None)
    registery_date = models.ForeignKey(CustomUser,
        on_delete=models.CASCADE, related_name='rg_date', default=None)

    def __str__(self) -> str:
        return "{} {}".format(self.first_name, self.last_name)
    

class Package(models.Model):
    
    STATUS_CHOICES = [
        ('waiting', 'منتظر قبول پبک'),
        ('the_way_to_pickup', 'پیک در راه مبدا'),
        ('the_way_to_deliver', 'پیک در راه مقصد'),
        ('delivered', 'انجام شد'),
        ('canceled', 'لغو شد'),
    ]
    origin_long = models.FloatField(default=None)
    origin_lat = models.FloatField(default=None)
    destination_long = models.FloatField(default=None)
    destination_lat = models.FloatField(default=None)
    status = models.CharField(max_length=30,
        choices=STATUS_CHOICES, default='waiting')
    pick_date = models.DateTimeField(null=True, blank=True, default=None)
    deliver_date = models.DateTimeField(null=True, blank=True, default=None)
    customer = models.ForeignKey(Customer,
        on_delete=models.CASCADE, null=True, blank=True, default=None)
    courier = models.ForeignKey(Courier,
        on_delete=models.CASCADE, null=True, blank=True, default=None)
    condition = models.TextField(null=True, blank=True, default=None)

    def __str__(self) -> str:
        return "{}-{}'s package".format(self.pk,self.status)
    

class Feedback(models.Model):
    
    RATING_CHOICES = [
        (1, '1 - very bad'),
        (2, '2 - bad'),
        (3, '3 - avrage'),
        (4, '4 - good'),
        (5, '5 - excellent'),
    ]
    package = models.ForeignKey(Package, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=RATING_CHOICES, default='2 - bad')
    comments = models.TextField(blank=True, null=True, default=None)
    date = models.DateTimeField(default=None)

    def __str__(self):
        return 'feedback for order {} rating: {}'.format(self.package.id, self.rating)    

