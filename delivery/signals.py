from django.db.models.signals import post_save
from django.dispatch import receiver
from user.models import CustomUser
from .models import Courier, Customer


@receiver(post_save, sender=CustomUser)
def create_cusomer(sender, instance, created, **kwargs):
    if  created:
        if CustomUser.user_type == 'customer':
            Customer.objects.create(user=instance)

def create_courier(sender, instance, created, **kwargs):
    if created:
        if CustomUser.user_type == 'courier':
            Courier.objects.create(user=instance)