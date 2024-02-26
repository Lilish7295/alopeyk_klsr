from django.contrib.admin import ModelAdmin, register
from .models import Courier, Customer, Package, Feedback


@register(Courier)
class CourierAdmin(ModelAdmin):
    pass


@register(Customer)
class CustomerAdmin(ModelAdmin):
    pass


@register(Package)
class PackageAdmin(ModelAdmin):
    pass


@register(Feedback)
class FeedbackAdmin(ModelAdmin):
    pass
