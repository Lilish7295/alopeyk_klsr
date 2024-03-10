from django.contrib.admin import ModelAdmin, register
from .models import Package, Feedback
from user.models import CustomUser


@register(Package)
class PackageAdmin(ModelAdmin):
    list_display = ('id', 'customer', 'courier')

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "customer":
            kwargs["queryset"] = CustomUser.objects.filter(user_type='customer')
        elif db_field.name == "courier":
            kwargs["queryset"] = CustomUser.objects.filter(user_type='courier')
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


@register(Feedback)
class FeedbackAdmin(ModelAdmin):
    pass
