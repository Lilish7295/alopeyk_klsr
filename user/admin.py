from django.contrib.admin import ModelAdmin, register
from .models import CustomUser, CourierRequest


@register(CustomUser)
class CustomUserAdmin(ModelAdmin):
    pass

@register(CourierRequest)
class CourierRequestAdmin(ModelAdmin):
    pass
