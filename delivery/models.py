from typing import Any
from django.db import models


class Courier(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=12)
    condition = models.TextField()

    def __str__(self) -> str:
        return "{} {}".format(self.first_name, self.last_name)
    

class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    adress = models.TextField()
    phone_number = models.CharField(max_length=12)
    user_name = models.CharField(max_length=100)
    password = models.CharField(max_length=10)
    registery_date = models.DateTimeField()

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
    origin_long = models.FloatField()
    origin_lat = models.FloatField()
    destination_long = models.FloatField()
    destination_lat = models.FloatField()
    status = models.CharField(max_length=30,
        choices=STATUS_CHOICES, default='waiting')
    pick_date = models.DateTimeField(null=True, blank=True)
    deliver_date = models.DateTimeField(null=True, blank=True)
    customer = models.ForeignKey(Customer,
        on_delete=models.CASCADE, null=True, blank=True)
    courier = models.ForeignKey(Courier,
        on_delete=models.CASCADE, null=True, blank=True)
    condition = models.TextField(null=True, blank=True)

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
    rating = models.IntegerField(choices=RATING_CHOICES)
    comments = models.TextField(blank=True, null=True)
    date = models.DateTimeField()

    def __str__(self):
        return 'feedback for order {} rating: {}'.format(self.package.id, self.rating)    

