from .models import Courier, Customer, Package, Feedback
from rest_framework import serializers


class CourierSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Courier
        fields = "__all__"


class CustomerSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Customer
        fields = "__all__"


class PackageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Package
        fields = ['id', 'origin_long', 'origin_lat',
            'destination_long', 'destination_lat', 'status',
            'pick_date', 'deliver_date', 'customer', 'courier', 'condition']


class FeedbackSerializer(serializers.ModelSerializer):

    class Meta:
        model = Feedback
        fields = "__all__"