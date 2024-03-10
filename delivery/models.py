from typing import Any
from django.db import models
from user.models import CustomUser
    

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
    pick_date = models.DateTimeField(null=True, blank=True)
    deliver_date = models.DateTimeField(null=True, blank=True)
    customer = models.ForeignKey(CustomUser, on_delete=models.CASCADE, 
        related_name='customer', null=True, blank=True)
    courier = models.ForeignKey(CustomUser, on_delete=models.CASCADE,
         related_name='courier', null=True, blank=True)
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
    rating = models.IntegerField(choices=RATING_CHOICES, default='2 - bad')
    comments = models.TextField(blank=True, null=True)
    date = models.DateTimeField(default=None)

    def __str__(self):
        return 'feedback for order {} rating: {}'.format(self.package.id, self.rating)    

