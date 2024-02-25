from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import CourierRequest


@receiver(post_save, sender=CourierRequest)
def update_user_type_courier_request(sender,
instance, created, **kwargs):
    print("hello")
    if  instance.status == 'accepted':
        user = instance.user
        user.user_type = 'courier'
        user.save()
        print("hello")